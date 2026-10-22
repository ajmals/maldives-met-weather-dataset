#!/usr/bin/env python3
"""
scripts/clean_data.py
---------------------
Processes raw MMS meteorological CSV files from data/raw/ into clean,
machine-readable CSV files in data/cleaned/.

Output:
  - data/cleaned/gan.csv
  - data/cleaned/hanimaadhoo.csv
  - data/cleaned/hulhule.csv
  - data/cleaned/kaadedhdhoo.csv
  - data/cleaned/kadhdhoo.csv
  - data/cleaned/maldives_national_weather_daily.csv (unified master file)

Features:
  - Removes metadata comment headers
  - Standardizes dates to ISO-8601 (YYYY-MM-DD)
  - Replaces missing placeholders ('-', 'N') with empty null fields
  - Handles Trace precipitation ('TR') by setting is_trace_rain=true and rainfall_mm=0.05
  - Adds geographical and station identifiers (WMO ID, coordinates, atoll)
"""

import os
import csv
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
CLEANED_DIR = os.path.join(BASE_DIR, 'data', 'cleaned')

STATIONS = {
    'Gan': {
        'id': 'gan',
        'name': 'Gan',
        'atoll_prefix': 'S.',
        'atoll_name': 'Seenu (Addu)',
        'region': 'South (Equatorial)',
        'wmo_id': '43599',
        'icao': 'VRMG',
        'latitude': -0.69,
        'longitude': 73.15,
        'filename': 'Gan_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv',
        'out_filename': 'gan.csv'
    },
    'Hanimaadhoo': {
        'id': 'hanimaadhoo',
        'name': 'Hanimaadhoo',
        'atoll_prefix': 'HDh.',
        'atoll_name': 'Haa Dhaalu',
        'region': 'North',
        'wmo_id': '43533',
        'icao': 'VRMH',
        'latitude': 6.75,
        'longitude': 73.17,
        'filename': 'Hanimaadhoo_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv',
        'out_filename': 'hanimaadhoo.csv'
    },
    'Hulhule': {
        'id': 'hulhule',
        'name': 'Hulhulé',
        'atoll_prefix': 'K.',
        'atoll_name': 'Kaafu',
        'region': 'Central',
        'wmo_id': '43555',
        'icao': 'VRMM',
        'latitude': 4.19,
        'longitude': 73.53,
        'filename': 'Hulhule_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv',
        'out_filename': 'hulhule.csv'
    },
    'Kaadedhdhoo': {
        'id': 'kaadedhdhoo',
        'name': 'Kaadedhdhoo',
        'atoll_prefix': 'GDh.',
        'atoll_name': 'Gaafu Dhaalu',
        'region': 'South',
        'wmo_id': '43588',
        'icao': 'VRMT',
        'latitude': 0.49,
        'longitude': 73.00,
        'filename': 'Kaadedhdhoo_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv',
        'out_filename': 'kaadedhdhoo.csv'
    },
    'Kadhdhoo': {
        'id': 'kadhdhoo',
        'name': 'Kadhdhoo',
        'atoll_prefix': 'L.',
        'atoll_name': 'Laamu',
        'region': 'South-Central',
        'wmo_id': '43577',
        'icao': 'VRMK',
        'latitude': 1.86,
        'longitude': 73.52,
        'filename': 'Kadhdhoo_1_Jan_1975_30_Sep_2026_daily_Multi_Elements.csv',
        'out_filename': 'kadhdhoo.csv'
    }
}

STATION_COLUMNS = [
    'date',
    'rainfall_mm',
    'is_trace_rain',
    'temp_max_c',
    'temp_min_c'
]

UNIFIED_COLUMNS = [
    'date',
    'station_id',
    'station_name',
    'atoll',
    'region',
    'wmo_id',
    'latitude',
    'longitude',
    'rainfall_mm',
    'is_trace_rain',
    'temp_max_c',
    'temp_min_c'
]


def clean_row(row):
    """
    Parses and sanitizes a single raw record.
    Returns: (iso_date, rainfall_mm, is_trace_rain, temp_max_c, temp_min_c)
    """
    raw_date, raw_rain, raw_tmax, raw_tmin = [x.strip() for x in row]

    # Date conversion: DD-MM-YYYY -> YYYY-MM-DD
    dt = datetime.strptime(raw_date, '%d-%m-%Y')
    iso_date = dt.strftime('%Y-%m-%d')

    # Rainfall sanitation
    if raw_rain == 'TR':
        rainfall_val = '0.05'
        is_trace = 'true'
    elif raw_rain in ('-', 'N', ''):
        rainfall_val = ''
        is_trace = 'false'
    else:
        rainfall_val = f"{float(raw_rain):.1f}"
        is_trace = 'false'

    # Temperature max sanitation
    if raw_tmax in ('-', 'N', ''):
        tmax_val = ''
    else:
        tmax_val = f"{float(raw_tmax):.1f}"

    # Temperature min sanitation
    if raw_tmin in ('-', 'N', ''):
        tmin_val = ''
    else:
        tmin_val = f"{float(raw_tmin):.1f}"

    return iso_date, rainfall_val, is_trace, tmax_val, tmin_val


def main():
    os.makedirs(CLEANED_DIR, exist_ok=True)
    unified_records = []
    total_processed = 0

    print("Cleaning Maldives Meteorological Service raw datasets...")

    for key, meta in STATIONS.items():
        raw_path = os.path.join(RAW_DIR, meta['filename'])
        out_path = os.path.join(CLEANED_DIR, meta['out_filename'])

        if not os.path.exists(raw_path):
            print(f"Warning: Missing {raw_path}")
            continue

        with open(raw_path, 'r', encoding='utf-8', errors='ignore') as fp:
            lines = fp.readlines()

        # Find header line with 'Date,'
        header_idx = None
        for i, line in enumerate(lines[:10]):
            if 'Date,' in line:
                header_idx = i
                break

        if header_idx is None:
            raise ValueError(f"Could not locate data header in {raw_path}")

        data_rows = [l.strip() for l in lines[header_idx + 1:] if l.strip()]

        station_records = []
        for line in data_rows:
            parts = line.split(',')
            if len(parts) != 4:
                continue
            iso_date, rain, is_trace, tmax, tmin = clean_row(parts)

            # Per-station record
            station_records.append([iso_date, rain, is_trace, tmax, tmin])

            # Unified record
            unified_records.append([
                iso_date,
                meta['id'],
                meta['name'],
                meta['atoll_prefix'].rstrip('.'),
                meta['region'],
                meta['wmo_id'],
                f"{meta['latitude']:.2f}",
                f"{meta['longitude']:.2f}",
                rain,
                is_trace,
                tmax,
                tmin
            ])

        # Write clean station file
        with open(out_path, 'w', newline='', encoding='utf-8') as out_f:
            writer = csv.writer(out_f)
            writer.writerow(STATION_COLUMNS)
            writer.writerows(station_records)

        count = len(station_records)
        total_processed += count
        date_start = station_records[0][0]
        date_end = station_records[-1][0]
        print(f"  * {meta['name']:<14} ({meta['atoll_prefix']:<4}) -> {meta['out_filename']:<16} [{count:,} rows | {date_start} to {date_end}]")

    # Sort unified records chronologically, then by station_id
    unified_records.sort(key=lambda r: (r[0], r[1]))

    unified_path = os.path.join(CLEANED_DIR, 'maldives_national_weather_daily.csv')
    with open(unified_path, 'w', newline='', encoding='utf-8') as out_f:
        writer = csv.writer(out_f)
        writer.writerow(UNIFIED_COLUMNS)
        writer.writerows(unified_records)

    print(f"\nSuccessfully generated unified dataset: {os.path.basename(unified_path)}")
    print(f"Total processed records across all stations: {len(unified_records):,}")


if __name__ == '__main__':
    main()
