import argparse
import logging
import os
import time
from typing import List

import numpy as np
import pandas as pd
from rich.console import Console
from rich.progress import Progress

from . import csv_edem_controller, csv_input, utils

logger = logging.getLogger(__name__)


class CSV_Edem_Batch:
    def __init__(self, input_file: str, args: argparse.Namespace):
        logger.info(
            "Creating object CSV_Edem_Batch with input file '{}'".format(input_file)
        )

        self._input_file = input_file
        self._files: List[str] = []
        self._number_files: int = 0

        self.args: argparse.Namespace = args

        self.mean_cols: np.ndarray = np.array([])
        self.logmean_cols: np.ndarray = np.array([])

        self.mean_fors: np.ndarray = np.array([])
        self.logmean_fors: np.ndarray = np.array([])

        self._export_log: bool = self.args.log

        # check if batch file exists
        if not os.path.isfile(self._input_file):
            logger.warn(
                'Batch mode input file "{}" does not exist'.format(self._input_file)
            )
            return

        self.extractFiles()

    def extractFiles(self) -> None:
        logger.info("extractFiles method called")
        with open(self._input_file) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        self._files = [x.strip() for x in content if utils.isValidCSV(x.strip())]
        logger.info("Files found:\n\t\t\t{}".format(self._files))
        self._number_files = len(self._files)
        logger.info("Number of files: {}".format(self._number_files))

    def executeBatch(self, progress_bar: Console = None) -> None:
        logger.info("executeBatch method called")

        skip: int = int(self.args.skip_rows[0])
        cut_time: float = float(self.args.cut_time[0])

        # allocate room for np arrays
        self.mean_cols = np.zeros(self._number_files, dtype=np.float32)
        self.logmean_cols = np.zeros(self._number_files, dtype=np.float32)

        self.mean_fors = np.zeros(self._number_files, dtype=np.float32)
        self.logmean_fors = np.zeros(self._number_files, dtype=np.float32)

        logger.info("Looping through each file")

        if progress_bar is not None:
            progress = Progress(console=progress_bar, transient=True)
            task = progress.add_task(
                total=len(self._files),
                description="Processing...",
            )
            progress.start()

        for i, file in enumerate(self._files):
            # call input

            inpt = csv_input.CSV_Edem_input(file, lines_to_skip=skip)
            basename_input = os.path.splitext(inpt.getFilename())[0]
            excel_file: str = (
                basename_input if (self.args.excel == "excel") else self.args.excel
            )
            summary_file: str = (
                basename_input
                if (self.args.summary == "summary")
                else self.args.summary
            )

            # Check if file exists
            if not inpt.checkIfFileExists():
                logger.warning("File '{}' does not exists!!".format(inpt.getFilename()))
                return

            inpt.extractRawData()
            inpt.getDataFromTime(cut_time)

            cntrllr = csv_edem_controller.CSV_Edem_Controller(inpt)

            self.mean_cols[i] = cntrllr.getMeanCol()
            self.logmean_cols[i] = cntrllr.getLogMeanCol()
            self.mean_fors[i] = cntrllr.getMeanForce()
            self.logmean_fors[i] = cntrllr.getLogMeanForce()

            if progress_bar is not None:
                progress.advance(task, 1)
                time.sleep(0.1)

        if progress_bar is not None:
            progress.remove_task(task)

    def getHeaders(self) -> List[str]:
        if self._export_log:
            return [
                "File",
                "Collision Number - Mean [-]",
                "Collision Number - Log Mean [-]",
                "Collision Normal Force Magnitude - Mean [N]",
                "Collision Normal Force Magnitude - Log Mean [N]",
            ]
        else:
            return [
                "File",
                "Collision Number - Mean [-]",
                "Collision Normal Force Magnitude - Mean [N]",
            ]

    def getFiles(self) -> List[str]:
        return self._files

    def getMeanCollisons(self) -> np.ndarray:
        return self.mean_cols

    def getMeanOfNormalCollisions(self) -> float:
        return float(np.mean(self.mean_cols))

    def getMeanOfNormalForces(self) -> float:
        return float(np.mean(self.mean_fors))

    def getMeanOfLogCollisions(self) -> float:
        return float(np.mean(self.logmean_cols))

    def getMeanOfLogForces(self) -> float:
        return float(np.mean(self.logmean_fors))

    def isExportingLog(self) -> bool:
        return self._export_log

    def getData(self) -> np.ndarray:
        if self._export_log:
            data = np.transpose(
                np.array(
                    [
                        self._files,
                        self.mean_cols,
                        self.logmean_cols,
                        self.mean_fors,
                        self.logmean_fors,
                    ]
                )
            )
        else:
            data = np.transpose(
                np.array(
                    [
                        self._files,
                        self.mean_cols,
                        self.mean_fors,
                    ]
                )
            )
        return data

    def saveToExcel(self, excel_filename: str) -> None:
        logger.info("saveToExcel called with argument '{}'".format(excel_filename))

        filename = excel_filename + ".xlsx"
        sheetname = "edem_batch_data"

        headers = self.getHeaders()
        data = self.getData()

        if self._export_log:
            logger.info("Exporting log mean information")
        else:
            logger.info("Not exporting log mean information")

        df = pd.DataFrame(data, columns=headers)

        # save data to excel and auto adjust columns width
        writer = pd.ExcelWriter(
            filename, engine="xlsxwriter", options={"strings_to_numbers": True}
        )

        df.to_excel(writer, sheet_name=sheetname, index=False)  # send df to writer
        worksheet = writer.sheets[sheetname]  # pull worksheet object
        for idx, col in enumerate(df):  # loop through all columns
            series = df[col]
            max_len = (
                max(
                    (
                        series.astype(str).map(len).max(),  # len of largest item
                        len(str(series.name)),  # len of column name/header
                    )
                )
                + 1
            )  # adding a little extra space
            worksheet.set_column(idx, idx, max_len)  # set column width
        writer.save()

        logger.info('Exported data to excel file: "{}"'.format(filename))
        return
