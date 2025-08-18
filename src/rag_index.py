"""
Module: rag_index.py
Purpose: Build and query a semantic index for RAG using Data Dictionary and Domain Model.
"""

from typing import List
import pandas as pd

class RAGIndex:
    def __init__(self, data_dict_df, domain_model_df):
        """
        Store normalized data dictionary and domain model DataFrames for context retrieval.
        """
        self.data_dict_df = data_dict_df
        self.domain_model_df = domain_model_df

    def get_context(self) -> str:
        """
        Return a concise string context for LLM prompt, combining data dictionary and domain model.
        """
        context = []
        
        # Source Data Dictionary (first 20 most important columns)
        context.append('SOURCE DATA COLUMNS (sample):')
        source_sample = self.data_dict_df.head(20)[['column_name', 'data_type', 'description']]
        for _, row in source_sample.iterrows():
            context.append(f"- {row['column_name']} ({row['data_type']}): {row['description']}")
        
        context.append('\nTARGET DOMAIN MODEL:')
        # Domain Model (all columns since it's smaller)
        for _, row in self.domain_model_df.iterrows():
            if pd.notna(row['column_name']) and row['column_name'] != 'Attribute':
                required = f" [Required: {row.get('required', 'N/A')}]" if 'required' in row else ""
                context.append(f"- {row['column_name']} ({row['data_type']}): {row['description']}{required}")
        
        context.append('\nTASK: Transform source data to match target domain model schema.')
        
        return '\n'.join(context)
