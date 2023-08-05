from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any, List

from rich.progress import track
from rich.table import Table

from . import __version__, csv_edem_batch, csv_edem_controller, csv_input, utils
from .rich_console import console

logger = logging.getLogger("csv_edem")

INPUT_TXT_DEFAULT = "input_csv_edem.txt"


def main(_args: List[str] = None) -> Any:

    default_skip_rows: int = 25
    default_cut_time: float = 1.01

    start_time = time.time()

    version_message = (
        "CSV EDEM reporter "
        + __version__
        + os.linesep
        + "Author: {}".format("Marcus Bruno Fernandes Silva")
        + os.linesep
        + "email: {}".format("marcusbfs@gmail.com")
    )

    desc = (
        version_message
        + os.linesep
        + os.linesep
        + "Process EDEM CSV files."
        + os.linesep
        + "Created for Gabi <3"
    )

    parser = argparse.ArgumentParser(
        description=desc, formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-s",
        "--single-file",
        dest="csv_file",
        nargs=1,
        help="single CSV EDEM file name with three columns: 1º time; 2º number of collisions; and 3º average force magnitude",
    )

    parser.add_argument(
        "-e",
        default="excel",
        dest="excel",
        help="base of the name of the excel file to be exported",
    )

    parser.add_argument(
        "--summary",
        default="summary",
        dest="summary",
        help="base of the name of the summary file to be exported",
    )

    parser.add_argument(
        "-n",
        "--no-comma",
        action="store_true",
        dest="no_comma",
        help="do not use comma (',') to separate decimal places (use '.')",
    )

    parser.add_argument(
        "-g",
        "--gen_batch",
        dest="gen_batch",
        nargs="?",
        default=".",
        help=f"generate input ({INPUT_TXT_DEFAULT}) file for batch mode",
    )

    parser.add_argument(
        "-b",
        "--batch",
        dest="batch",
        nargs="?",
        default=INPUT_TXT_DEFAULT,
        help=f'treat batch files. BATCH is a input file containing the CSV files in order to be processed. Default value is "{INPUT_TXT_DEFAULT}"',
    )

    parser.add_argument(
        "-l",
        "--log",
        action="store_true",
        dest="log",
        default=False,
        help="Exports log means as well",
    )

    parser.add_argument(
        "-t",
        dest="cut_time",
        nargs=1,
        default=[1.01],
        help="cut off time. Default value is {:.3f}".format(default_cut_time),
    )

    parser.add_argument(
        "-r",
        "--skip_rows",
        dest="skip_rows",
        nargs=1,
        default=[default_skip_rows],
        help="number of rows to skip. Default value is {}".format(default_skip_rows),
    )

    parser.add_argument(
        "-u",
        "--update",
        dest="update",
        default=False,
        help="update source code",
        action="store_true",
    )

    parser.add_argument(
        "--info",
        dest="info",
        default=False,
        help="Print aditional information",
        action="store_true",
    )

    parser.add_argument("-v", "--version", action="version", version=version_message)

    if _args:
        sys.argv = _args

    args = parser.parse_args(args=_args)
    level = logging.WARNING if not args.info else logging.INFO
    info = level == logging.INFO

    logging.basicConfig(level=level, format="%(asctime)s - %(name)s: %(message)s")

    logger.info("Arguments passed: {}".format(args))

    status_message = "Processing..."
    status = console.status(status_message)

    if args.update:
        logger.info("Calling update script...\n")

        from . import csv_edem_updater

        csv_edem_updater.update()

        return 0

    if ("-g" in sys.argv) or ("--gen_batch" in sys.argv):
        gen_dir: Path = (
            Path(".").resolve()
            if (args.gen_batch is None)
            else Path(args.gen_batch).resolve()
        )
        input_file = INPUT_TXT_DEFAULT
        logger.info('Generate batch file mode called with arg "{}"'.format(input_file))

        console.print(f'Generating files from "{str(gen_dir)}"')

        csv_files_in_curr_dir = [
            f for f in gen_dir.iterdir() if utils.isValidCSV(str(f))
        ]
        i = 1
        with open(input_file, "w") as outf:
            for csv in track(
                csv_files_in_curr_dir, description="Getting files...", transient=True
            ):
                time.sleep(0.1)
                outf.write(str(csv))
                outf.write(os.linesep)

        console.print(f"Found [bold blue]{len(csv_files_in_curr_dir)}[/] files:")
        for csv in csv_files_in_curr_dir:
            if not info:
                f = Path(os.curdir).resolve() / csv
                console.print(f'  {i:02d} - "{f}"')
                i += 1

        logger.info('"{}" generated'.format(input_file))

    elif ("-b" in sys.argv) or ("--batch" in sys.argv):
        input_file = INPUT_TXT_DEFAULT if (args.batch is None) else args.batch
        logger.info('Batch mode called with arg "{}"'.format(input_file))

        # check if batch file exists
        if not os.path.isfile(input_file):
            logger.warning(
                'Batch mode input file "{}" does not exist'.format(input_file)
            )
            return 1

        batch_ctrller = csv_edem_batch.CSV_Edem_Batch(input_file, args)
        batch_ctrller.executeBatch(progress_bar=console if not info else None)
        excel_file: str = "batch_EDEM_files"
        batch_ctrller.saveToExcel(excel_file)

        # show rich table
        headers = batch_ctrller.getHeaders()
        data = batch_ctrller.getData()
        table = Table()

        mean_row = ["" for _ in range(len(headers))]
        mean_row[0] = "Mean"
        mean_row[1] = f"{batch_ctrller.getMeanOfNormalCollisions():.5f}"

        if batch_ctrller.isExportingLog():
            mean_row[2] = f"{ batch_ctrller.getMeanOfLogCollisions():.5f}"
            mean_row[3] = f"{batch_ctrller.getMeanOfNormalForces():.5f}"
            mean_row[4] = f"{batch_ctrller.getMeanOfLogForces():.5f}"
        else:
            mean_row[2] = f"{batch_ctrller.getMeanOfNormalForces():.5f}"

        console.print(f"[bold blue]{Path(data[0,0]).parent.resolve()}")

        index = 0
        for header in headers:
            if index == 0:
                table.add_column(header, justify="left")
            else:
                table.add_column(header, justify="right")
            mean_row[index] = f"[bold red]{mean_row[index]}[/]"
            index += 1

        for i in range(len(data)):
            data[i, 0] = str(Path(data[i, 0]).name)
            if i == len(data) - 1:
                table.add_row(*data[i], end_section=True)
            else:
                table.add_row(*data[i])

        table.add_row(*mean_row)
        console.print(table)

    elif ("-s" in sys.argv) or ("--single-file" in sys.argv):
        if not info:
            status.start()

        logger.info("Single file mode")

        # call input
        skip: int = int(args.skip_rows[0])
        cut_time: float = float(args.cut_time[0])

        inpt = csv_input.CSV_Edem_input(args.csv_file[0], lines_to_skip=skip)
        basename_input = os.path.splitext(inpt.getFilename())[0]

        excel_file = basename_input if (args.excel == "excel") else args.excel
        summary_file: str = (
            basename_input if (args.summary == "summary") else args.summary
        )

        # Check if file exists

        if not inpt.checkIfFileExists():
            logger.warning("File '{}' does not exists!!".format(inpt.getFilename()))
            return 1

        inpt.extractRawData()
        inpt.getDataFromTime(cut_time)

        cntrllr = csv_edem_controller.CSV_Edem_Controller(inpt)

        # save
        cntrllr.saveSummary(
            summary_file, useCommaAsDecimal=not args.no_comma, export_log=args.log
        )
        cntrllr.saveToExcel(excel_file)
        # return cntrllr

        try:
            txt_file = summary_file + ".txt"
            with open(txt_file, "r") as tf:
                content = tf.read()
                console.print(content)
        except:
            pass

        if not info:
            status.stop()

    logger.info("Program finished in {:.3f} seconds".format(time.time() - start_time))

    return 0


if __name__ == "__main__":
    main()
