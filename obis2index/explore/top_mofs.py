"""
Shows sorted count of the most common Measurement or Facts.
Use this to see what kind of MoFs your data subset contains.
"""
import sys
import pandas as pd
from argparse import ArgumentParser

from obis2index.util.plot_most_common_in_column \
    import plot_most_common_in_column


def top_mofs(mof_csv_filepath):
    print("showing top MoFs for file {}...".format(mof_csv_filepath))
    obis_mofs = pd.read_csv(mof_csv_filepath, low_memory=False)
    plot_most_common_in_column(df=obis_mofs, column='measurementType', TOP_N=9)


def parse_args(argv):
    parser = ArgumentParser(
        description="Shows sorted count of the most common Measurement or "
        "Facts"
    )
    parser.add_argument(
        "mof_csv_filepath",
        help="Measurment or Fact .csv file path"
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    top_mofs(**vars(parse_args(sys.argv[1:])))
