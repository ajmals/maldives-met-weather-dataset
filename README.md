# Maldives Meteorological Weather Dataset (1975 – 2026)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Temporal Coverage](https://img.shields.io/badge/Coverage-1975--2026-brightgreen.svg)]()
[![Stations](https://img.shields.io/badge/Stations-5%20Synoptic%20Offices-orange.svg)]()
[![Total Records](https://img.shields.io/badge/Records-75%2C000%2B%20Daily%20Rows-informational.svg)]()

A comprehensive multi-decadal historical daily weather dataset from the 5 primary meteorological observatories across the Republic of Maldives, sourced from the **Maldives Meteorological Service (MMS)**.

This repository is designed as an open-access resource for climate researchers, meteorologists, data scientists, students, and environmental analysts studying equatorial climate dynamics, Indian Ocean monsoons, El Niño–Southern Oscillation (ENSO), Indian Ocean Dipole (IOD), and long-term climate change impacts in low-lying island states.

---

## Stations & Geographic Coverage

The Maldives stretches ~860 km north-to-south across the equator. The 5 synoptic stations provide full-length geographical coverage of the archipelago:

| Station | Atoll | Region | WMO ID | ICAO | Latitude | Longitude | Active Record Range | Records |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hanimaadhoo** | Haa Dhaalu (HDh.) | North | `43533` | `VRMH` | 06°45' N | 73°10' E | 01-06-1991 to 30-09-2026 | 12,906 |
| **Hulhulé** *(Male' Airport)* | Kaafu (K.) | Central | `43555` | `VRMM` | 04°11' N | 73°32' E | 01-01-1975 to 30-09-2026 | 18,901 |
| **Kadhdhoo** | Laamu (L.) | South-Central | `43577` | `VRMK` | 01°51' N | 73°31' E | 01-01-1990 to 30-09-2026 | 13,422 |
| **Kaadedhdhoo** | Gaafu Dhaalu (GDh.) | South | `43588` | `VRMT` | 00°29' N | 72°59' E | 01-01-1994 to 30-09-2026 | 11,961 |
| **Gan** *(Addu City)* | Seenu (S.) | Far South *(South of Equator)* | `43599` | `VRMG` | 00°41' S | 73°09' E | 01-01-1978 to 30-09-2026 | 17,805 |

*Note: While filenames specify `1_Jan_1975_30_Sep_2026`, individual station data starts on the date that each meteorological station officially commenced synoptic observation records.*

---

## Repository Structure

```text
maldives-met-weather-dataset/
├── .gitignore
├── README.md
├── requirements.txt
├── scripts/
│   ├── clean_data.py               # Reproducible cleaning pipeline (raw -> cleaned)
│   └── eda_analysis.py             # Comprehensive EDA script & figure generator
├── reports/
│   ├── EXPLORATORY_DATA_ANALYSIS.md # 51-year comprehensive Exploratory Data Analysis report
│   └── figures/                    # High-resolution diagnostic figures and charts
└── data/
    ├── cleaned/                    # Machine-readable, standardized (UTF-8, ISO dates, no headers)
    │   ├── DATA_CLEANING_REPORT.md # Comprehensive audit & cleaning report (before vs. after metrics)
    │   ├── gan.csv
    │   ├── hanimaadhoo.csv
    │   ├── hulhule.csv
    │   ├── kaadedhdhoo.csv
    │   ├── kadhdhoo.csv
    │   └── maldives_national_weather_daily.csv   # Unified master dataset (all stations)
    └── raw/                        # Original source files as received from MMS
        ├── Gan_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv
        ├── Hanimaadhoo_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv
        ├── Hulhule_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv
        ├── Kaadedhdhoo_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv
        └── Kadhdhoo_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv
```

---

## Data Analysis & Transformation Reports

- **Exploratory Data Analysis Report:** For complete statistical distributions, monsoonal cycles, multi-decadal warming trends (+0.27 deg C/decade at Hulhulé), spatial drying gradients, and historical record deluges, see the [Exploratory Data Analysis Report](reports/EXPLORATORY_DATA_ANALYSIS.md).
- **Data Cleaning Report:** For before-and-after audit statistics, concrete row examples, and sanitization rules, see the [Data Cleaning Report](data/cleaned/DATA_CLEANING_REPORT.md).

### Cleaned Datasets (`data/cleaned/`)
The files in `data/cleaned/` are 100% machine-readable without needing `skiprows` or complex parsing:
- **Clean header row on line 1** (no `#` comment lines)
- **Standardized dates**: ISO-8601 (`YYYY-MM-DD`)
- **Missing values**: Standard blank/empty fields `,` (auto-interpreted as `NaN` / `NULL` in SQL, Pandas, R, Polars, DuckDB)
- **Trace rainfall**: `is_trace_rain` flag (`true`/`false`) + `rainfall_mm` set to numeric `0.05` mm (meteorological midpoint for `< 0.1` mm)

#### 1. Per-Station Files (`gan.csv`, `hulhule.csv`, etc.)
| Column Name | Data Type | Units / Values | Description |
| :--- | :---: | :---: | :--- |
| `date` | Date (`YYYY-MM-DD`) | ISO-8601 | Observation date |
| `rainfall_mm` | Float | `mm` | 24-hr accumulated precipitation (numeric; empty if missing, `0.05` if Trace) |
| `is_trace_rain` | Boolean | `true` / `false` | Indicates if rainfall was trace amount (< 0.1 mm) |
| `temp_max_c` | Float | `°C` | Maximum 24-hr temperature (empty if missing) |
| `temp_min_c` | Float | `°C` | Minimum 24-hr temperature (empty if missing) |

#### 2. Unified Master Dataset (`maldives_national_weather_daily.csv`)
Combines all 5 stations (74,995 total rows) into a single tidy table sorted by date:
`date`, `station_id`, `station_name`, `atoll`, `region`, `wmo_id`, `latitude`, `longitude`, `rainfall_mm`, `is_trace_rain`, `temp_max_c`, `temp_min_c`.

---

### Raw Datasets (`data/raw/`)
The original raw files from Maldives Meteorological Service contain 4 metadata comment lines prefixed with `#`, a blank line, and `DD-MM-YYYY` dates with `TR` for Trace rain and `-`/`N` for missing data.

---

## Quick Start / How to Use

### Read Clean Data Directly (Python / Pandas)
No custom parsing needed! Standard one-liner:

```python
import pandas as pd

# 1. Load an individual station
df_hulhule = pd.read_csv('data/cleaned/hulhule.csv', parse_dates=['date'])
print(df_hulhule.head())

# 2. Or load the unified national dataset
df_national = pd.read_csv('data/cleaned/maldives_national_weather_daily.csv', parse_dates=['date'])
print(df_national.info())
```

### Reproduce Cleaning Pipeline
You can re-run the end-to-end cleaning pipeline anytime using the included zero-dependency Python script:

```bash
python3 scripts/clean_data.py
```

### R Example (Reading Cleaned Data)

```r
library(readr)
library(dplyr)

# Load clean station data
df_hulhule <- read_csv("data/cleaned/hulhule.csv")
glimpse(df_hulhule)

# Load unified national dataset
df_national <- read_csv("data/cleaned/maldives_national_weather_daily.csv")
glimpse(df_national)
```

---

## Meteorological & Climate Context of the Maldives

The Maldives features a tropical monsoon climate characterized by two distinct seasons and two transitional periods:

1. **Southwest Monsoon (*Hulhangu*, Wet Season)**: Mid-May through November. Marked by increased cloud cover, convective rainfall, and gusty winds.
2. **Northeast Monsoon (*Iruvai*, Dry Season)**: January through March. Generally sunny, calm, and dry.
3. **Inter-monsoon Transition Periods**: April (onset of Southwest monsoon) and December (onset of Northeast monsoon).

- **Rainfall Gradient**: Annual precipitation systematically increases from north to south. Northern atolls receive ~1,779 mm/year on average, Central atolls ~1,966 mm/year, and Southern atolls ~2,218 mm/year.
- **Temperature**: Year-round mean daily temperatures range between 25°C and 32°C, moderated by surrounding ocean surface temperatures.

---

## Data Source & Acquisition

Official meteorological measurements and data are maintained by:
- **Authority**: [Maldives Meteorological Service (MMS)](https://www.meteorology.gov.mv/)
- **Ministry**: Ministry of Climate Change, Environment and Energy, Republic of Maldives
- **Official Climate Data Portal**: [https://www.meteorology.gov.mv/climate-data](https://www.meteorology.gov.mv/climate-data)

MMS provides climate data as a public service for scientific, educational, and developmental research. If your project requires additional elements (e.g., hourly wind speed/direction, relative humidity, atmospheric pressure, sunshine hours), submit a request directly via the [MMS Climate Data Request portal](https://www.meteorology.gov.mv/climate-data).

---

## Citation

If you use this dataset in your research, academic paper, blog post, or project, please cite:

```bibtex
@misc{maldives_weather_dataset_met,
  title        = {Maldives Meteorological Weather Dataset: 1975--2026 Daily Synoptic Observations},
  author       = {Maldives Meteorological Service and Contributors},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/ajmals/maldives-met-weather-dataset}},
  note         = {Sourced from Maldives Meteorological Service (https://www.meteorology.gov.mv/climate-data)}
}
```

---

## License & Disclaimer

- **Raw Data Attribution**: The meteorological observation data originates from the [Maldives Meteorological Service (MMS)](https://www.meteorology.gov.mv/).
- **Repository Content**: Documentation, loader scripts, and organized repository structure are shared under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) License.
- **Disclaimer**: This dataset is provided "as is" for informational and research purposes. Users should perform their own data validation and quality control checks for specific research applications.
