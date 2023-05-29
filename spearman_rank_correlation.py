from scipy.stats import spearmanr
import pandas as pd

df = pd.read_csv("spearman_all_6d.csv", sep=";")

rank = df["performance rank"].tolist()
df = df.drop(columns=["performance rank", "system"])

for measure in df.columns:
    print(measure, spearmanr(df[measure].tolist(), rank).correlation)