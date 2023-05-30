import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("kendalls_tau_6d.csv", sep=";")
data = data.set_index("system")

#fig, ax = plt.subplots(figsize=(12,12))
ax = sns.heatmap(data, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
ax.set(xlabel=None, ylabel=None)
plt.savefig('heatmap_6d.png', bbox_inches="tight")