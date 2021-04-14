#! /usr/bin/env python3

"""
Compute statistics from the results
"""

from csv import DictReader
from pprint import pprint
from typing import Dict

def row_count_q(row_data, count_dict):
    if row_data not in count_dict:
        count_dict[row_data] = 0
    count_dict[row_data] += 1

# Read the clean results
with open("clean.csv", newline="") as f:
    dict_reader = DictReader(f)

    # Data
    countries: Dict[str, int] = {}
    sources: Dict[str, int] = {}

    # Get the data from each row
    for i, row in enumerate(dict_reader):
        row_count_q(row["Q1"], countries)
        row_count_q(row["Q2"], sources)

    # Print
    print(f"Number of responses: {i+1}")
    print(f"Countries:")
    pprint(countries)
    print(f"Sources:")
    pprint(sources)
