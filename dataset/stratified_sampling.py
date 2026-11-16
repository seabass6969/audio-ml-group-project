import shutil
import numpy as np
import pandas as pd

csv = pd.read_csv("./ESC-50/meta/esc50.csv")

categories = []

categories_dict = {}

for file in (csv["category"]):
    if file not in categories:
        categories.append(file)


min_number = 1000000
for category in categories:
    categories_dict[category] = csv[csv["category"] == category]["filename"]
    min_number = min(len(categories_dict[category]),min_number)
print(min_number)

categories_strata_dict = {}

rng = np.random.default_rng(seed=42)
for k,v in categories_dict.items():
    strata = rng.choice(v, size=min_number)
    categories_strata_dict[k] = strata


print(categories_strata_dict)
for category, values in categories_dict.items():
    for index, value in enumerate(values):
        shutil.copy("./ESC-50/audio/" + value, f"./ESC50_Junk_strata/{category}-{index:03d}.wav")
