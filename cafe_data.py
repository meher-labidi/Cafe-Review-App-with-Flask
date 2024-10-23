import csv
import os

# default data file
DEFAULT_CSV_FILE = "cafe-data.csv"
# default header, in case there is no CSV file
DEFAULT_HEADER = ["Cafe Name", "Location", "Open", "Close", "Coffee", "Wifi", "Power"]


class CafeManager:

    def __init__(self, data_file=DEFAULT_CSV_FILE):
        # use the default CSV file, unless a different one is specified
        self._data_file = data_file

    def get_cafes(self):
        """Returns the header and the contents of the CSV file as LISTS."""
        try:
            with open(file=self._data_file, mode="r", encoding="utf-8", newline='') as f:
                reader = csv.reader(f)
                cafe_header = []
                cafe_list = []
                for row in reader:
                    # keep the header separate from the cafes
                    if len(cafe_header) == 0:
                        cafe_header = row
                    else:
                        cafe_list.append(row)
        except FileNotFoundError:
            # return the default header and an empty list of cafes
            cafe_header = DEFAULT_HEADER
            cafe_list = []
        return cafe_header, cafe_list

    def add_cafe(self, new_entry):
        """Takes a LIST and adds it as new row into the data file."""
        # in case there is no CSV file, create a new one with just the default header
        if not self._data_file:
            with open(file=self._data_file, mode="w", encoding="utf-8", newline='') as f:
                header = ','.join(DEFAULT_HEADER)
                f.write(header)
        # add the new cafe with proper quoting
        new_row = ','.join([f'"{item}"' if ',' in item else item for item in new_entry])
        with open(file=self._data_file, mode="a", encoding="utf-8", newline='') as f:
            f.write('\n' + new_row)
