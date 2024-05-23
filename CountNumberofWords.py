import pandas as pd 
import tkinter as tk
from tkinter import filedialog

file_path = filedialog.askopenfilename(title='Data')
print(file_path)
data = pd.read_excel(file_path, header=1)
# df = pd.DataFrame(data)

print(data)

data["Remark"] = data["new_remark"].apply(lambda n: len(n.split()))
print(data.head())
