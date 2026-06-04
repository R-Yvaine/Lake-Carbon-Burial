---
name: lake-catchment-carbonate-isotopes
description: Use this skill when extracting or checking modern non-marine lake-catchment, watershed, terrestrial, river, soil, spring, tufa, travertine, PIC, SIC, carbonate coating, or carbonate isotope data from papers, PDFs, supplementary tables, Excel/Word files, or folders. Also use when the user says 全球湖泊流域碳酸盐数据提取, 现代湖泊流域碳酸盐同位素, 碳酸盐数据整理, tufa/travertine 能不能要, or asks to generate an Excel table for these data.
---

# Modern Lake-Catchment Carbonate Isotope Data

Use this skill to search, screen, download, verify, extract, deduplicate, and tabulate modern non-marine carbonate isotope data from lake catchments, watersheds, terrestrial systems, rivers, soils, springs, streams, tufa/travertine systems, carbonate coatings, PIC, SIC, and related source materials.

Default master workbook: `【总】现代湖泊流域碳酸盐同位素检索数据.xlsx`
Default download folder: `新增流域同位素文献`
Default output sheet for accepted new rows: `新增`

Fixed data columns:
`碳酸盐, Location, Latitude, Longitude, Elevation, 13C, 13Cstd, 18O, 18Ostd, 同位素类型, 参考文献, 备注`

## Mandatory Workflow Checkpoints

Follow these checkpoints in order. Do not skip a checkpoint unless the user explicitly says to skip it.

### Checkpoint 1: Search, Screen, Download, Verify

Use Browser / Chrome / Computer Use when available. Search only these sources unless the user expands scope:

- Google Scholar: `https://scholar.google.com.hk/`
- Web of Science: `https://www.webofscience.com/wos/woscc/smart-search`
- CNKI: `https://www.cnki.net/`

Workflow:

1. Create or reuse `新增流域同位素文献` under the current workspace.
2. Search with targeted keyword combinations, including English and Chinese terms for modern soil carbonate, pedogenic carbonate, SIC, river PIC, stream tufa/travertine, spring carbonate, carbonate coating, encrustation, δ13C, and δ18O.
3. Screen candidates before download by keyword relevance, inclusion/exclusion rules, tufa/travertine setting, and duplicate risk against the master workbook.
4. Download only plausible original-data papers or supplements. Prefer original tables and supplementary files over figure-only papers.
5. Verify every downloaded file: title/DOI/first page matches the candidate; supplementary file belongs to the article; filename is traceable; mismatches are excluded or flagged.
6. If login, CAPTCHA, institutional access, or paywall blocks download, ask the user to authorize login when interactive browser control is available. Otherwise report title, DOI/link, and why the user must download it.

After all searches finish, stop and report:

- Downloaded and verified candidate literature, with local filenames.
- Candidate literature not downloaded because of login, paywall, permission, or CAPTCHA.
- Links/DOIs for user authorization or manual download.
- Brief reason each candidate survived initial screening.

Do not extract data yet. Wait for the user to confirm all candidate literature has been downloaded, or that extraction should proceed with available files.

### Checkpoint 2: Extract Data And Write `新增`

After the user confirms the download set:

1. Process all files in `新增流域同位素文献`.
2. Apply inclusion/exclusion rules again from the actual full text and tables.
3. Extract only traceable original table/text values. Do not estimate from figures.
4. Write accepted rows to the master workbook sheet `新增`.
5. Preserve all fixed columns even if blank.
6. Preserve original coordinate formats; do not convert to decimal degrees.
7. Preserve original numeric precision and units; do not pad zeros, standardize rounding, or convert units unless requested.
8. Put Chinese explanations in `备注`, `核查说明`, and/or `排除原因`.
9. For excluded papers or samples, record Chinese reasons in `排除原因` or `核查说明`.

After extraction and table generation, stop and report:

- Number of files processed.
- Number of accepted papers/supplements.
- Number of rows written to `新增`.
- Excluded papers/samples and reasons.
- That the workbook is ready for user review.

Do not perform final deduplication yet unless the user explicitly authorizes it at this point.

### Checkpoint 3: Final Deduplication Against Master Table

After the user confirms the extracted `新增` sheet has been reviewed:

1. Compare `新增` against the master data sheet. Prefer `查重后总表` if present; otherwise use the current master sheet specified by the user.
2. Apply the duplicate rules below.
3. Remove or flag duplicate `新增` rows according to the user’s requested output style.
4. Record matched master row numbers and Chinese reasons.

Only after this final deduplication is complete should the workflow be considered finished.

## Inclusion Rules

Include modern/current/active/recent/surface lake-catchment or terrestrial carbonate isotope data. Modernity does not require dating if supported by sampling date, surface sample, active/recent/modern/current wording, ongoing formation, or present-day river/soil/spring environment.

Include:

- Catchment bedrock or watershed rock carbonate if used as watershed background/source data.
- River suspended sediment carbonate, river PIC, or carbonate in river sediment.
- Soil carbonate, SIC, pedogenic carbonate, soil carbonate nodule, filament, or coating if reasonably modern/surface/current.
- Modern tufa/travertine/carbonate coating/encrustation/fresh carbonate from springs, streams, rivers, slopes, valleys, groundwater outlets, wells, pipes, or artificial tablets/surfaces.
- Freshwater carbonate precipitated on artificial tablets, plastic surfaces, pipes, wells, or outlets when the setting is terrestrial/catchment and not lake-internal or marine.

Useful inclusion clues:
`active`, `recent`, `modern`, `current`, `surface sample`, `topsoil`, `suspended sediment`, `river PIC`, `stream`, `spring`, `downstream from spring`, `spring orifice`, `tufa dam`, `barrage`, `cascade`, `fresh carbonate`, `artificial tablet`, `plastic surface`, `pipe encrustation`, `soil inorganic carbon`, `pedogenic carbonate`.

## Exclusion Rules

Exclude:

- Marine, ocean, coastal, intertidal, or marine carbonate data.
- Lake-internal carbonate: lake-bottom authigenic carbonate, lake mud authigenic carbonate, lake shells, freshwater gastropods/bivalves, ostracods, lake biological carbonate, lake-internal tufa/travertine, lake marl.
- Clearly old sections, fossils, stratigraphic samples, Holocene/Pleistocene/Quaternary deposits, unless active/recent/modern rows are explicitly separated.
- Data only shown in figures/curves without original table/text values.
- Reviews, secondary compilations, or database descriptions unless the user explicitly asks to use them or the local file contains traceable original sample tables.
- Already organized papers or attachments unless the user explicitly asks to recheck or revise.

Cautious/exclusion clues:
`marine`, `ocean`, `coastal`, `lacustrine authigenic carbonate`, `lake sediment carbonate`, `shell`, `gastropod`, `bivalve`, `ostracod`, `lake marl`, `fossil`, `Holocene profile`, `Pleistocene`, `Quaternary mound`, `U-Th dated fossil`, `core`, `stratigraphic section`, `only plotted data`.

## Tufa/Travertine Judgment

Do not accept or reject by name alone. Judge by formation environment.

Accept:

- Spring, cold spring, hot spring, stream, river channel, waterfall, slope, valley, groundwater outlet, well, pipe, artificial tablet/surface modern tufa/travertine.

Exclude:

- Lake-internal, lake-bottom, lake-shore but lake-system internal, lake-waterfall internal carbonate, or biological shell carbonate.

If a paper contains words like `lake`, `pool`, `pond`, or `fishpond`, inspect the actual sample setting. If the sample is from a stream, spring outlet, downstream channel, barrage, cascade, or tufa dam rather than lake sediment, it may be included. Explain this in `备注`.

## Duplicate Checking Rules

Before adding new extracted rows to `新增`, compare them against the master workbook.

A candidate is duplicate if one of these is true:

1. Same or highly similar reference, same data, and basically the same carbonate type.
2. Different reference, same coordinates/location, and same carbonate type.
3. Different reference, same catchment/region or nearby coordinates/location, and same carbonate type.

Carbonate type equivalence is semantic, not exact text:

- `土壤`, `soil carbonate`, `pedogenic carbonate`, `SIC` are the same broad type.
- `tufa`, `travertine`, `钙华`, `stromatolite` in terrestrial/river/spring setting are the same broad type.
- `speleothem`, cave carbonate, cave calcite are the same broad type.
- `bedrock`, limestone, dolomite, rock carbonate are the same broad type.
- Lake sediment/authigenic/internal biological carbonate should usually be excluded before deduplication.

### Continuous-Row Protection

Never judge rows inside the same continuous citation/source run as duplicates of each other.

If rows are adjacent or part of a continuous block with the same or highly similar reference/source title, do not mark them as duplicates against each other, even when coordinates or region match.

For block marking or checking, split broad papers into small continuous location/site blocks:

- Same continuous source plus same site/location family = one small block.
- Do not mark unrelated sites from the same global compilation just because one site duplicates another source.

## Excel Output Rules

When writing extracted data:

1. Use fixed columns: `碳酸盐, Location, Latitude, Longitude, Elevation, 13C, 13Cstd, 18O, 18Ostd, 同位素类型, 参考文献, 备注`.
2. Put accepted new rows in sheet `新增`.
3. Preserve all columns even when blank.
4. All explanatory sheets must use Chinese names, e.g. `核查说明`, `排除原因`, `备注`, `下载记录`, `待用户下载`.
5. `备注` and `核查说明` must be mainly Chinese. Keep necessary English technical terms.
6. Preserve original coordinate format; do not convert to decimal degrees.
7. Preserve original numeric precision and units; do not pad zeros, standardize rounding, or convert units unless explicitly requested.
8. Reference column must contain the full article title plus table/supplement source when available. Do not use only abbreviated titles.
9. Isotope standard should be explicit when possible: VPDB, PDB, VSMOW, SMOW. If δ13C and δ18O standards differ, state that in `同位素类型` or `备注`. Do not convert standards unless explicitly requested.
10. Every accepted row should have a traceable basis in `备注`, including table/supplement name, modernity evidence, sample environment, and any judgment notes.
11. If no suitable data exist, write `没有可纳入数据` in an explanation sheet; do not invent placeholder rows.

## Recommended Workbook Sheets

Use or create these sheets as needed:

- `新增`: accepted new extracted rows.
- `核查说明`: per-paper inclusion/exclusion summary.
- `排除原因`: rejected files, duplicate papers, plotted-only data, marine/lake-internal/old samples, access issues.
- `下载记录`: searched title, source website, DOI/link, download status, local filename, title-match check.
- `待用户下载`: paywalled or login-blocked papers with links and reasons.

## Response Style

When the user asks “这个能不能要”, “这是什么”, or “对应哪篇文章”:

1. Give a clear conclusion first: `可纳入`, `排除`, or `暂不确定`.
2. Then give short evidence.
3. If uncertain but a working decision was made, say `我按……判断为纳入/排除` and mention the user can ask for recheck.

Do not modify Excel when the user only asks a question.

When the user asks to continue organizing or generate Excel, proceed with the process directly for available files. Do not repeatedly ask for confirmation except for login, paywall, download completion, user-review checkpoints, or genuinely ambiguous sample settings.