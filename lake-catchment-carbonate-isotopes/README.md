# Lake Catchment Carbonate Isotope Skill

## 中文说明

这是一个用于现代非海洋湖泊流域、汇水区、陆生、河流、土壤、泉水、溪流、tufa/travertine、PIC、SIC、碳酸盐包壳或相关碳酸盐同位素数据检索、下载、核查、提取、查重和整理的 Codex skill。

适用于以下任务：

- 全球湖泊流域碳酸盐数据提取
- 现代湖泊流域碳酸盐同位素整理
- 土壤碳酸盐、SIC、pedogenic carbonate 数据提取
- 河流 PIC、河流沉积物碳酸盐、悬浮物碳酸盐数据提取
- 泉水、溪流、河道、坡面、地下水出露形成的现代 tufa/travertine 数据判断
- 判断某篇文献、某类 tufa/travertine 或某组样品“能不能要”
- 将合格数据整理进总表的 `新增` sheet

## 主要工作流

该 skill 固定采用三个反馈节点：

1. **检索、筛选、下载与核验文献**
   - 优先检索 Google Scholar、Web of Science、CNKI。
   - 下载前先按关键词、纳入/排除规则和查重风险筛选候选文献。
   - 下载后核验文献标题、DOI、首页或附件信息是否与候选文献一致。
   - 遇到登录、验证码、机构权限或付费墙时，向用户反馈链接，由用户授权或手动下载。
   - 完成后暂停，等待用户确认文献已全部下载。

2. **从已下载文献中提取数据并写入 Excel**
   - 只提取可追溯的原始表格或正文数值，不从图上估数。
   - 按固定列写入总表的 `新增` sheet：
     `碳酸盐, Location, Latitude, Longitude, Elevation, 13C, 13Cstd, 18O, 18Ostd, 同位素类型, 参考文献, 备注`
   - 经纬度保持原文格式，不统一转换。
   - 数值小数位和单位尽量保持原文。
   - 所有判断依据写入中文备注或说明 sheet。
   - 完成后暂停，等待用户核验。

3. **用户核验后执行最终查重**
   - 将 `新增` 与总表指定 sheet 比对。
   - 使用语义碳酸盐类型、参考文献、数据、经纬度、位置、流域/区域相似性进行查重。
   - 保护连续相邻同来源数据，避免误判同一文献内部连续样品为重复。
   - 记录重复原因和对应总表行号。

## 纳入范围

可纳入现代、表层、active、recent、current 或合理判断为当代环境形成的非海洋碳酸盐同位素数据，包括：

- 流域基岩或流域背景岩石碳酸盐
- 河流悬浮物、河流 PIC、河流沉积物中的碳酸盐
- 土壤碳酸盐、SIC、pedogenic carbonate、nodule、filament、coating
- 泉水、溪流、河道、坡面、河谷、地下水出露形成的现代 tufa/travertine
- 人工片、plastic surface、pipe、well、outlet 上形成的现代淡水碳酸盐

## 排除范围

排除：

- 海洋、近海、潮间带或海相碳酸盐
- 湖内生成碳酸盐、湖泥自生碳酸盐、湖内贝壳、介形虫、lake marl
- 明确古老剖面、化石、地层样品、Holocene/Pleistocene/Quaternary 古沉积样品
- 只有图或曲线、没有原始数值的数据
- 综述、二手汇编或无法追溯原始样品表的数据
- 已经整理过且无需复查的文献

## tufa/travertine 判断原则

不按名称一刀切，而按形成环境判断。

可纳入：

- 泉水、冷泉、温泉、溪流、河道、瀑布、坡面、河谷、地下水出露、井口、管道、人工片上现代形成的 tufa/travertine。

排除：

- 湖泊内部、湖底、湖岸湖内系统、湖泊生物壳体或 lake marl 相关碳酸盐。

如果文章中同时出现 lake、pool、pond、fishpond 等词，需要核查样品实际是否来自湖内沉积；若来自溪流、泉口下游、河道坝状钙华等，仍可纳入，并在备注说明。

## 查重原则

候选数据满足以下任一条件时，可判定为重复：

1. 参考文献相同或高度相似，数据相同，碳酸盐类型基本相同。
2. 参考文献不同，但经纬度或位置相同，碳酸盐类型相同。
3. 参考文献不同，但位于同一流域、同一区域或经纬度位置相近，且碳酸盐类型相同。

特别注意：

- 连续相邻且同一来源/同一参考文献的行，不在内部互判重复。
- 全球汇编或多地点文献需要拆分为连续地点小区块，不能因其中一处重复而把整篇文献全部判为重复。

---

## English Description

This Codex skill is designed for searching, downloading, verifying, extracting, deduplicating, and organizing modern non-marine carbonate isotope data from lake catchments, watersheds, terrestrial systems, rivers, soils, springs, streams, tufa/travertine systems, PIC, SIC, carbonate coatings, and related source materials.

Use this skill for tasks involving:

- Global lake-catchment carbonate data extraction
- Modern lake-catchment carbonate isotope datasets
- Soil carbonate, SIC, and pedogenic carbonate extraction
- River PIC, suspended carbonate, and river sediment carbonate data
- Modern spring, stream, river, slope, groundwater-outlet tufa/travertine data
- Decisions about whether a paper, sample type, or tufa/travertine dataset should be included
- Generating Excel tables in the required master-table format

## Workflow

The skill follows three mandatory checkpoints:

1. **Search, screen, download, and verify literature**
   - Search Google Scholar, Web of Science, and CNKI.
   - Screen candidate papers before download using keywords, inclusion/exclusion rules, and duplicate-risk checks.
   - Verify downloaded papers and supplements by title, DOI, first page, or metadata.
   - If access is blocked by login, CAPTCHA, institutional permission, or paywall, report the link to the user.
   - Pause after this stage and wait for user confirmation.

2. **Extract data and write to Excel**
   - Extract only traceable original table or text values.
   - Do not estimate values from figures.
   - Write accepted rows to the `新增` sheet using the fixed columns:
     `碳酸盐, Location, Latitude, Longitude, Elevation, 13C, 13Cstd, 18O, 18Ostd, 同位素类型, 参考文献, 备注`
   - Preserve original coordinate formats and numeric precision.
   - Record evidence and decisions mainly in Chinese notes.
   - Pause after extraction for user review.

3. **Final deduplication after user review**
   - Compare the `新增` sheet against the specified master table sheet.
   - Deduplicate using reference similarity, data equality, coordinates, location, catchment/region similarity, and semantic carbonate-type equivalence.
   - Protect continuous rows from the same source so that adjacent samples from the same paper are not falsely marked as duplicates.
   - Record duplicate reasons and matched master-table row numbers.

## Inclusion Scope

Include modern, surface, active, recent, current, or reasonably contemporary non-marine carbonate isotope data, such as:

- Catchment bedrock or watershed rock carbonate
- River suspended carbonate, river PIC, or carbonate in river sediment
- Soil carbonate, SIC, pedogenic carbonate, nodules, filaments, or coatings
- Modern tufa/travertine from springs, streams, river channels, slopes, valleys, or groundwater outlets
- Modern freshwater carbonate precipitated on artificial tablets, plastic surfaces, pipes, wells, or outlets

## Exclusion Scope

Exclude:

- Marine, coastal, intertidal, or marine carbonate data
- Lake-internal carbonate, lake-bottom authigenic carbonate, shells, ostracods, and lake marl
- Fossil, stratigraphic, Holocene, Pleistocene, or Quaternary deposits unless active/recent/modern rows are explicitly separated
- Figure-only data without original numeric values
- Reviews or secondary compilations without traceable original sample tables
- Already organized papers unless the user requests rechecking

## Tufa/Travertine Rule

Do not include or exclude tufa/travertine by name alone. Judge by formation environment.

Include modern tufa/travertine formed in springs, streams, rivers, waterfalls, slopes, valleys, groundwater outlets, wells, pipes, or artificial surfaces.

Exclude lake-internal tufa/travertine, lake-bottom carbonates, lake biological carbonates, and lake marl.

If a paper mentions lake, pool, pond, or fishpond, inspect the actual sample setting before deciding.

## Deduplication Rule

A candidate is duplicate if:

1. The reference is the same or highly similar, the data are the same, and the carbonate type is semantically the same.
2. The reference differs, but coordinates/location are the same and the carbonate type is the same.
3. The reference differs, but the sample is from the same catchment/region or nearby coordinates, and the carbonate type is the same.

Continuous rows from the same source must not be deduplicated against each other. Broad multi-site papers should be split into small continuous site/location blocks before marking duplicates.