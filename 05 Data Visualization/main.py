import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

avocado = pd.read_csv(
    "avocado.csv",
    index_col=0,
)
sns.set()
# sns.lineplot(
#     x="Generation",
#     y="Total",
#     data=pokemon
#
# )

# generation_values = pd.melt(
#     pokemon,
#     id_vars=["Generation"],
#     value_vars=["Speed", "Defense", "Sp. Def", "Sp. Atk", "HP", "Attack"],
# )
#
# fig = plt.subplot()
# sns.lineplot(
#     x="Generation",
#     y="value",
#     hue="variable",
#     ci=None,
#     data=generation_values,
# )
# # fig.set_size_inches(12, 8)
# pokemon["Generation"].value_counts().plot.bar()
# sns.barplot(
#     x="Generation",
#     y="Total",
#     data=pokemon
# )

# sns.countplot(
#     "Generation",
#     data=pokemon
# )


avocado.groupby('region').AveragePrice.min().plot.countplot()

plt.show()
