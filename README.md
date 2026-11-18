# Quantitative Analysis of Shared Bike Externalities and Optimal Deployment at Metro Station Areas in Haidian District, Beijing

**基于海淀区多地铁站出口数据的共享单车外部性与最优投放量实证研究**

*An empirical study based on multiple metro station exits in Haidian District, Beijing.*

---

## About / 简介

A course research paper examining the negative externality created when dockless
shared bikes cluster around metro station exits. Using on-site counts and a
marginal-analysis framework (marginal private cost, marginal external cost,
marginal private benefit and marginal external benefit), the paper estimates
private and socially optimal parking densities and quantifies the welfare loss
from over-deployment, then discusses density caps, tidal rebalancing and
platform assessment policies.

本研究以北京市海淀区多个地铁站出口为样本，通过实地计数与问卷调查量化共享单车
过度投放带来的公共空间占用（负外部性），估计社会最优停放密度，并测算高峰时段的
福利损失。

## Keywords / 关键词

`shared bike` · `externality` · `optimal deployment` · `market failure` · `public space occupancy`

共享单车；外部性；最优投放量；市场失灵；公共空间占用

## Key findings / 核心结论

- Peak-hour parking density at the Wudaokou Exit B reached **3.773 bikes/m²**,
  approximately **15.5 times** the estimated socially optimal density.
- The correlation coefficient between parking density and illegal-parking rate
  was **0.932**.
- Estimated welfare loss over a two-hour peak period was about **1,777 CNY**.

Length: 23 pages / 8,204 words (English final draft).

## Repository layout / 文件清单

| Path | Description |
| --- | --- |
| `thesis/thesis_en.docx` | English final thesis — authoritative layout |
| `thesis/thesis_zh.docx` | 中文终稿 — authoritative layout |
| `Thesis.pdf` | 23-page PDF rendition of the English final thesis |
| `thesis/thesis_en.md`, `thesis/thesis_zh.md` | Plain-text renditions for convenient web browsing; equation and table rendering may differ |
| `figures/*.png` | Six figures produced for the paper |
| `data/survey_data.xlsx` | Field survey table (station-exit level) |
| `photos/field_01.jpg` … `field_10.jpg` | Ten field photographs, redacted and EXIF-stripped |
| `photos/README.md` | Photograph provenance and privacy notice |
| `src/crowd_flow.py` | Passenger-flow aggregation example |
| `requirements.txt` | Optional dependencies for re-running the analysis |
| `docs/LICENSE-NOTES.md` | Licence scope and notes on excluded material |

**On the PDF**: `Thesis.pdf` is a 23-page PDF rendition regenerated
from the sanitised English DOCX. Its cover page carries only the author name
`Jason Han`; the original document metadata (author nickname, WPS creator and
precise export timestamps) has been removed. The DOCX files remain the
authoritative versions for layout and citation.

## Data / 数据说明

`data/survey_data.xlsx` contains a single sheet with the columns `Name`, `Time`,
`Area (m²)`, `Bikes`, `Parking Density`, `Illegal Bikes`, `Illegal Rate`,
`Five-minute Crowd Flow` and `Two-hour Crowd Flow`. The `Name` column holds
station-exit labels (for example `Wudaokou B`) and contains no personal names.
All counts were collected by the author on site.

## Reproducing / 复现说明

```bash
python3 -m pip install -r requirements.txt
python3 src/crowd_flow.py
```

`src/crowd_flow.py` expects `data/metro_passengers_20190114.csv`, a third-party
metro passenger-flow dataset that is **not included** in this repository for
size and licensing reasons. It is provided as a method example only. The survey
data in `data/survey_data.xlsx` is self-contained. All six figures in `figures/`
are included as final PNGs, so no regeneration is required to read the paper.

## Photographs / 照片说明

The ten photographs in `photos/` were taken by the author around metro station
exits in Haidian District as field documentation. Recognisable people, licence
plates, street signs and shop signage have been pixelated; the images were
downscaled, renamed to neutral filenames, and stripped of all EXIF / GPS / XMP /
ICC metadata and exact capture timestamps. See `photos/README.md` for the full
notice and the removal-request channel.

## Author

**Jason Han**

## License / 许可

- Thesis text, figures and photographs: **CC BY-NC-SA 4.0** (`LICENSE`).
  Attribution, non-commercial use and share-alike apply — chosen for a course
  paper to prevent commercial reuse while allowing academic sharing.
- Code under `src/`: **MIT** (`src/LICENSE`). Creative Commons licences are not
  appropriate for software, hence the separate code licence.

See `docs/LICENSE-NOTES.md` for scope details.
