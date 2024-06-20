import re
from word2num import word2num
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# File selection with tkinter
file_path = filedialog.askopenfilename(title="Select a Dataset")
df = pd.read_excel(file_path, header=1)

## Charges(Money) cleaned:

def get_distance_metric_inr(test_str):
    temp_string_re = re.compile(r"([a-zA-Z]*)([0-9]*[\.]*[0-9]*)([ ]*)([-]*)([ ]*)([ ]*)([0-9]*[\.]*[0-9]*)([ ]*)([a-zA-Z]*)([ ]*)([a-zA-Z]*)")

    test_str = str(test_str).strip()
    test_str = test_str.replace(' .','.').replace('. ','.')
    res = temp_string_re.match(test_str).groups()
    list_breakdown = list(res)
    if 'nan' in list_breakdown:
        return ""
    
    try:
        min_dist = float(list_breakdown[1])
    except:
        min_dist = list_breakdown[1]
    try:
        max_dist = float(list_breakdown[6])
    except:
        max_dist = list_breakdown[6]

    if isinstance(min_dist, (int, float)) and isinstance(max_dist, (int, float)):
        return float((min_dist+max_dist)/2.0)
    elif isinstance(min_dist, (int, float)):
        min_dist = min_dist
        return float(min_dist)
    elif isinstance(max_dist, (int, float)):
        max_dist = max_dist
        return float(max_dist)
    
    
    return ''

## 

df['3.1 AS per you, how much is the PGMs charging for general service ?'] = df['3.1 AS per you, how much is the PGMs charging for general service ?'].apply(get_distance_metric_inr)
df['3.2 AS per you, how much is the TVSMs charging for general service ?'] = df['3.2 AS per you, how much is the TVSMs charging for general service ?'].apply(get_distance_metric_inr)
df['3.3 What was the labour charged in the last service at TVSM?'] = df['3.3 What was the labour charged in the last service at TVSM?'].apply(get_distance_metric_inr)
df['3.5 As per you what should be the avg cost of service excluding GST at TVSM?'] = df['3.5 As per you what should be the avg cost of service excluding GST at TVSM?'].apply(get_distance_metric_inr)

file_name = 'Q_3.xlsx'
df.to_excel(file_name)
print("Successful!")