"""
Export ``DAX`` formulas from a ``Power BI`` template file.

``Power BI`` files in the ``pbix`` and ``pbit`` formats are basically zip
archives containing other compressed data. The ``DataModel`` file in a ``pbix``
file contains all the ``DAX`` formulas created when processing data. Formulas
are saved in the ``Xpress9`` format, which is a proprietary compresson method
optimized to dump memory to disk and vice-versa, with encryption and all kinds
of other wonderful features which will break you heart if you try to get a
peek inside.

Fortunately, if one saves a ``Power BI`` workbook as a template, the ``DAX``
formulas are now saved in the ``DataModelSchema`` object, which is unencrypted
and requires only a bit of fiddling to remove.

This script is intended to help with that fiddling, and to aid users in
serializing work done in an otherwise fairly opaque binary format. Here's
hoping it's useful to you.

At this point, there appears to be no way to automate exporting ``pbix`` files
as ``pbit``, so you'll have to do that the usual way.

This script will work as long as it does, given the rate of churn (I mean
development) in ``Power BI``. Good luck!


Example:
::
    usage: daxextract.py [-h] pbit_path [csv_path]

    Extract DAX expressions from Power BI template file.

    positional arguments:
      pbit_path   Path to .pbit file.
      csv_path    Path to write DAX expressions and metadata in csv format. If
                  this argument is not specified, formulas will be written to
                  STDOUT

    optional arguments:
      -h, --help  show this help message and exit

"""

import argparse
import csv
import json
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile


class DaxExtract:
    """
    Extract ``DAX`` expressions from Power BI templates."
    """
    def __init__(self):
        """
        Run ``argparse.ArgumentParser`` to give a nice args object.
        """

        parser = argparse.ArgumentParser(
            description="Extract DAX expressions from Power BI template file."
        )

        parser.add_argument("pbit_path", type=str, help="Path to .pbit file.")
        parser.add_argument(
            "csv_path",
            type=str,
            help="""Path to write DAX expressions and metadata in csv format.
            If this argument is not specified, formulas will be written to STDOUT""",
            nargs="?",
        )

        self.args = parser.parse_args()

    def extract_data_model_schema(self):
        """
        Extract ``DataModelSchema`` from ``.pbit`` archive.

        Returns:
            data (dict): ``dict`` object of ``DataModelSchema`` data.
        """

        pbit_path = Path(self.args.pbit_path)

        if not pbit_path.is_file():
            raise OSError(f"{pbit_path} not found or not a file.")

        if not pbit_path.parts[-1:][0].endswith(".pbit"):
            raise OSError(f"{pbit_path} is not a Power BI template (pbit) file.")

        # extract data to temporary directory
        with tempfile.TemporaryDirectory() as tempdir:
            with ZipFile(pbit_path, "r") as pbit:
                for info in pbit.infolist():
                    if info.filename == "DataModelSchema":
                        filepath = Path(tempdir, info.filename)
                        pbit.extract(info, tempdir)
                        # read data as utf-8
                        with open(filepath, "r") as _fh:
                            data = json.loads(bytes(_fh.read(), "utf-8"))
                            if data:
                                return data

        # if we are here, there was either no "DataModelSchema" object, or it
        # was empty. Bummer.

        raise OSError(f"Unable to extract DataModelSchema from {pbit_path}.")

    def extract_dax(self):
        """
        Extract ``DAX`` formulas from ``DataModelSchema``.

        Returns:
            dax (dict): dax formulas and metadata.
        """

        data = self.extract_data_model_schema()

        dax = {
            "fieldnames": [
                "table_name",
                "measure_name",
                "data_type",
                "dax_expression",
            ],
            "measures": [],
        }

        for table in data["model"]["tables"]:
            if "measures" in table:
                for measure in table["measures"]:
                    dax["measures"].append(
                        {
                            "table_name": table.get("name"),
                            "measure_name": measure.get("name"),
                            "data_type": measure.get("dataType"),
                            "dax_expression": measure.get("expression"),
                        }
                    )

        return dax

    def dax_to_stdout(self):
        """
        Write nicely-formatted ``DAX`` expressions and metadata to STDOUT
        """
        sys.stdout.write(json.dumps(self.extract_dax(), indent=True))

    def dax_to_csv(self):
        """
        Write ``DAX`` expressions and metadata to file in ``.csv`` format.
        """

        dax = self.extract_dax()

        with open(Path(self.args.csv_path), "w", newline="") as _fh:
            writer = csv.DictWriter(_fh, fieldnames=dax["fieldnames"])
            writer.writeheader()
            writer.writerows(dax["measures"])
