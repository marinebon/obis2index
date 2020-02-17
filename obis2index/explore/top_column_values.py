"""
Shows sorted count of the most common Measurement or Facts.
Use this to see what kind of MoFs your data subset contains.
"""
import sys
import pandas as pd
from argparse import ArgumentParser

from obis2index.util.plot_most_common_in_column \
    import plot_most_common_in_column


def top_column_values(csv_filepath, column_name):
    obis_mofs = pd.read_csv(csv_filepath, low_memory=False)
    plot_most_common_in_column(df=obis_mofs, column=column_name, TOP_N=9)


def parse_args(argv):
    parser = ArgumentParser(
        description="Shows sorted count of the most common Measurement or "
        "Facts"
    )
    parser.add_argument(
        "csv_filepath",
        help=".csv file path"
    )
    parser.add_argument(
        "column_name",
        help="name of column in dataframe to visualize"
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    top_column_values(**vars(parse_args(sys.argv[1:])))
