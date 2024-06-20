import re
from word2num import word2num
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Create a simple Tkinter root for file selection
root = tk.Tk()
root.withdraw()  # Hide the root window

# File selection with tkinter
file_path = filedialog.askopenfilename(title="Select a Dataset")

# Check if a file was selected
if not file_path:
    print("No file selected")
    exit()  # Exit if no file was selected

# Read the Excel file
df = pd.read_excel(file_path, header=1)

# Corrected regex pattern with proper escaping
temp_string_re = re.compile(r"([a-zA-Z]*)([0-9]*\.*[0-9]*)([ ]*)([-]*)([ ]*)([ ]*)([0-9]*\.*[0-9]*)([ ]*)([a-zA-Z]*)([ ]*)([a-zA-Z]*)([0-9]*)")

# Function to get distance metric
def get_distance_metric_Q6(test_str):
    # Handle NaN or None inputs to avoid AttributeError
    if pd.isna(test_str):
        return ""

    # Convert to string and strip to avoid AttributeError
    test_str = str(test_str).strip()  # Convert to string before stripping
    test_str = test_str.replace(' .', '.').replace('. ', '.')

    # Match the regex pattern
    match = temp_string_re.match(test_str)

    if not match:  # If no match, return an empty string
        return ""

    res = match.groups()  # Extract groups from the regex match
    list_breakdown = list(res)

    # Check for 'nan' in the list
    if 'nan' in list_breakdown:
        return ""

    # Process logic based on your original code
    # Process 'ghar', 'pass', 'paas' logic
    if 'ghar' in list_breakdown or ('pass' in list_breakdown or 'paas' in list_breakdown):
        if 'bilkul' in list_breakdown or 'lake' in list_breakdown or 'neeche' in list_breakdown or 'niche' in list_breakdown or 'building' in list_breakdown:
            return float(0.5)
        else:
            return float(0.5)

    # Processing based on unit and other conditions
    unit = list_breakdown[8]

    try:
        min_dist = float(list_breakdown[1])
    except ValueError:
        min_dist = list_breakdown[1]

    try:
        max_dist = float(list_breakdown[6])
    except ValueError:
        max_dist = list_breakdown[6]

    first_string = list_breakdown[0]

    try:
        last_string = float(list_breakdown[11])
    except ValueError:
        last_string = list_breakdown[11]

    # Handling based on unit and other logic
    if unit == '':
        return ""

    if unit in ['wk', 'week', 'wks', 'weeks']:
        if isinstance(max_dist, (int, float)) and isinstance(min_dist, (int, float)):
            return float((min_dist + max_dist) / 2.0) * 24.0 * 7
        elif isinstance(max_dist, (int, float)):
            max_dist = float(max_dist) * 24.0 * 7
            return max_dist
        elif isinstance(min_dist, (int, float)):
            min_dist = float(min_dist) * 24.0 * 7
            return min_dist

    # Handling other units like 'hr', 'minute', 'day', etc.
    if unit in ['hr', 'hours', 'hour', 'hrs']:
        if isinstance(max_dist, (int, float)) and isinstance(min_dist, (int, float)):
            return float((min_dist + max_dist) / 2.0)

    # Handling minutes and other cases
    if unit in ['minute', 'min', 'minutes', 'mints', 'minut', 'mint']:
        if isinstance(min_dist, (int, float)) and isinstance(max_dist, (int, float)):
            max_dist = (min_dist + max_dist) / 2.0 - 1
            max_dist = np.floor((max_dist / 30.0 + 1)) / 2
            return max_dist

    # Handle cases with day unit
    if unit in ['day', 'days','din']:
        if isinstance(min_dist, (int, float)) and isinstance(max_dist, (int, float)):
            return 24.0 * ((min_dist + max_dist) / 2.0)

    # If unit is missing, check other conditions
    if max_dist != '' and min_dist != '':
        if isinstance(min_dist, (int, float)) and isinstance(max_dist, (int, float)):
            return round((max_dist + min_dist) / 2.0, 2)

    return ""

# Apply the function to the DataFrame columns
df['6.2 How much time the PGM took to service your vehicle?'] = df['6.2 How much time the PGM took to service your vehicle?'].apply(get_distance_metric_Q6)
df['6.3 And how much time TVS workshop guy took to service your vehicle?'] = df['6.3 And how much time TVS workshop guy took to service your vehicle?'].apply(get_distance_metric_Q6)
df['6.4 What was the waiting time in PGM when you arrived ?'] = df['6.4 What was the waiting time in PGM when you arrived ?'].apply(get_distance_metric_Q6)
df['6.5 In TVSm WS, what was the waiting time before you were attended?'] = df['6.5 In TVSm WS, what was the waiting time before you were attended?'].apply(get_distance_metric_Q6)
df['6.6 How much time would you prefer for Servicing your vehicle?'] = df['6.6 How much time would you prefer for Servicing your vehicle?'].apply(get_distance_metric_Q6)

# Save the resulting DataFrame to an Excel file
file_name = 'Q_6.xlsx'
df.to_excel(file_name)

print("Processing successful!")
