# smartdataorganizer_app/models.py
from django.db import models
import pandas as pd


class Spreadsheet(models.Model):
    file = models.FileField(upload_to='spreadsheets/')

    def get_column_names(self):
        # Assuming the file is an Excel file (.xlsx), modify as needed
        try:
            df = pd.read_excel(self.file.path, engine='openpyxl')
            return df.columns.tolist()
        except pd.errors.EmptyDataError:
            # Handle the case where the file is empty
            return []
        except Exception as e:
            # Handle other exceptions
            print(f"Error reading file: {e}")
            return []
        
    def get_data(self):
        try:
            df = pd.read_excel(self.file.path, engine='openpyxl')
            # Assuming you want to return the entire DataFrame
            return df
        except pd.errors.EmptyDataError:
            return pd.DataFrame()
        except Exception as e:
            print(f"Error reading file: {e}")
            return pd.DataFrame()
