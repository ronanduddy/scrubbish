import json
import time
import csv


class CsvHelper:
    def __init__(self, filename):
        self.filename = filename
        self.directory = "csv"
        self.file = None
        self.fieldnames = None
        self.writer = None
        self.creation = time.time()

    def write(self, row):
        self._writer("w+", row)

    def append(self, row):
        self._writer("a", row)

    def read(self):
        return csv.DictReader(self._file("r"))

    def _filename(self):
        if len(self.filename.split("/")) == 1:
            return f"{self.directory}/{self.filename}_{self.creation}.csv"

        return self.filename

    def _file(self, operation):
        if self.file is None:
            self.file = open(self._filename(), operation)

        return self.file

    def _writer(self, operation, row):
        if self.fieldnames is None:
            self.fieldnames = row.keys()

        if self.writer is None:
            self.writer = csv.DictWriter(
                self._file(operation), fieldnames=self.fieldnames
            )

            if operation[0] == "w":
                self.writer.writeheader()

        self.writer.writerow(row)
