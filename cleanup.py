#! /usr/bin/env python3

"""
Pre-process and cleanup the csv file for use in actual processing

* Cleans up the column names
* Removes unused questions
"""

import csv

# Read the results to clean
with open("cleaned.csv", newline="") as f:
    dict_reader = csv.DictReader(f)

    with open("clean.csv", "w", newline="") as wf:
        # Merge in columns
        dict_writer = csv.DictWriter(wf, dict_reader.fieldnames)
        dict_writer.writeheader()
        for row in dict_reader:
            to_write = row.copy()

            # Q2, change to abcdefg and combine with write-in
            if to_write["Q2"] == "Twitter":
                to_write["Q2"] = "a"
            elif to_write["Q2"] == "Reddit":
                to_write["Q2"] = "b"
            elif to_write["Q2"] == "IRC":
                to_write["Q2"] = "c"
            elif to_write["Q2"] == "Bitcoin Talk":
                to_write["Q2"] = "d"
            elif to_write["Q2"] == "Bitcoin Opt-Tech Newsletter":
                to_write["Q2"] = "e"
            elif to_write["Q2"] == "Defline to specify":
                to_write["Q2"] = "f"
            elif to_write["Q2"] == "Other (Write-In)":
                to_write["Q2"] = f"g {to_write['Q2 Writein']}"

            # Q3, change to abc
            if to_write["Q3"] == "Yes":
                to_write["Q3"] = "a"
            elif to_write["Q3"] == "No, but I have in the past":
                to_write["Q3"] = "b"
            elif to_write["Q3"] == "No, I have never run a node with Bitcoin Core":
                to_write["Q3"] = "c"

            # Merge Q4 and Q4_2
            to_write["Q4"] += to_write["Q4_2"]

            # Q4, change to abc
            if to_write["Q4"] == "Yes":
                to_write["Q4"] = "a"
            elif to_write["Q4"] == "No, but I have in the past":
                to_write["Q4"] = "b"
            elif to_write["Q4"] == "No, I have never used Bitcoin Core wallet":
                to_write["Q4"] = "c"

            # Merge Q5 and Q5_2 and Q5_3
            to_write["Q5"] += to_write["Q5_2"]
            to_write["Q5"] += to_write["Q5_3"]

            # Q6 options, set to X if non-empty
            if to_write["Q6a"]:
                to_write["Q6a"] = "X"
            if to_write["Q6b"]:
                to_write["Q6b"] = "X"
            if to_write["Q6c"]:
                to_write["Q6c"] = "X"
            if to_write["Q6d"]:
                to_write["Q6d"] = "X"
            if to_write["Q6e"]:
                to_write["Q6e"] = "X"

            # Q7, change to abcd
            if to_write["Q7"] == "0-6 Months":
                to_write["Q7"] = "a"
            elif to_write["Q7"] == "6-12 Months":
                to_write["Q7"] = "b"
            elif to_write["Q7"] == "1-3 Years":
                to_write["Q7"] = "c"
            elif to_write["Q7"] == "3+ years":
                to_write["Q7"] = "d"

            # Q8 options, set to X if non-empty
            if to_write["Q8a"]:
                to_write["Q8a"] = "X"
            if to_write["Q8b"]:
                to_write["Q8b"] = "X"
            if to_write["Q8c"]:
                to_write["Q8c"] = "X"
            if to_write["Q8d"]:
                to_write["Q8d"] = "X"

            # Merge Q9* and Q9*_2 and Q9*_3
            to_write["Q9a"] += to_write["Q9a_2"]
            to_write["Q9b"] += to_write["Q9b_2"]
            to_write["Q9c"] += to_write["Q9c_2"]
            to_write["Q9d"] += to_write["Q9d_2"]
            to_write["Q9e"] += to_write["Q9e_2"]
            to_write["Q9f"] += to_write["Q9f_2"]
            to_write["Q9g"] += to_write["Q9g_2"]
            to_write["Q9h"] += to_write["Q9h_2"]
            to_write["Q9i"] += to_write["Q9i_2"]
            to_write["Q9a"] += to_write["Q9a_3"]
            to_write["Q9b"] += to_write["Q9b_3"]
            to_write["Q9c"] += to_write["Q9c_3"]
            to_write["Q9d"] += to_write["Q9d_3"]
            to_write["Q9e"] += to_write["Q9e_3"]
            to_write["Q9f"] += to_write["Q9f_3"]
            to_write["Q9g"] += to_write["Q9g_3"]
            to_write["Q9h"] += to_write["Q9h_3"]

            # Q9 options, set to X if non-empty
            if to_write["Q9a"]:
                to_write["Q9a"] = "X"
            if to_write["Q9b"]:
                to_write["Q9b"] = "X"
            if to_write["Q9c"]:
                to_write["Q9c"] = "X"
            if to_write["Q9d"]:
                to_write["Q9d"] = "X"
            if to_write["Q9e"]:
                to_write["Q9e"] = "X"
            if to_write["Q9f"]:
                to_write["Q9f"] = "X"
            if to_write["Q9g"]:
                to_write["Q9g"] = "X"
            if to_write["Q9h"]:
                to_write["Q9h"] = "X"

            # Q10, change to abcd
            if to_write["Q10"] == "Every release":
                to_write["Q10"] = "a"
            elif to_write["Q10"] == "Every Major (Feature) Release":
                to_write["Q10"] = "b"
            elif to_write["Q10"] == "Every Minor (Security) release":
                to_write["Q10"] = "c"
            elif to_write["Q10"] == "Other - Write In":
                to_write["Q10"] = f"d {to_write['Q10 Writein']}"

            # Q11, change to abcd
            if to_write["Q11"] == ">=0.20":
                to_write["Q11"] = "a"
            elif to_write["Q11"] == "0.19":
                to_write["Q11"] = "b"
            elif to_write["Q11"] == "0.18":
                to_write["Q11"] = "c"
            elif to_write["Q11"] == "0.17":
                to_write["Q11"] = "d"

            # Q12 options, set to X if non-empty
            if to_write["Q12a"]:
                to_write["Q12a"] = "X"
            if to_write["Q12b"]:
                to_write["Q12b"] = "X"
            if to_write["Q12c"]:
                to_write["Q12c"] = "X"
            if to_write["Q12d"]:
                to_write["Q12d"] = "X"
            if to_write["Q12e"]:
                to_write["Q12e"] = "X"

            # Q13 options, set to X if non-empty
            if to_write["Q13a"]:
                to_write["Q13a"] = "X"
            if to_write["Q13b"]:
                to_write["Q13b"] = "X"
            if to_write["Q13c"]:
                to_write["Q13c"] = "X"
            if to_write["Q13d"]:
                to_write["Q13d"] = "X"
            if to_write["Q13e"]:
                to_write["Q13e"] = "X"
            if to_write["Q13f"]:
                to_write["Q13f"] = "X"

            # Merge Q14 and Q14_2 and Q14_3
            to_write["Q14"] += to_write["Q14_2"]
            to_write["Q14"] += to_write["Q14_3"]

            # Q15, change to abcd
            if to_write["Q15"] == "0-6 Months":
                to_write["Q15"] = "a"
            elif to_write["Q15"] == "6-12 Months":
                to_write["Q15"] = "b"
            elif to_write["Q15"] == "1-3 Years":
                to_write["Q15"] = "c"
            elif to_write["Q15"] == "3+ years":
                to_write["Q15"] = "d"

            # Q16, change to abcd
            if to_write["Q16"] == "0-6 Months ago":
                to_write["Q16"] = "a"
            elif to_write["Q16"] == "6-12 Months ago":
                to_write["Q16"] = "b"
            elif to_write["Q16"] == "1-3 Years ago":
                to_write["Q16"] = "c"
            elif to_write["Q16"] == "3+ years ago":
                to_write["Q16"] = "d"

            # Q17 options, set to X if non-empty
            if to_write["Q17a"]:
                to_write["Q17a"] = "X"
            if to_write["Q17b"]:
                to_write["Q17b"] = "X"
            if to_write["Q17c"]:
                to_write["Q17c"] = "X"
            if to_write["Q17d"]:
                to_write["Q17d"] = "X"

            # Q19, change to abcd
            if to_write["Q19"] == "Ease of use":
                to_write["Q19"] = "a"
            elif to_write["Q19"] == "Privacy":
                to_write["Q19"] = "b"
            elif to_write["Q19"] == "Backed by members in the community I trust":
                to_write["Q19"] = "c"
            elif to_write["Q19"] == "Other - Write-In":
                to_write["Q19"] = f"d {to_write['Q19 Writein']}"

            # Q20 options, set to X if non-empty
            if to_write["Q20a"]:
                to_write["Q20a"] = "X"
            if to_write["Q20b"]:
                to_write["Q20b"] = "X"
            if to_write["Q20c"]:
                to_write["Q20c"] = "X"

            # Q22 options, set to X if non-empty
            if to_write["Q22a"]:
                to_write["Q22a"] = "X"
            if to_write["Q22b"]:
                to_write["Q22b"] = "X"
            if to_write["Q22c"]:
                to_write["Q22c"] = "X"

            # Q23, change to abcd
            if to_write["Q23"] == "Yes, it's my only Bitcoin Wallet":
                to_write["Q23"] = "a"
            elif to_write["Q23"] == "No, I use other wallets too":
                to_write["Q23"] = "b"

            # Q26, change to abcd
            if to_write["Q26"] == "< 100":
                to_write["Q26"] = "a"
            elif to_write["Q26"] == "100 -1000":
                to_write["Q26"] = "b"
            elif to_write["Q26"] == "> 1000":
                to_write["Q26"] = "c"
            elif to_write["Q26"] == "Not Sure":
                to_write["Q26"] = "d"

            # Q27 options, set to X if non-empty
            if to_write["Q27a"]:
                to_write["Q27a"] = "X"
            if to_write["Q27b"]:
                to_write["Q27b"] = "X"
            if to_write["Q27c"]:
                to_write["Q27c"] = "X"
            if to_write["Q27d"]:
                to_write["Q27d"] = "X"
            if to_write["Q27e"]:
                to_write["Q27e"] = "X"
            if to_write["Q27f"]:
                to_write["Q27f"] = "X"

            # Merge Q29* and Q29*_2
            to_write["Q29a"] += to_write["Q29a_2"]
            to_write["Q29b"] += to_write["Q29b_2"]
            to_write["Q29c"] += to_write["Q29c_2"]
            to_write["Q29d"] += to_write["Q29d_2"]
            to_write["Q29e"] += to_write["Q29e_2"]

            # Q29 options, set to X if non-empty
            if to_write["Q29a"]:
                to_write["Q29a"] = "X"
            if to_write["Q29b"]:
                to_write["Q29b"] = "X"
            if to_write["Q29c"]:
                to_write["Q29c"] = "X"
            if to_write["Q29d"]:
                to_write["Q29d"] = "X"

            # Q31, change to abcd
            if to_write["Q31"] == "0-6 Months":
                to_write["Q31"] = "a"
            elif to_write["Q31"] == "6-12 Months":
                to_write["Q31"] = "b"
            elif to_write["Q31"] == "1-3 Years":
                to_write["Q31"] = "c"
            elif to_write["Q31"] == "3+ years":
                to_write["Q31"] = "d"

            # Q32 options, set to X if non-empty
            if to_write["Q32a"]:
                to_write["Q32a"] = "X"
            if to_write["Q32b"]:
                to_write["Q32b"] = "X"
            if to_write["Q32c"]:
                to_write["Q32c"] = "X"

            # Q34 options, set to X if non-empty
            if to_write["Q34a"]:
                to_write["Q34a"] = "X"
            if to_write["Q34b"]:
                to_write["Q34b"] = "X"
            if to_write["Q34c"]:
                to_write["Q34c"] = "X"

            # Q35, change to abcd
            if to_write["Q35"] == "When I stopped running a Core Node":
                to_write["Q35"] = "a"
            elif to_write["Q35"] == "Before I stopped running a Core Node":
                to_write["Q35"] = "b"

            # Q36, change to abcd
            if to_write["Q36"] == "0-6 Months ago":
                to_write["Q36"] = "a"
            elif to_write["Q36"] == "6-12 Months ago":
                to_write["Q36"] = "b"
            elif to_write["Q36"] == "1-3 Years ago":
                to_write["Q36"] = "c"
            elif to_write["Q36"] == "3+ years ago":
                to_write["Q36"] = "d"

            # Merge Q39 and Q39_2
            to_write["Q39"] += to_write["Q39_2"]

            # Q41, change to abcd
            if to_write["Q41"] == "Yes":
                to_write["Q41"] = "a"
            elif to_write["Q41"] == "No":
                to_write["Q41"] = "b"

            # Q42, change to abcd
            if to_write["Q42"] == "I don't remember why I decided not to use Bitcoin Core Wallet":
                to_write["Q42"] = "a"
            elif to_write["Q42"] == "Reason:":
                to_write["Q42"] = f"b {to_write['Q42 Writein']}"

            # Q43 options, set to X if non-empty
            if to_write["Q43a"]:
                to_write["Q43a"] = "X"
            if to_write["Q43b"]:
                to_write["Q43b"] = "X"
            if to_write["Q43c"]:
                to_write["Q43c"] = "X"
            if to_write["Q43d"]:
                to_write["Q43d"] = "X"
            if to_write["Q43e"]:
                to_write["Q43e"] = "X"
            if to_write["Q43f"]:
                to_write["Q43f"] = "X"
            if to_write["Q43g"]:
                to_write["Q43g"] = "X"

            # Q45, change to abcd
            if to_write["Q45"] == "Yes":
                to_write["Q45"] = "a"
            elif to_write["Q45"] == "No":
                to_write["Q45"] = "b"

            # Q48, change to abcd
            if to_write["Q48"] == "Yes":
                to_write["Q48"] = "a"
            elif to_write["Q48"] == "No":
                to_write["Q48"] = "b"

            # Q49 options, set to X if non-empty
            if to_write["Q49a"]:
                to_write["Q49a"] = "X"
            if to_write["Q49b"]:
                to_write["Q49b"] = "X"
            if to_write["Q49c"]:
                to_write["Q49c"] = "X"

            # Write it
            dict_writer.writerow(to_write)
