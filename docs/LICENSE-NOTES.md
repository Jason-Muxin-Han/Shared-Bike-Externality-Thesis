# Licence scope and repository notes

## Dual licence

| Material | Licence | File |
| --- | --- | --- |
| Thesis text (`thesis/`), figures (`figures/`), photographs (`photos/`) | CC BY-NC-SA 4.0 | `LICENSE` |
| Analysis code (`src/`) | MIT | `src/LICENSE` |

Creative Commons licences are designed for creative works and are explicitly
not recommended for software, so `src/` carries its own MIT licence. GitHub's
automatic licence detection reads the root `LICENSE`; the code licence is
documented here and in `README.md`.

CC BY-NC-SA 4.0 permits sharing and adaptation with attribution, prohibits
commercial reuse, and requires derivative works to use the same licence.

## About the published files

- The DOCX files are the authoritative, fully typeset versions. The Markdown
  files are convenience renditions generated for web browsing; equations,
  tables and pagination may not be preserved exactly.
- `data/survey_data.xlsx` holds station-exit level field counts. Its `Name`
  column contains station-exit labels (for example `Wudaokou B`), not personal
  names.
- The figures in `figures/` were produced by the author from the survey data.
- The photographs in `photos/` have been redacted and stripped of metadata;
  see `photos/README.md`.

## Material deliberately not included

- Drafts, intermediate working documents, screenshots and scratch notebooks.
- The third-party metro passenger-flow CSV referenced by `src/crowd_flow.py`
  (not distributed for size and licensing reasons).
- The original WPS-exported PDF, whose cover page carried personal identifying
  information. A regenerated, desensitised PDF may be added later.
- Temporary processing scripts used locally to prepare the published copies.

## Third-party content

The paper cites publicly available sources (government statistics, news
reports, industry reports and an open dataset) with attribution in the
references. Shared-bike brand marks, shop signage and other third-party marks
appearing incidentally in the photographs remain the property of their
respective owners; no endorsement is implied.
