#!/usr/bin/env python3
"""Digitize simple line/point plots using Codex-provided visual calibration.

The script assumes linear axes. It intentionally avoids OCR: labels and tick
values must be supplied in the JSON config after visual inspection.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def load_image(path: Path) -> Image.Image:
    return Image.open(path).convert("RGB")


def linear_map(pixel: float, ticks: list[dict]) -> float:
    if len(ticks) < 2:
        raise ValueError("Each numeric axis needs at least two calibration ticks.")
    p1, v1 = float(ticks[0]["pixel"]), float(ticks[0]["value"])
    p2, v2 = float(ticks[1]["pixel"]), float(ticks[1]["value"])
    if p1 == p2:
        raise ValueError("Calibration tick pixels must differ.")
    return v1 + (pixel - p1) * (v2 - v1) / (p2 - p1)


def inverse_linear_map(value: float, ticks: list[dict]) -> float:
    p1, v1 = float(ticks[0]["pixel"]), float(ticks[0]["value"])
    p2, v2 = float(ticks[1]["pixel"]), float(ticks[1]["value"])
    if v1 == v2:
        raise ValueError("Calibration tick values must differ.")
    return p1 + (value - v1) * (p2 - p1) / (v2 - v1)


def dark_mask(img: Image.Image, threshold: int) -> np.ndarray:
    arr = np.asarray(img)
    gray = arr.mean(axis=2)
    return gray <= threshold


def crop_mask(mask: np.ndarray, roi: list[int]) -> tuple[np.ndarray, int, int]:
    left, top, right, bottom = [int(x) for x in roi]
    return mask[top:bottom, left:right], left, top


def shared_axis_rows(mask: np.ndarray, config: dict) -> list[dict]:
    shared = config["shared_axis"]
    shared_col = shared["column"]
    shared_orientation = shared.get("orientation", "y")
    sample_values = shared["sample_values"]
    rows = []

    for shared_value in sample_values:
        row = {shared_col: shared_value}
        for series in config["series"]:
            roi_mask, left, top = crop_mask(mask, series["roi"])
            orientation = series.get("orientation", "x")
            shared_pixel = inverse_linear_map(shared_value, shared["ticks"])

            if shared_orientation == "y" and orientation == "x":
                local_y = int(round(shared_pixel - top))
                band = roi_mask[max(0, local_y - 2):min(roi_mask.shape[0], local_y + 3), :]
                ys, xs = np.where(band)
                if len(xs):
                    pixel = float(xs.mean() + left)
                    row[series["column"]] = round(linear_map(pixel, series["ticks"]), 4)
                else:
                    row[series["column"]] = ""
            elif shared_orientation == "x" and orientation == "y":
                local_x = int(round(shared_pixel - left))
                band = roi_mask[:, max(0, local_x - 2):min(roi_mask.shape[1], local_x + 3)]
                ys, xs = np.where(band)
                if len(ys):
                    pixel = float(ys.mean() + top)
                    row[series["column"]] = round(linear_map(pixel, series["ticks"]), 4)
                else:
                    row[series["column"]] = ""
            else:
                raise ValueError("Unsupported shared/series orientation combination.")
        row["备注"] = "估计"
        rows.append(row)
    return rows


def long_rows(mask: np.ndarray, config: dict, points: int) -> list[dict]:
    rows = []
    for series in config["series"]:
        roi_mask, left, top = crop_mask(mask, series["roi"])
        ys, xs = np.where(roi_mask)
        if not len(xs):
            continue
        order = np.argsort(xs)
        xs, ys = xs[order], ys[order]
        bins = np.array_split(np.arange(len(xs)), max(1, points))
        for idx in bins:
            if not len(idx):
                continue
            px = float(xs[idx].mean() + left)
            py = float(ys[idx].mean() + top)
            rows.append({
                "曲线名称": series.get("name", "曲线"),
                config["x_axis"].get("label", "横坐标数值"): round(linear_map(px, config["x_axis"]["ticks"]), 4),
                config["y_axis"].get("label", "纵坐标数值"): round(linear_map(py, config["y_axis"]["ticks"]), 4),
                "备注": "估计",
            })
    return rows


def connected_components(binary: np.ndarray) -> list[list[tuple[int, int]]]:
    visited = np.zeros(binary.shape, dtype=bool)
    components = []
    h, w = binary.shape
    for y in range(h):
        for x in range(w):
            if not binary[y, x] or visited[y, x]:
                continue
            q = deque([(y, x)])
            visited[y, x] = True
            comp = []
            while q:
                cy, cx = q.popleft()
                comp.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        if dy == 0 and dx == 0:
                            continue
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and binary[ny, nx] and not visited[ny, nx]:
                            visited[ny, nx] = True
                            q.append((ny, nx))
            components.append(comp)
    return components


def point_rows(mask: np.ndarray, config: dict) -> list[dict]:
    rows = []
    counter = 1
    for series in config["series"]:
        roi_mask, left, top = crop_mask(mask, series["roi"])
        min_pixels = int(series.get("min_pixels", 3))
        max_pixels = int(series.get("max_pixels", 200))
        for comp in connected_components(roi_mask):
            if not (min_pixels <= len(comp) <= max_pixels):
                continue
            ys = np.array([p[0] for p in comp], dtype=float)
            xs = np.array([p[1] for p in comp], dtype=float)
            px = float(xs.mean() + left)
            py = float(ys.mean() + top)
            rows.append({
                "点位编号": f"{series.get('name', '点位')}{counter}",
                "横坐标数值": round(linear_map(px, config["x_axis"]["ticks"]), 4),
                "纵坐标数值": round(linear_map(py, config["y_axis"]["ticks"]), 4),
                "备注": "估计",
            })
            counter += 1
    return rows


def write_tsv(rows: list[dict], out: Path | None) -> str:
    if not rows:
        text = "备注\n未识别到可用数据点\n"
        if out:
            out.write_text(text, encoding="utf-8")
        return text
    columns = list(rows[0].keys())
    for row in rows[1:]:
        for key in row.keys():
            if key not in columns:
                columns.append(key)
    lines = ["\t".join(columns)]
    for row in rows:
        lines.append("\t".join(str(row.get(col, "")) for col in columns))
    text = "\n".join(lines) + "\n"
    if out:
        out.write_text(text, encoding="utf-8")
    return text


def draw_overlay(img: Image.Image, config: dict, outdir: Path) -> None:
    overlay = img.copy()
    draw = ImageDraw.Draw(overlay)
    for series in config.get("series", []):
        if "roi" in series:
            draw.rectangle(series["roi"], outline="red", width=2)
    overlay.save(outdir / "overlay_check.png")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--tsv")
    parser.add_argument("--points", type=int, default=15)
    parser.add_argument("--threshold", type=int, default=150)
    parser.add_argument("--no-overlay", action="store_true")
    args = parser.parse_args()

    image_path = Path(args.image)
    config_path = Path(args.config)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    img = load_image(image_path)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    mask = dark_mask(img, args.threshold)

    mode = config["mode"]
    if mode == "shared_axis":
        rows = shared_axis_rows(mask, config)
    elif mode == "long":
        rows = long_rows(mask, config, args.points)
    elif mode == "points":
        rows = point_rows(mask, config)
    else:
        raise ValueError(f"Unsupported mode: {mode}")

    if not args.no_overlay:
        draw_overlay(img, config, outdir)

    tsv_path = Path(args.tsv) if args.tsv else None
    print(write_tsv(rows, tsv_path), end="")


if __name__ == "__main__":
    main()
