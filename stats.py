#! /usr/bin/env python3

"""
Compute statistics from the results
"""

from collections import OrderedDict
from csv import DictReader
from pprint import pprint
from typing import Dict

def print_dict_sorted(data):
    sorted_data = sorted(data.items(), key=lambda item: item[1])
    sorted_data.reverse()
    pprint(sorted_data)

def row_count_q(row_data, count_dict):
    # Normalize to lowercase
    row_data = row_data.lower()

    # Get the counts
    if row_data not in count_dict:
        count_dict[row_data] = 0
    count_dict[row_data] += 1

# Read the clean results
with open("clean.csv", newline="") as f:
    dict_reader = DictReader(f)

    # Data
    countries: Dict[str, int] = {}
    sources: Dict[str, int] = {}
    do_wallet_use_gui: Dict[str, int] = {}
    do_wallet_use_daemon: Dict[str, int] = {}
    do_wallet_use_3p: Dict[str, int] = {}
    did_wallet_use_gui: Dict[str, int] = {}
    did_wallet_use_daemon: Dict[str, int] = {}
    did_wallet_use_3p: Dict[str, int] = {}

    # Get the data from each row
    for i, row in enumerate(dict_reader):
        row_count_q(row["Q1"], countries)
        row_count_q(row["Q2"], sources)
        row_count_q(row["Q20a"], do_wallet_use_gui)
        row_count_q(row["Q20b"], do_wallet_use_daemon)
        row_count_q(row["Q20c"], do_wallet_use_3p)
        row_count_q(row["Q32a"], did_wallet_use_gui)
        row_count_q(row["Q32b"], did_wallet_use_daemon)
        row_count_q(row["Q32c"], did_wallet_use_3p)

    # Print
    print(f"Number of responses: {i+1}")
    print(f"Countries:")
    print_dict_sorted(countries)
    print(f"Sources:")
    print_dict_sorted(sources)
    print("Do Use Wallet GUI")
    print_dict_sorted(do_wallet_use_gui)
    print("Do Use Wallet with Daemon")
    print_dict_sorted(do_wallet_use_daemon)
    print("Do Use Wallet through 3rd Party")
    print_dict_sorted(do_wallet_use_3p)
    print("Did Use Wallet GUI")
    print_dict_sorted(did_wallet_use_gui)
    print("Did Use Wallet with Daemon")
    print_dict_sorted(did_wallet_use_daemon)
    print("Did Use Wallet through 3rd Party")
    print_dict_sorted(did_wallet_use_3p)
