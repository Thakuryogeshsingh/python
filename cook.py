import os
import pandas as pd
from tkinter import filedialog
import warnings

warnings.filterwarnings('ignore')

script_dir = os.path.dirname(os.path.abspath(__file__))

print("Import your dataset")
file_path = filedialog.askopenfilename(title='Select Dataset')
existing_dataset = pd.read_excel(file_path, header=0)

dealer_mapping_path = os.path.join(script_dir, 'Dealer Mapping.xlsx')
dealer_mapping_data = pd.read_excel(dealer_mapping_path)

merged_dataset = pd.merge(existing_dataset, dealer_mapping_data[['Dealer Code', 'TTY']], on='Dealer Code', how='left')

print(merged_dataset['Area'].unique())

for tty_value in merged_dataset['TTY_y'].unique():
    desired_rows_filtered = merged_dataset[merged_dataset['TTY_y'] == tty_value]

    numerical_cols = desired_rows_filtered.select_dtypes(include=['float', 'int']).columns
    for col in numerical_cols:
        median_non_null_rows = desired_rows_filtered[col].median()
        
        merged_dataset.loc[merged_dataset['TTY_y'] == tty_value, col] = merged_dataset.loc[merged_dataset['TTY_y'] == tty_value, col].fillna(median_non_null_rows)

merged_dataset.dropna(subset=['Dealer Code'], inplace=True)

output_file_path = os.path.join(script_dir, 'hey.xlsx')
merged_dataset.to_excel(output_file_path, index=False)

print("Process completed. Merged dataset saved to:", output_file_path)
