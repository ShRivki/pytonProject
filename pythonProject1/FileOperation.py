import pandas as pd
import datetime


class FileOperation:

    def __init__(self):
        pass

    def read_csv(self, file_path: str):
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print("File not found.")
            return None

    def save_to_csv(self, data, file_name: str):
        try:
            data.to_csv(file_name, index=False)
            print(f"Data saved to {file_name}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def error(self, error: str):
        print('<{0},{1} >,type error:{2}<{0}>'.format('rivki', datetime.datetime.now().strftime("%d.%m.%y, %H:%M"),
                                                      error))

    def read_file(self, path):
        try:
            with open(path, 'r') as f:
                return f.read()
        except FileNotFoundError as e:
            self.error(e)
