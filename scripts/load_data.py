import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, file_path,sep="|"):
        self.file_path = file_path
        self.sep=sep

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path,sep="|")
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            return None    

