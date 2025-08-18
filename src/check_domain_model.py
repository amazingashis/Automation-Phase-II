"""
Check the actual structure of the domain model Excel file
"""
import pandas as pd

def check_domain_model_structure():
    domain_model_file = "../domain_model/Domain Model Eligibility.xlsx"
    
    try:
        # Read the Excel file without any processing
        df = pd.read_excel(domain_model_file)
        print("Domain Model file structure:")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst 10 rows:")
        print(df.head(10))
        print("\nData types:")
        print(df.dtypes)
    except Exception as e:
        print(f"Error reading domain model: {e}")

if __name__ == "__main__":
    check_domain_model_structure()
