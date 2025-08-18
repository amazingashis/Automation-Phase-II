"""
Test script for ingest.py
Test the parsing functions with actual files in the workspace
"""
import sys
import os
sys.path.append('.')
from ingest import load_data_table, parse_data_dict, parse_domain_model

def test_ingest():
    # Define file paths relative to project root
    data_file = "../source_file/member_enrollment_file.csv"
    data_dict_file = "../data_dict/member eligibility data dictitonary.xlsx"
    domain_model_file = "../domain_model/Domain Model Eligibility.xlsx"
    
    print("=== Testing ingest.py functions ===\n")
    
    # Test data table loading
    try:
        print("1. Loading data table...")
        data = load_data_table(data_file)
        print(f"Data table shape: {data.shape}")
        print("First 5 rows:")
        print(data.head())
        print(f"Columns: {list(data.columns)}")
        print()
    except Exception as e:
        print(f"Error loading data table: {e}")
        print()
    
    # Test data dictionary parsing
    try:
        print("2. Parsing data dictionary...")
        data_dict = parse_data_dict(data_dict_file)
        print(f"Data dictionary shape: {data_dict.shape}")
        print("Data dictionary content:")
        print(data_dict)
        print()
    except Exception as e:
        print(f"Error parsing data dictionary: {e}")
        print()
    
    # Test domain model parsing
    try:
        print("3. Parsing domain model...")
        domain_model = parse_domain_model(domain_model_file)
        print(f"Domain model shape: {domain_model.shape}")
        print("Domain model content:")
        print(domain_model)
        print()
    except Exception as e:
        print(f"Error parsing domain model: {e}")
        print()

if __name__ == "__main__":
    test_ingest()
