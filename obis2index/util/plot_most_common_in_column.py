import seaborn
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint


def plot_most_common_in_column(df, column, TOP_N):
    """shows the TOP_N most common values in given column for dataframe df"""
    print("plotting top {} values for column '{}'".format(TOP_N, column))

    counts = df[column].value_counts()
    plt.figure(figsize=(20, 6))

    pprint(list(counts.index)[:TOP_N])
    g = sns.barplot(
        list(counts.index)[:TOP_N],
        counts.values[:TOP_N],
        alpha=0.8
    )
    g.set_yscale("log")
    plt.show()
