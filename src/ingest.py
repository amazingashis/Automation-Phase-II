"""
Module: ingest.py
Purpose: Read and parse Data Dictionary and Domain Model Excel files, and load the data table.
"""
import pandas as pd


def load_data_table(path):
    """Load the raw data table (CSV)."""
    return pd.read_csv(path)

def parse_data_dict(path):
    """Parse and normalize the data dictionary Excel file."""
    df = pd.read_excel(path)
    # Clean column names
    df.columns = [c.strip() for c in df.columns]
    
    # Map actual columns to expected standardized names (like domain model)
    column_mapping = {
        'Column Name': 'column_name',
        'Data Type': 'data_type', 
        'Description': 'description',
        'Format': 'format',
        'Required': 'required',
        'Notes': 'notes'
    }
    
    # Rename columns using the mapping
    df = df.rename(columns=column_mapping)
    
    # Clean the data - remove rows where column_name is NaN or contains instructions
    if 'column_name' in df.columns:
        df = df.dropna(subset=['column_name'])
        # Remove instruction rows
        instruction_patterns = ['instruction', 'this table', 'all fields', 'for actual', 'note:', 'example']
        for pattern in instruction_patterns:
            df = df[~df['column_name'].astype(str).str.contains(pattern, case=False, na=False)]
    
    # Ensure we have the required columns
    required_cols = ['column_name', 'data_type', 'description']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing expected column '{col}' in data dictionary.")
    
    # Return all available columns, but ensure we have the core ones
    available_cols = [col for col in ['column_name', 'data_type', 'description', 'format', 'required', 'notes'] if col in df.columns]
    return df[available_cols]

def parse_domain_model(path):
    """Parse and normalize the domain model Excel file."""
    df = pd.read_excel(path)
    # Clean column names
    df.columns = [c.strip() for c in df.columns]
    
    # Map actual columns to expected standardized names
    column_mapping = {
        'Column Name': 'column_name',
        'Data Type': 'data_type', 
        'Description': 'description',
        'Allowed Values / Format': 'allowed_values',
        'Required': 'required',
        'Notes': 'notes'
    }
    
    # Rename columns using the mapping
    df = df.rename(columns=column_mapping)
    
    # Return all available columns, but ensure we have the core ones
    required_cols = ['column_name', 'data_type', 'description']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing expected column '{col}' in domain model.")
    
    return df
