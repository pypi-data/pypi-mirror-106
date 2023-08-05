#!/usr/bin/env python

"""
Run dax_extract module with command line arguments
"""

from dax_extract import DaxExtract

def main():
    """
    Run DaxExtract to file or ``STDOUT``.
    """

    _da = DaxExtract()

    if _da.args.csv_path:
        _da.dax_to_csv()
    else:
        _da.dax_to_stdout()
