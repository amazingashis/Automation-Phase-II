"""
Check the actual structure of the data dictionary Excel file
"""
import pandas as pd

def check_data_dict_structure():
    data_dict_file = "../data_dict/member eligibility data dictitonary.xlsx"
    
    try:
        # Read the Excel file without any processing
        df = pd.read_excel(data_dict_file)
        print("Data Dictionary file structure:")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst 10 rows:")
        print(df.head(10))
        print("\nData types:")
        print(df.dtypes)
    except Exception as e:
        print(f"Error reading data dictionary: {e}")

if __name__ == "__main__":
    check_data_dict_structure()
