import os
import glob
from datetime import datetime

import pandas as pd


partial_results = 'partial_results'


def save_results(results):
    search_timestamp = datetime.now().replace(microsecond=0).isoformat()

    if not os.path.isdir(partial_results):
        os.mkdir(partial_results)

    results.to_csv(
        f"{partial_results}/{search_timestamp}-phase1.csv", index=False)


def load_results():
    phase1_files = glob.glob(f"{partial_results}/*-phase1.csv")

    items = None

    for file in phase1_files:
        if items is None:
            items = pd.read_csv(file)
        else:
            df = pd.read_csv(file)
            items = pd.concat([items, df])

    return items.drop_duplicates().sort_values('repo_name', ignore_index=True)


def load_phase2_results():
    phase2_files = glob.glob(f"{partial_results}/*phase2.csv")
    phase2_files.sort()
    return pd.read_csv(phase2_files[-1])


def load_phase3_results():
    phase3_files = glob.glob(f"{partial_results}/*phase3.csv")
    phase3_files.sort()
    return pd.read_csv(phase3_files[-1])