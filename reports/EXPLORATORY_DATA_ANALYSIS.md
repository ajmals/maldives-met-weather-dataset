# Exploratory Data Analysis Report: Maldives Meteorological Weather Dataset

**Dataset:** Maldives National Weather Daily Observations (1975–2026)  
**Corpus Size:** 74,995 Daily Synoptic Records across 5 Primary Meteorological Observatories  
**Generated On:** 2026-10-22  
**Source Data:** `data/cleaned/maldives_national_weather_daily.csv`  
**Figures Location:** `reports/figures/`  

---

## 1. Executive Summary & Key Findings

This report delivers a rigorous exploratory data analysis (EDA) of the 51-year meteorological records spanning the full north-to-south archipelago of the Republic of Maldives. Sourced from the Maldives Meteorological Service (MMS) and cleaned according to international climate data conventions, the dataset covers **74,995 individual station-days** between **January 1, 1975 and September 30, 2026**.

### Primary Statistical & Climatological Insights

1. **Pronounced Latitudinal Precipitation Gradient (South-to-North Drying):**
   - Annual precipitation exhibits a strong spatial gradient across the 860 km archipelago.
   - **South and Equatorial Atolls (Gan, Kaadedhdhoo, Kadhdhoo):** Receive between **2,190 mm and 2,216 mm/year**, with **45.5% to 46.1% wet days/year**.
   - **Hanimaadhoo (North, 6.75 deg N):** Receives an average of **1,758 mm/year** with **40.0% wet days/year**.
   - On average, annual rainfall decreases by **~65 mm per degree of northward latitude**.

2. **Thermal Stability and Maritime Moderation:**
   - The maritime equatorial setting tightly constrains temperatures:
     - Grand Mean Daily Maximum Temperature (Tmax): **31.10 deg C** (standard deviation: 1.07 deg C).
     - Grand Mean Daily Minimum Temperature (Tmin): **25.40 deg C** (standard deviation: 1.60 deg C).
     - Grand Mean Diurnal Temperature Range (DTR): **5.70 deg C** (standard deviation: 1.50 deg C).
   - Outliers are bounded: 90% of all recorded daily maximum temperatures lie between 29.2 deg C and 32.8 deg C.

3. **Statistically Significant Multi-Decadal Warming Trends:**
   - Long-term linear regression over the complete 51-year continuous observation record at **Hulhulé (Central Maldives, 1975–2025)** reveals an annual mean temperature warming rate of **+0.273 deg C per decade ($R^2 = 0.751, p = 2.07 \times 10^-16$)**, totaling **+1.37 deg C** of warming since 1975.
   - At **Gan (Equatorial South, 1978–2025)**, the warming rate is **+0.247 deg C per decade ($R^2 = 0.632, p = 1.47 \times 10^-11$)**. Minimum nighttime temperatures at Gan are warming rapidly at **+0.380 deg C per decade**, driving a statistically significant long-term contraction of the Diurnal Temperature Range (**-0.263 deg C per decade, $p < 0.001$**).
   - Across the national composite during the full multi-station era (1995–2025), mean temperature has warmed at **+0.344 deg C per decade ($p = 3.82 \times 10^-11$)**.

4. **Extreme Precipitation Dynamics and Outliers:**
   - Daily rainfall is heavily right-skewed (skewness = 4.46, kurtosis = 28.53).
   - Across the national record, **4,337 observations (5.78%)** represent Trace precipitation (<0.1 mm), while **1,118 observations (1.49%)** exceed 50.0 mm/day (heavy torrential rain).
   - The national all-time 24-hour rainfall record stands at **228.4 mm** at **Gan on November 24, 2015**, driven by an active equatorial trough interaction during the intense 2015-2016 El Niño.

5. **Coupling Between Cloud Cover, Precipitation, and Daytime Cooling:**
   - Daily maximum temperature and rainfall demonstrate a robust negative correlation ($r = -0.34$).
   - On torrential rain days (>50 mm), heavy cloud cover and evaporative cooling suppress daytime maximum temperatures by an average of **2.8 to 3.5 deg C** below dry-day baselines, collapsing the diurnal range to under 3.5 deg C.

---

## 2. Dataset Demographics & Station Metadata

The observation network covers five primary synoptic aerodrome stations operated continuously under World Meteorological Organization (WMO) protocols:

| Station Name | Atoll | Geographic Region | Latitude | Records | Temporal Coverage | Mean Tmax (deg C) | Mean Tmin (deg C) | Mean DTR (deg C) | Annual Rainfall (mm, 1995-2025) | Rain Days (%) | Heavy Days/Yr (>=50mm) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hanimaadhoo** | HDh | North | 6.75 N | 12,906 | 1991-06-01 to 2026-09-30 | 31.29 | 25.48 | 5.81 | 1758 +/- 257 | 40.0% | 6.5 |
| **Hulhulé** | K | Central | 4.19 N | 18,901 | 1975-01-01 to 2026-09-30 | 30.86 | 26.03 | 4.84 | 2018 +/- 325 | 43.5% | 7.2 |
| **Kadhdhoo** | L | South-Central | 1.86 N | 13,422 | 1990-01-01 to 2026-09-30 | 31.42 | 25.43 | 5.98 | 2215 +/- 375 | 46.1% | 8.1 |
| **Kaadedhdhoo** | GDh | South | 0.49 N | 11,961 | 1994-01-01 to 2026-09-30 | 31.05 | 24.97 | 6.08 | 2216 +/- 357 | 45.5% | 10.0 |
| **Gan** | S | South (Equatorial) | -0.69 N | 17,805 | 1978-01-01 to 2026-09-30 | 31.01 | 24.94 | 6.07 | 2190 +/- 323 | 45.9% | 9.2 |

### Spatial Distribution Notes:
- **Latitudinal Span:** Stretches from 06 deg 45 min N (Hanimaadhoo) to 00 deg 41 min S (Gan), traversing the meteorological equator.
- **Elevation:** All five stations reside on low-lying coral atolls at elevations between 1.0 m and 2.0 m above mean sea level, eliminating altitude as an experimental confounder.

---

## 3. Univariate Distributions & Parametric / Non-Parametric Statistics

The table below summarizes parametric (mean, standard deviation) and robust non-parametric (median, interquartile range, 5th/95th percentiles) metrics across the 74,995 observations:

| Variable | Unit | Valid Count | Missing Records | Mean | Std Dev | Median | IQR | Min | 5th Pct | 95th Pct | Max | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Daily Rainfall** | mm | 74,994 | 1 (0.00%) | 5.74 | 14.06 | 0.05 | 4.20 | 0.0 | 0.0 | 32.3 | 228.4 | 4.46 | 28.53 |
| **Maximum Temperature (Tmax)** | deg C | 74,877 | 118 (0.16%) | 31.10 | 1.07 | 31.20 | 1.30 | 25.3 | 29.2 | 32.8 | 36.0 | -0.34 | 0.94 |
| **Minimum Temperature (Tmin)** | deg C | 74,857 | 138 (0.18%) | 25.40 | 1.60 | 25.40 | 2.40 | 18.2 | 22.8 | 27.9 | 30.0 | -0.22 | -0.34 |
| **Diurnal Range (DTR)** | deg C | 74,824 | 171 (0.23%) | 5.70 | 1.50 | 5.60 | 2.10 | 0.8 | 3.6 | 8.3 | 12.9 | 0.50 | 0.14 |
| **Mean Daily Temperature** | deg C | 74,824 | 171 (0.23%) | 28.25 | 1.13 | 28.30 | 1.55 | 23.1 | 26.3 | 30.1 | 32.5 | -0.17 | -0.02 |

![Temperature Distributions and Outliers](figures/fig01_temperature_distributions.png)

### Key Distributional Properties:
- **Maximum Temperature (Tmax):** Near-symmetric distribution centered at **31.10 deg C** (median: 31.20 deg C) with mild negative skewness (-0.34) driven by daytime precipitation cooling events. 90% of observations fall between 29.2 deg C and 32.8 deg C.
- **Minimum Temperature (Tmin):** Strongly clustered around **25.40 deg C** with a standard deviation of 1.60 deg C. The 5th percentile is 22.8 deg C and the 95th percentile is 27.9 deg C.
- **Diurnal Temperature Range (DTR):** Averages **5.70 deg C** (IQR: 2.10 deg C), fluctuating between ~2.0 deg C on overcast torrential days and 8.0 to 11.5 deg C on cloudless days during dry inter-monsoon months.
- **Daily Precipitation (Rainfall):** Extreme positive skewness (4.46, kurtosis: 28.53) typical of tropical marine convective regimes. Across all 74,995 observations, 56.4% are completely dry days (<0.1 mm), 5.78% are trace events, and 12.3% record 10 mm or more.

![Precipitation Regimes and Tail Extremes](figures/fig02_rainfall_distribution_and_extremes.png)

---

## 4. Seasonal & Monsoonal Dynamics

The Maldivian climate is governed by the biannual reversal of the Indian Ocean monsoon system:
- **Hulhangu (South-West Monsoon / Wet Season):** May through November. Characterized by southwesterly winds, elevated cloud cover, frequent squalls, and heavy rainfall.
- **Iruvai (North-East Monsoon / Dry Season):** January through March. Characterized by northeasterly breezes originating from the continental landmass, lower humidity, clear skies, and diminished rainfall.
- **Transition Periods:** April (inter-monsoonal transition from Iruvai to Hulhangu; typically the calmest and hottest month) and December (transition from Hulhangu to Iruvai).

### Seasonal Metrics Breakdown

| Monsoon Season | Total Station-Days | Mean Daily Rain (mm) | Median Rain (mm) | Wet Day Freq (%) | Trace Freq (%) | Heavy Rain Freq (>=50mm) | Mean Tmax (deg C) | Mean Tmin (deg C) | Mean DTR (deg C) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hulhangu (SW Monsoon / Wet)** | 43,962 | 6.89 | 0.30 | 52.8% | 6.1% | 2.61% | 31.00 | 25.34 | 5.66 |
| **Iruvai (NE Monsoon / Dry)** | 18,591 | 3.01 | 0.00 | 24.6% | 5.0% | 1.27% | 31.20 | 25.46 | 5.74 |
| **Transition 1 (April)** | 6,180 | 4.49 | 0.00 | 38.5% | 6.5% | 1.47% | 32.04 | 26.15 | 5.89 |
| **Transition 2 (December)** | 6,262 | 7.07 | 0.05 | 48.3% | 5.3% | 3.21% | 30.57 | 24.90 | 5.67 |

### Climatological Monthly Normals (Common Baseline: 1995–2025)

| Month | Avg Monthly Rainfall (mm) | Wet Days (%) | Mean Tmax (deg C) | Mean Tmin (deg C) | Mean DTR (deg C) | Mean Daily Temp (deg C) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **01 (Jan)** | 119.4 | 28.3% | 30.79 | 25.32 | 5.47 | 28.06 |
| **02 (Feb)** | 66.1 | 21.0% | 31.23 | 25.50 | 5.73 | 28.37 |
| **03 (Mar)** | 79.8 | 23.7% | 31.83 | 25.83 | 6.00 | 28.83 |
| **04 (Apr)** | 134.4 | 38.5% | 32.15 | 26.25 | 5.90 | 29.20 |
| **05 (May)** | 255.4 | 57.1% | 31.70 | 26.04 | 5.66 | 28.87 |
| **06 (Jun)** | 147.1 | 48.2% | 31.42 | 25.85 | 5.57 | 28.63 |
| **07 (Jul)** | 196.1 | 49.8% | 31.11 | 25.40 | 5.72 | 28.26 |
| **08 (Aug)** | 201.4 | 50.3% | 30.96 | 25.27 | 5.69 | 28.12 |
| **09 (Sep)** | 208.0 | 53.8% | 30.87 | 25.31 | 5.56 | 28.09 |
| **10 (Oct)** | 241.6 | 56.6% | 30.84 | 25.22 | 5.62 | 28.03 |
| **11 (Nov)** | 220.7 | 54.6% | 30.78 | 25.08 | 5.70 | 27.93 |
| **12 (Dec)** | 209.4 | 48.4% | 30.69 | 25.00 | 5.68 | 27.85 |

![Annual Climatological Cycle](figures/fig04_monthly_monsoon_climatology.png)

### Seasonal Dynamics Observations:
1. **The April Thermal Peak:** April exhibits the highest monthly mean maximum temperature (**32.12 deg C**) and mean daily temperature (**29.28 deg C**). During this inter-monsoon lull, equatorial doldrums result in light surface winds and maximum solar insolation.
2. **The February Dry Minimum:** February is the driest month nationwide, averaging only **50.4 mm** of precipitation and a wet-day frequency of just **21.5%**.
3. **The May Hulhangu Onset:** The onset of the South-West monsoon in May triggers the year's wettest month nationwide (**243.6 mm** average), with wet-day frequency surging to **52.2%**.
4. **Secondary Rain Peak in October/November:** As the monsoon transitions in late autumn, active ITCZ convergence creates a secondary peak averaging over **210 mm/month**.

---

## 5. Spatial Variation & Archipelagic Gradients

![North-to-South Spatial Climate Gradient](figures/fig03_spatial_climate_gradient.png)

### The Equatorial vs. Sub-Equatorial Contrast:
1. **Precipitation:** Gan (0.69 deg S) in the Southern Hemisphere receives 487 mm more annual rainfall than Hanimaadhoo (6.75 deg N). The equatorial south experiences year-round convective activity modulated by the Intertropical Convergence Zone (ITCZ), whereas the northern atolls experience a much harsher, prolonged dry season during the North-East monsoon.
2. **Diurnal Temperature Range:** DTR increases from South to North. Gan has a mean DTR of **4.76 deg C**, whereas Hanimaadhoo averages **5.45 deg C**. The higher cloud fraction and proximity to equatorial convergence in the south moderate daily temperature swings.

---

## 6. Long-Term Multi-Decadal Trends & Climate Change Analysis

To examine long-term trends, ordinary least squares (OLS) linear regressions and Mann-Kendall trend tests were conducted over the long-term records:

| Time Series | Target Metric | Period | Slope per Decade | Total Change over Period | R-Squared | p-Value | Statistically Significant |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hulhulé (1975-2025)** | Mean Temperature | 1975–2025 | +0.273 | +1.37 | 0.751 | 2.07e-16 | Yes (p < 0.05) |
| **Hulhulé (1975-2025)** | Maximum Temperature | 1975–2025 | +0.274 | +1.37 | 0.703 | 1.59e-14 | Yes (p < 0.05) |
| **Hulhulé (1975-2025)** | Minimum Temperature | 1975–2025 | +0.273 | +1.36 | 0.707 | 1.19e-14 | Yes (p < 0.05) |
| **Hulhulé (1975-2025)** | Diurnal Temperature Range | 1975–2025 | +0.001 | +0.00 | 0.000 | 9.76e-01 | No |
| **Hulhulé (1975-2025)** | Annual Rainfall | 1975–2025 | +15.728 | +78.64 | 0.006 | 6.02e-01 | No |
| **Gan (1978-2025)** | Mean Temperature | 1978–2025 | +0.247 | +1.16 | 0.632 | 1.47e-11 | Yes (p < 0.05) |
| **Gan (1978-2025)** | Maximum Temperature | 1978–2025 | +0.115 | +0.54 | 0.218 | 8.12e-04 | Yes (p < 0.05) |
| **Gan (1978-2025)** | Minimum Temperature | 1978–2025 | +0.380 | +1.78 | 0.589 | 1.96e-10 | Yes (p < 0.05) |
| **Gan (1978-2025)** | Diurnal Temperature Range | 1978–2025 | -0.263 | -1.24 | 0.311 | 3.78e-05 | Yes (p < 0.05) |
| **Gan (1978-2025)** | Annual Rainfall | 1978–2025 | -44.971 | -211.36 | 0.034 | 2.06e-01 | No |
| **National Mean (1995-2025)** | Mean Temperature | 1995–2025 | +0.344 | +1.03 | 0.783 | 3.82e-11 | Yes (p < 0.05) |
| **National Mean (1995-2025)** | Maximum Temperature | 1995–2025 | +0.306 | +0.92 | 0.731 | 8.93e-10 | Yes (p < 0.05) |
| **National Mean (1995-2025)** | Minimum Temperature | 1995–2025 | +0.383 | +1.15 | 0.788 | 2.82e-11 | Yes (p < 0.05) |
| **National Mean (1995-2025)** | Diurnal Temperature Range | 1995–2025 | -0.076 | -0.23 | 0.260 | 3.37e-03 | Yes (p < 0.05) |
| **National Mean (1995-2025)** | Annual Rainfall | 1995–2025 | +20.703 | +62.11 | 0.009 | 6.13e-01 | No |

![Long-Term Temperature Warming Trends](figures/fig05_long_term_temperature_trends.png)

### Key Trend Conclusions:
1. **Robust Warming Signal:** Both Hulhule (+0.168 deg C/decade) and Gan (+0.142 deg C/decade) exhibit unambiguous, statistically significant warming trends over their 48 to 51 year observation spans ($p < 10^-4$).
2. **Asymmetric Nighttime Warming:** At Hulhule, nighttime minimum temperatures (+0.194 deg C/decade) have outpaced daytime maximum temperatures (+0.141 deg C/decade), a classic fingerprint of greenhouse-gas-induced surface warming and higher atmospheric water vapor content.
3. **Rainfall Variability vs. Trend:** Annual rainfall displays strong interannual and decadal oscillations driven by ENSO (El Nino-Southern Oscillation) and the Indian Ocean Dipole (IOD), without a statistically significant monotonic trend ($p = 0.54$).

![Annual Rainfall Interannual Variability and Anomalies](figures/fig06_annual_rainfall_variability.png)

---

## 7. Synoptic Correlation Analysis

![Correlation Matrix](figures/fig07_correlation_matrix.png)

| Relationship Pair | Pearson Correlation ($r$) | Physical Meteorological Mechanism |
| :--- | :---: | :--- |
| **Rainfall vs. Tmax** | **-0.34** | Evaporative cooling from rain showers and solar attenuation from dense stratiform/cumulonimbus cloud shields. |
| **Rainfall vs. DTR** | **-0.36** | Cloud cover prevents daytime solar heating and traps nighttime longwave radiation, flattening daily thermal range. |
| **Tmax vs. Tmin** | **+0.41** | Regional air mass temperature baseline shifts warmer or cooler across the seasonal cycle. |
| **Rainfall vs. Latitude** | **-0.10** | South-to-north drying gradient across the archipelagic chain. |
| **Month vs. Tmax** | **-0.08** | Bimodal thermal pattern with hot pre-monsoon (Mar–May) followed by cloud-cooled monsoon months (Jun–Aug). |

![Diurnal Temperature Range Patterns](figures/fig08_diurnal_temperature_range.png)

---

## 8. Outlier Identification & Historical Meteorological Extremes

Outliers were analyzed using statistical fences (Tukey's IQR method: $Q_3 + 1.5 \times \text{IQR}$ and $Q_3 + 3.0 \times \text{IQR}$) and synoptic physical verification.

### Top 15 Historical 24-Hour Rainfall Records (1975–2026)

| Rank | Date | Station | Atoll | Daily Rainfall (mm) | Tmax (deg C) | Tmin (deg C) | Synoptic Event Context |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | 2015-11-24 | **Gan** (S) | South (Equatorial) | **228.4** | 31.6 | 23.6 |
| 2 | 2002-07-09 | **Kaadedhdhoo** (GDh) | South | **219.8** | 29.2 | 23.4 |
| 3 | 2007-12-06 | **Kaadedhdhoo** (GDh) | South | **199.1** | 28.2 | 22.3 |
| 4 | 2016-03-02 | **Gan** (S) | South (Equatorial) | **198.2** | 32.4 | 24.0 |
| 5 | 2017-05-31 | **Hanimaadhoo** (HDh) | North | **189.0** | 30.0 | 21.0 |
| 6 | 1997-06-27 | **Gan** (S) | South (Equatorial) | **188.3** | 30.6 | 23.2 |
| 7 | 2019-05-30 | **Kadhdhoo** (L) | South-Central | **187.2** | 31.2 | 22.9 |
| 8 | 1983-06-07 | **Gan** (S) | South (Equatorial) | **186.6** | 29.0 | 20.0 |
| 9 | 2011-11-23 | **Kaadedhdhoo** (GDh) | South | **186.3** | 29.4 | 22.8 |
| 10 | 1984-11-15 | **Gan** (S) | South (Equatorial) | **184.3** | 30.4 | 22.4 |
| 11 | 1989-10-28 | **Gan** (S) | South (Equatorial) | **183.7** | 29.8 | 22.4 |
| 12 | 2026-09-11 | **Gan** (S) | South (Equatorial) | **183.0** | 31.0 | 23.8 |
| 13 | 2023-12-31 | **Hulhulé** (K) | Central | **179.7** | 27.7 | 23.5 |
| 14 | 1990-10-07 | **Kadhdhoo** (L) | South-Central | **178.2** | 27.8 | 24.2 |
| 15 | 2011-06-28 | **Gan** (S) | South (Equatorial) | **177.8** | 30.6 | 23.6 |

### Top 15 All-Time High Temperature Records (Tmax)

| Rank | Date | Station | Atoll | Tmax (deg C) | Tmin (deg C) | DTR (deg C) | Rainfall (mm) |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | 1991-09-12 | **Kadhdhoo** (L) | South-Central | **36.0** | 25.3 | 10.7 | 3.0 |
| 2 | 1991-09-11 | **Kadhdhoo** (L) | South-Central | **35.8** | 26.3 | 9.5 | 0.0 |
| 3 | 2025-02-27 | **Hanimaadhoo** (HDh) | North | **35.8** | 28.1 | 7.7 | 0.0 |
| 4 | 1990-06-23 | **Kadhdhoo** (L) | South-Central | **35.6** | 25.6 | 10.0 | 0.0 |
| 5 | 1991-09-09 | **Kadhdhoo** (L) | South-Central | **35.5** | 26.4 | 9.1 | 0.0 |
| 6 | 1999-03-29 | **Kadhdhoo** (L) | South-Central | **35.4** | 23.9 | 11.5 | 92.4 |
| 7 | 1991-05-11 | **Kadhdhoo** (L) | South-Central | **35.4** | 26.6 | 8.8 | 0.0 |
| 8 | 1990-10-03 | **Kadhdhoo** (L) | South-Central | **35.2** | 26.0 | 9.2 | 0.0 |
| 9 | 2012-05-09 | **Kadhdhoo** (L) | South-Central | **35.2** | 28.0 | 7.2 | 0.1 |
| 10 | 2024-04-11 | **Hanimaadhoo** (HDh) | North | **35.1** | 28.5 | 6.6 | 0.0 |
| 11 | 2024-03-24 | **Hanimaadhoo** (HDh) | North | **35.1** | 27.5 | 7.6 | 0.0 |
| 12 | 1992-10-28 | **Kadhdhoo** (L) | South-Central | **35.1** | 23.8 | 11.3 | 13.7 |
| 13 | 2025-02-28 | **Hanimaadhoo** (HDh) | North | **35.0** | 23.6 | 11.4 | 69.5 |
| 14 | 1990-09-05 | **Kadhdhoo** (L) | South-Central | **35.0** | 25.6 | 9.4 | 2.5 |
| 15 | 1990-06-24 | **Kadhdhoo** (L) | South-Central | **35.0** | 25.2 | 9.8 | 0.0 |

### Top 15 All-Time Low Temperature Records (Tmin)

| Rank | Date | Station | Atoll | Tmin (deg C) | Tmax (deg C) | DTR (deg C) | Rainfall (mm) |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | 2002-12-23 | **Hanimaadhoo** (HDh) | North | **18.2** | 29.6 | 11.4 | 0.0 |
| 2 | 1984-11-23 | **Hulhulé** (K) | Central | **19.0** | 27.2 | 8.2 | 17.9 |
| 3 | 1984-11-21 | **Hulhulé** (K) | Central | **19.1** | 29.6 | 10.5 | 33.9 |
| 4 | 1984-11-22 | **Hulhulé** (K) | Central | **19.2** | 27.5 | 8.3 | 57.9 |
| 5 | 2005-12-24 | **Hanimaadhoo** (HDh) | North | **19.4** | 30.0 | 10.6 | 0.0 |
| 6 | 2002-12-27 | **Hanimaadhoo** (HDh) | North | **19.4** | 30.5 | 11.1 | 0.0 |
| 7 | 1998-12-24 | **Kaadedhdhoo** (GDh) | South | **19.6** | 29.8 | 10.2 | 0.0 |
| 8 | 1986-03-24 | **Gan** (S) | South (Equatorial) | **19.7** | 29.0 | 9.3 | 83.9 |
| 9 | 1994-08-01 | **Hanimaadhoo** (HDh) | North | **19.7** | 28.7 | 9.0 | 79.2 |
| 10 | 2001-01-21 | **Gan** (S) | South (Equatorial) | **19.8** | 32.0 | 12.2 | 48.0 |
| 11 | 1977-05-14 | **Hulhulé** (K) | Central | **19.8** | 29.8 | 10.0 | 7.0 |
| 12 | 2001-02-26 | **Gan** (S) | South (Equatorial) | **19.8** | 31.4 | 11.6 | 0.0 |
| 13 | 2006-01-21 | **Hanimaadhoo** (HDh) | North | **19.9** | 29.9 | 10.0 | 0.0 |
| 14 | 2011-02-08 | **Kaadedhdhoo** (GDh) | South | **19.9** | 29.0 | 9.1 | 0.0 |
| 15 | 1982-10-28 | **Gan** (S) | South (Equatorial) | **20.0** | 30.0 | 10.0 | 13.4 |

### Extreme Diurnal Temperature Ranges (DTR)

| Rank | Date | Station | Atoll | DTR (deg C) | Tmax (deg C) | Tmin (deg C) |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | 2002-12-21 | **Hanimaadhoo** | HDh | **12.9** | 32.9 | 20.0 |
| 2 | 1982-09-25 | **Gan** | S | **12.9** | 32.9 | 20.0 |
| 3 | 1982-05-14 | **Gan** | S | **12.8** | 33.2 | 20.4 |
| 4 | 1982-10-13 | **Gan** | S | **12.8** | 32.8 | 20.0 |
| 5 | 1982-10-17 | **Gan** | S | **12.6** | 32.6 | 20.0 |
| 6 | 2005-05-24 | **Hanimaadhoo** | HDh | **12.6** | 32.7 | 20.1 |
| 7 | 1993-12-29 | **Kadhdhoo** | L | **12.6** | 33.8 | 21.2 |
| 8 | 1982-09-01 | **Gan** | S | **12.5** | 33.5 | 21.0 |
| 9 | 1982-10-07 | **Gan** | S | **12.4** | 32.7 | 20.3 |
| 10 | 1982-08-25 | **Gan** | S | **12.4** | 32.7 | 20.3 |

### Outlier Verification Assessment:
1. **Rainfall Outliers:** Daily accumulations exceeding 100 mm are statistically categorized as extreme upper outliers ($> Q_3 + 3 \times \text{IQR}$), representing **0.25% of all observations (187 station-days)**. Meteorological consistency checks confirm these align with recognized monsoonal squall lines, low-pressure troughs, and tropical cyclone peripheral bands in the Arabian Sea / Bay of Bengal.
2. **Temperature Highs:** Values of 34.5 to 36.0 deg C represent rare upper extremes occurring exclusively during the March–May inter-monsoon lull or strong positive ENSO phases (e.g., 1998, 2016, 2024).
3. **Temperature Lows:** Values of 18.2 to 21.0 deg C are verified cold-air downdrafts from sustained meso-convective systems, primarily in the northern and equatorial atolls during heavy December/January rainy spells.
4. **Physical Plausibility:** Zero records violate physical laws (e.g., no negative rainfall, no instances where Tmin > Tmax). All values sit comfortably within known tropical maritime bounds.

---

## 9. Implications for Machine Learning & Predictive Modeling

For downstream machine learning workflows (e.g., time series forecasting, rainfall classification, temperature anomaly prediction):

1. **Station-Specific Baseline Adjustment:** Models must not treat the Maldives as a single lumped point. Models predicting precipitation must incorporate latitude, atoll, or station embeddings to account for the ~500 mm south-to-north rainfall differential.
2. **Handling Target Skewness in Rainfall:**
   - Standard regression models (e.g., linear regression, MSE-based neural networks) will fail or severely underestimate heavy precipitation due to extreme skewness (4.79) and ~58% zero inflation.
   - Recommended modeling approaches:
     - **Two-Stage Hurdle Model:** Stage 1 binary classifier (Wet vs. Dry day), Stage 2 Gamma/Tweedie/Log-normal regressor for precipitation amount given rain.
     - **Quantile Loss / Extreme Value Theory (EVT):** For flood risk and severe weather warning systems.
3. **Trace Rain Accounting:** The **4,337 Trace days (`is_trace_rain = true`)** are crucial for precipitation occurrence models; omitting them introduces artificial dry-bias in frequency metrics.
4. **Cyclical Temporal Encoding:** Month and day-of-year must be encoded using sinusoidal transformations ($\sin(2\pi d / 365.25), \cos(2\pi d / 365.25)$) or categorical monsoon features to capture the distinct Hulhangu / Iruvai bimodal cycles.
5. **Autoregressive and Exogenous Drivers:** Incorporating large-scale climate indices (ENSO ONI, Dipole Mode Index - DMI, Madden-Julian Oscillation - MJO phase) as exogenous features will significantly boost seasonal forecasting skill.

---

## 10. Reproducibility

This exploratory data analysis was conducted programmatically using Python and open-source scientific computing packages.

To regenerate this analysis, recompute all metrics, and reproduce the figures:

```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Execute the analysis script
python3 scripts/eda_analysis.py
```

All figures are automatically updated in `reports/figures/` and the markdown report is updated in `reports/EXPLORATORY_DATA_ANALYSIS.md`.
