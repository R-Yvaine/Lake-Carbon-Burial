---
name: lake-isotope-literature-harvester
description: Automatically search, deduplicate, download, screen, extract, and tabulate modern lake isotope literature for lake carbonate/inorganic carbon sediment isotope workflows. Use when the user asks to search new lake isotope papers, download eligible literature, screen downloaded PDFs, extract lake metadata/isotope/dating/sample-time data, save review figures/tables, generate Excel-ready workbooks, or digitize lake carbonate/inorganic carbon isotope plots.
---

# Lake Isotope Literature Harvester

## Scope

Use this skill for three linked workflows:

1. Search for new lake isotope literature, deduplicate against the existing lake isotope Excel file, screen candidates, and download eligible papers.
2. Re-screen downloaded papers for inclusion, extract required metadata and isotope information, save review figures/tables, and create/update the Excel workbook `ry_现代湖泊流域同位素数据端元文献检索`.
3. Digitize isotope data from figures/tables in `新增湖泊同位素文献图表` and return one copyable TSV table directly in the final reply.

If the user does not specify a starting step, run the full workflow from Step 1. If the user asks to skip or start from a specific step, begin there.

Stop after each step and ask the user to review before continuing.

## Safety And Permissions

- Treat the current workspace as the working boundary unless the user explicitly requests another location.
- Do not modify the comparison Excel file `副本同位素湖泊部分点位_new20260611_ry`; read it only.
- Do not bypass paywalls, CAPTCHAs, login restrictions, publisher access controls, or download protections.
- If Google Scholar, Web of Science, CNKI, or publisher pages require login/manual action, report the obstacle and ask the user to provide access, PDFs, exported records, or permission to use alternative sources.
- Before overwriting any existing output workbook, ask whether to append, create a timestamped copy, or overwrite.
- Keep source PDFs and extracted figures/tables traceable to their paper title.

## Core Inclusion Rules

Apply these rules in both Step 1 candidate screening and Step 2 downloaded-paper screening.

Include only papers that meet all required conditions:

1. The study object is a modern lake or modern lake sediment system, preferably lake sediment cores.
2. The paper is not about only ancient lake basins, paleolake strata, ancient formations, or geological outcrops unrelated to modern lake sediments.
3. The paper contains original measured sample data, shown in tables, figures, supplementary data, or clear text. Exclude review papers without original measurements.
4. The paper contains stable carbon isotope or stable oxygen isotope data; either one is enough.
5. The isotope data must include inorganic carbon/carbonate sediment material, such as mixed/bulk carbonate, inorganic carbon, authigenic carbonate, endogenous carbonate, fine-fraction carbonate, or size-separated small carbonate fraction.
6. Exclude papers that contain only suspended particulate matter, DIC, organic carbon, water isotopes, or other non-sedimentary/non-carbonate isotope data.
7. Exclude papers where the only inorganic carbonate material is biological shell carbonate, such as mollusk shells, ostracod shells, or other purely biogenic shell material, unless the paper separately reports non-shell sediment carbonate/inorganic carbon isotope data.
8. If the paper describes authigenic/endogenic carbonate directly, treat it as potentially included.
9. If the paper describes grain-size separation and measures isotope values from the smaller/finer carbonate fraction, treat this as pointing to authigenic carbonate unless contradictory evidence exists.

If evidence is insufficient during Step 1, mark as `待全文确认` rather than rejecting. During Step 2, decide inclusion from the full downloaded paper.

## Deduplication Rules

Read `副本同位素湖泊部分点位_new20260611_ry` in read-only mode.

Exclude a candidate or downloaded paper as duplicate if either condition is true:

- The paper title is the same or very similar to an existing paper title.
- The lake name is the same or very similar and the dating method is the same or very similar.

Do not exclude solely because the lake name is similar if the dating method differs and the paper is different; keep it as potentially useful, especially when it provides a different chronology method or new isotope endpoint information.

Normalize case, punctuation, spaces, hyphens, lake/lac/湖/湖泊, and translated names before comparing.

If uncertain, mark as `疑似重复` and ask the user to review before including.

## Step 1: Search, Deduplicate, Download

Create or reuse `新增湖泊同位素文献`.

Search allowed sources first:

- `https://scholar.google.com.hk/`
- `https://www.webofscience.com/wos/woscc/smart-search`
- `https://www.cnki.net/`

Use targeted Chinese and English keyword combinations, including:

- 湖泊 稳定碳氧同位素
- 湖泊 稳定氧同位素
- 湖泊 混合碳酸盐 同位素
- 湖泊 自生碳酸盐 同位素
- 湖泊 内源碳酸盐 同位素
- 湖泊 细粒级 碳酸盐 同位素
- 湖泊 沉积柱 碳酸盐 δ13C δ18O
- 湖泊 沉积物 无机碳 同位素
- 湖泊 碳埋藏 无机碳 沉积 同位素
- lake sediment core carbonate isotope
- modern lake authigenic carbonate isotope
- lake endogenic carbonate δ13C δ18O
- lake bulk carbonate isotope sediment core
- lake inorganic carbon burial isotope

For each candidate, record title, authors/year, source link, visible lake name, likely sample type, likely isotope type, likely dating method, inclusion status (`纳入`, `排除`, `待全文确认`, or `疑似重复`), and reason.

Only download candidates that are `纳入` or `待全文确认` and not duplicate. Save eligible PDFs to `新增湖泊同位素文献` with clear names like `FirstAuthor_Year_ShortTitle.pdf`. If a PDF cannot be downloaded legally or automatically, save a citation/link note and report it in the Step 1 review.

End Step 1 by asking the user to review the candidate/download list before continuing.

## Step 2: Re-Screen, Extract, Save Figures/Tables, Build Excel

Read papers from `新增湖泊同位素文献`.

Before extracting data, inspect each downloaded paper and decide whether it truly meets the Core Inclusion Rules. For each downloaded paper, record:

- `纳入` or `排除`
- reason
- evidence location, such as method section, table number, figure number, supplementary table, or caption
- carbonate type judgment: `混合（整体）碳酸盐`, `无机碳`, `自生/内源碳酸盐`, `细粒级指示自生碳酸盐`, `仅生物壳体-排除`, or `不确定`

Only perform extraction for papers that pass Step 2 screening. If the paper fails Step 2 screening, do not add it to the output workbook, but mention it in the Step 2 review summary.

Create or reuse `新增湖泊同位素文献图表`. Save screenshots or extracted table/figure images containing inorganic carbon/carbonate sediment sample isotope data. Name each file with the corresponding paper title or safe shortened title, for example `FirstAuthor_Year_ShortTitle_Fig3_carbonate_isotopes.png`.

Create or update `ry_现代湖泊流域同位素数据端元文献检索.xlsx`. Before overwriting an existing workbook, ask whether to append, create a timestamped copy, or overwrite.

Create the table with these columns exactly:

序号
湖泊
统一湖泊湖泊
Lat（湖泊纬度）
Lon（湖泊经度）
采样时间
测年方法1（Pb Cs 14C等）
文献名称1
测年方法2
文献名称2
混合碳酸盐碳同位素
混合碳酸盐碳氧位素
自生碳酸盐碳同位素
自生碳酸盐氧同位素
湖水DIC的碳同位素
湖水DIC的氧同位素
碎屑碳酸盐的碳同位素
碎屑碳酸盐的氧同位素
入湖水体的碳同位素
入湖水体的氧同位素
备注

For each included lake/paper, extract lake name, unified lake name, latitude, longitude, sampling or coring time, dating method, paper title, lake-water DIC carbon/oxygen isotope values, detrital carbonate carbon/oxygen isotope values, and inflow water carbon/oxygen isotope values when available.

If one lake has multiple non-duplicate papers or methods, use repeated method/title pairs. Add more method/title columns only if necessary, and report that change to the user.

Leave these four columns blank at this stage even if the paper contains data:

- 混合碳酸盐碳同位素
- 混合碳酸盐碳氧位素
- 自生碳酸盐碳同位素
- 自生碳酸盐氧同位素

Fill all other columns whenever information is available.

In `备注`, clearly state whether detected sediment site/sample isotope data are inorganic carbon/carbonate data. Classify as `混合（整体）碳酸盐`, `无机碳`, `自生/内源碳酸盐`, `仅生物壳体-排除`, or `不确定`, and briefly mention evidence such as sieving size, fraction name, table caption, method sentence, or figure label.

End Step 2 by asking the user to review the included/excluded paper list, extracted fields, uncertain fields, figure/table files, and output workbook before continuing.

## Step 3: Digitize Figures/Tables And Return TSV

Use files saved in `新增湖泊同位素文献图表`.

Do not deliver an Excel file for Step 3. The final Step 3 result must be one TSV table pasted directly in the Codex reply so the user can copy it into Excel. Do not output multiple separate tables. Combine into one TSV when possible. Use Chinese column names and simple Chinese notes.

If the source is a table image or extracted table, directly transcribe the data into the final TSV.

For plot images, visually inspect coordinate axis labels, units, tick numbers, plot type, number of curves or point series, and whether multiple curves or points share the same x-axis or y-axis. If the axis is nonlinear, log-scaled, broken, or otherwise not linearly mappable, state that the default digitizing script is not suitable unless the user provides a transformation rule.

Use shared-axis format when multiple curves share one natural coordinate axis, such as Depth(cm): first column is the shared coordinate, e.g. `深度_cm`, and each curve gets one value column, e.g. `δ13C_数值`, `δ18O_数值`.

Use long format when curves cannot naturally align: `曲线名称`, `横坐标数值`, `纵坐标数值`, `备注`.

Use point format for independent scatter points: `点位编号`, `横坐标数值`, `纵坐标数值`, `备注`.

Create a calibration JSON before running the digitizing script. Use at least two calibration points for each numeric axis. `roi` means `[left, top, right, bottom]` in pixels. Keep the ROI around the curve/points and avoid axes, text, scale bars, and legends.

Run the bundled script:

```bash
python scripts/digitize_plot.py --image image.png --config calibration.json --outdir output --tsv table.tsv
```

Common options:

```bash
--points 15
--threshold 150
--no-overlay
```

Use `--tsv table.tsv` on Windows to preserve Chinese text and δ symbols. Read the TSV file and paste its content into the final reply. If visual checking is needed, generate `overlay_check.png`, inspect it, and revise calibration or ROI before finalizing.

Return one TSV table directly in the reply, for example:

```tsv
深度_cm	δ13C_数值	δ18O_数值	δ13Corg_数值	备注
0	-2.9	-8.0	-26.5	估计
10	-2.4	-7.6	-26.1	可靠
```

Rules:

- Do not provide only a file path.
- Do not output multiple tables.
- Keep numbers as Arabic numerals.
- Use simple remarks such as `可靠`, `估计`, `重叠不确定`, `坐标轴不确定`, `需人工复核`.
- If uncertainty is high, add one or two Chinese sentences after the table explaining what needs review.
