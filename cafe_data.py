import csv
import os


DEFAULT_CSV_FILE = "cafe-data.csv"

DEFAULT_HEADER = ["Cafe Name", "Location", "Open", "Close", "Coffee", "Wifi", "Power"]


class CafeManager:

    def __init__(self, data_file=DEFAULT_CSV_FILE):

        self._data_file = data_file

    def get_cafes(self):
        """Returns the header and the contents of the CSV file as LISTS."""
        try:
            with open(file=self._data_file, mode="r", encoding="utf-8", newline='') as f:
                reader = csv.reader(f)
                cafe_header = []
                cafe_list = []
                for row in reader:
                    
                    if len(cafe_header) == 0:
                        cafe_header = row
                    else:
                        cafe_list.append(row)
        except FileNotFoundError:
         
            cafe_header = DEFAULT_HEADER
            cafe_list = []
        return cafe_header, cafe_list

    def add_cafe(self, new_entry):
        """Takes a LIST and adds it as new row into the data file."""
        if not self._data_file:
            with open(file=self._data_file, mode="w", encoding="utf-8", newline='') as f:
                header = ','.join(DEFAULT_HEADER)
                f.write(header)
        # add the new cafe with proper quoting
        new_row = ','.join([f'"{item}"' if ',' in item else item for item in new_entry])
        with open(file=self._data_file, mode="a", encoding="utf-8", newline='') as f:
            f.write('\n' + new_row)
