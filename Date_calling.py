import pandas as pd
import numpy as np
import re
import tkinter as tk
from tkinter import filedialog

file_path = filedialog.askopenfilename(title='select a database')
df = pd.read_excel(file_path, header=1)


df['Date of calling '] = df['Date of calling '].astype(str)

# Regular expression to extract the date (YYYY-MM-DD)
date_pattern = r'^\d{4}-\d{2}-\d{2}'

# Function to extract the date from a string
def extract_date(value):
    match = re.match(date_pattern, value)
    if match:
        return match.group(0)
    return None

# Apply the function to the 'Date of calling ' column
df['Date of calling '] = df['Date of calling '].apply(extract_date)

file_name = 'date.xlsx'
df.to_excel(file_name)
print("Successful! Saved")