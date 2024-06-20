import re
from word2num import word2num
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# File selection with tkinter
file_path = filedialog.askopenfilename(title="Select a Dataset")
df = pd.read_excel(file_path, header=1)

# Compiled regex with proper escaping
temp_string_re = re.compile(r"([a-zA-Z]*)([0-9]*[\.]*[0-9]*)([ ]*)([-]*)([ ]*)([ ]*)([0-9]*[\.]*[0-9]*)([ ]*)([a-zA-Z]*)([ ]*)([a-zA-Z]*)")

# Function to get distance metric
def get_distance_metric(test_str):
    # Convert to string and handle potential None or NaN inputs
    if pd.isna(test_str):  # Handle NaN inputs
        return ""  # Return a default value if necessary

    test_str = str(test_str).strip()  # Convert to string and strip
    test_str = test_str.replace(' .', '.').replace('. ', '.')

    # Check if the regex matches
    match = temp_string_re.match(test_str)
    
    if not match:  # If there's no match, return a default value
        return ""

    res = match.groups()
    list_breakdown = list(res)

    if 'nan' in list_breakdown:
        return ""

    if 'ghar' in list_breakdown or ('pass' in list_breakdown or 'paas' in list_breakdown):
        if 'bilkul' in list_breakdown or 'lake' in list_breakdown or 'neeche' in list_breakdown or 'niche' in list_breakdown or 'building' in list_breakdown:
            return 0.5  # Float conversion not required if already float
        else:
            return 0.5

    unit = list_breakdown[8]

    # Ensure all conversions are float where possible
    try:
        min_dist = float(list_breakdown[1])
    except ValueError:
        min_dist = list_breakdown[1]
    
    try:
        max_dist = float(list_breakdown[6])
    except ValueError:
        max_dist = list_breakdown[6]

    first_string = list_breakdown[0]

    if unit == '':
        if isinstance(max_dist, (int, float)) and isinstance(min_dist, (int, float)):
            if max_dist >= 90 or min_dist >= 90:
                return round((max_dist + min_dist) / 2000.0, 2)
            elif max_dist <= 40 or min_dist <= 40:
                return round((max_dist + min_dist) / 2.0, 2)
        elif isinstance(max_dist, (int, float)) and max_dist >= 90:
            return round(max_dist / 1000.0, 2)
        elif isinstance(min_dist, (int, float)) and min_dist >= 90:
            return round(min_dist / 1000.0, 2)
        elif isinstance(max_dist, (int, float)) and max_dist <= 40:
            return max_dist
        elif isinstance(min_dist, (int, float)) and min_dist <= 40:
            return min_dist

    if unit in ['m', 'meter', 'mtr', 'metre', 'mt', 'metres', 'meters']:
        if isinstance(max_dist, (int, float)) and isinstance(min_dist, (int, float)):
            return round((min_dist + max_dist) / 2000.0, 2)
        elif isinstance(max_dist, (int, float)):
            max_dist = round(max_dist / 1000.0, 2)
            return max_dist
        elif isinstance(min_dist, (int, float)):
            min_dist = round(min_dist / 1000.0, 2)
            return min_dist
        elif first_string != '' and isinstance(word2num(first_string), (int, float)):
            return round(word2num(first_string) / 1000.0, 2)
        elif first_string == '':
            return 1.0

    if unit in ['km', 'kilometer', 'kilometers', 'kms']:
        if isinstance(min_dist, (int, float)) and isinstance(max_dist, (int, float)):
            return round((min_dist + max_dist) / 2.0, 2)
        elif isinstance(min_dist, (int, float)):
            return min_dist
        elif isinstance(max_dist, (int, float)):
            return max_dist
        elif first_string != '' and isinstance(word2num(first_string), (int, float)):
            return word2num(first_string)

    if max_dist != '' and min_dist != '':
        if isinstance(min_dist, (int, float)) and isinstance(max_dist, (int, float)):
            if max_dist >= 90 or min_dist >= 90:
                return round((max_dist + min_dist) / 2000.0, 2)
            elif max_dist <= 40 or min_dist <= 40:
                return round((max_dist + max_dist) / 2.0, 2)
    elif max_dist != '' and isinstance(max_dist, (int, float)):
        return max_dist
    elif min_dist != '' and isinstance(min_dist, (int, float)):
        return min_dist

    return ""

# Apply the function to the specified DataFrame column
df['4.1 What is the distance(KM) from your residence  to the garage where you get your vehicle serviced? (Approximate KM)'] = df['4.1 What is the distance(KM) from your residence  to the garage where you get your vehicle serviced? (Approximate KM)'].apply(get_distance_metric)
df['4.2 What is the distance(KM) from your residence  to Authorised TVSM service centre? (Approximate KM)'] = df['4.2 What is the distance(KM) from your residence  to Authorised TVSM service centre? (Approximate KM)'].apply(get_distance_metric)
df['4.3 What is the distance(KM) from your office to Authorised TVSM service centre? (Approximate KM)'] = df['4.3 What is the distance(KM) from your office to Authorised TVSM service centre? (Approximate KM)'].apply(get_distance_metric)
df['4.6 As per you what should be the distance between TVSM workshop and your place so that it will be convenient for you to come for service (Approximate KM)'] = df['4.6 As per you what should be the distance between TVSM workshop and your place so that it will be convenient for you to come for service (Approximate KM)'].apply(get_distance_metric)

df['13.1 Can you pls tell us how far is the current TVSM AMD/AD WS from your place'] = df['13.1 Can you pls tell us how far is the current TVSM AMD/AD WS from your place'].apply(get_distance_metric)
df['13.2 As per you what should be the distance between TVSM workshop and your place so that it will be convenient for you to come for service (Approximate KM)'] = df['13.2 As per you what should be the distance between TVSM workshop and your place so that it will be convenient for you to come for service (Approximate KM)'].apply(get_distance_metric)
# Check the results
# print("Processed Data:")
print(df.head())

file_name = 'df2.xlsx'
df.to_excel(file_name)
print("Successful!")