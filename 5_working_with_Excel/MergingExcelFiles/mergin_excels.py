import pandas as pd
import os

### 1
data_dir = os.walk('excels')

file_path = []
for root, dir, files in data_dir:
    print(root, dir, files)
    for file in files:
        file_path.append(os.path.join(root, file))

print(file_path)

dataframe = [pd.read_excel(filepath) for filepath in file_path]

merged_df = pd.concat(dataframe, ignore_index=True)
merged_df.to_excel('merged.xlsx', index=False)


### 2
# Directory where the Excel files are located
directory = 'excel'

# Get filenames of Excel files for 2025 and 2024
filenames_2025 = [f for f in os.listdir(directory) if '2025' in f]
filenames_2024 = [f for f in os.listdir(directory) if '2024' in f]

# File paths for each year
filepaths_2025 = [os.path.join(directory, filename) for filename in filenames_2025]
filepaths_2024 = [os.path.join(directory, filename) for filename in filenames_2024]

# Read and merge DataFrames for 2024
dataframes_2024 = [pd.read_excel(filepath) for filepath in filepaths_2024]
merged_df_2024 = pd.concat(dataframes_2024, ignore_index=True)
output_file_path_2024 = os.path.join(directory, '2024.xlsx')
merged_df_2024.to_excel(output_file_path_2024, index=False)

# Read and merge DataFrames for 2025
dataframes_2025 = [pd.read_excel(filepath) for filepath in filepaths_2025]
merged_df_2025 = pd.concat(dataframes_2025, ignore_index=True)
output_file_path_2025 = os.path.join(directory, '2025.xlsx')
merged_df_2025.to_excel(output_file_path_2025, index=False)