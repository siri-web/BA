import pandas as pd
from scipy.stats import kendalltau
from collections import defaultdict


data = pd.read_csv("Table.csv", sep=";")
tau = defaultdict(list)

for name_1 in data["system"].unique():
    for name_2 in data["system"].unique():
        system_1 = data.loc[(data["system"] == name_1) & (data["dialect"].isin(["Bern", "Grisons", "Valais", "Basel",
                                                                                "Lucerne", "Zürich"]))]
        system_2 = data.loc[(data["system"] == name_2) & (data["dialect"].isin(["Bern", "Grisons", "Valais", "Basel",
                                                                                "Lucerne", "Zürich"]))]
        system_1 = system_1.loc[system_1["dialect"].isin(system_2["dialect"].unique())]
        system_1 = system_1.sort_values(by=["dialect"])
        system_2 = system_2.sort_values(by=["dialect"])
        system_1["corrected_rank"] = system_1["Rank"].rank()
        system_1 = system_1.astype({"corrected_rank": "int"})
        system_2["corrected_rank"] = system_2["Rank"].rank()
        system_2 = system_2.astype({"corrected_rank": "int"})
        X = system_1["corrected_rank"].values.tolist()
        Y = system_2["corrected_rank"].values.tolist()
        tau[name_1].append(kendalltau(X, Y)[0])

df = pd.DataFrame.from_dict(tau)
df.index = data["system"].unique().tolist()
df.to_csv(r"kendalls_tau_6d.csv", index=True, header=True, sep=";")