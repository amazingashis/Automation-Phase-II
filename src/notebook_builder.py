"""
Module: notebook_builder.py
Purpose: Assemble SQL scripts and documentation into a Databricks-compatible notebook.
"""

import nbformat

def build_notebook(sql_scripts, output_path):
    nb = nbformat.v4.new_notebook()
    cells = []
    
    # Add a main title
    cells.append(nbformat.v4.new_markdown_cell("# Databricks Healthcare Data Transformation Notebook\nThis notebook was generated automatically with modular SQL scripts."))
    
    # Section titles for each SQL script
    section_titles = [
        "## Step 1: Create Target Table Schema",
        "## Step 2: Basic Column Mapping", 
        "## Step 3: Data Type Conversions",
        "## Step 4: Business Logic Transformations",
        "## Step 5: Insert Transformed Data",
        "## Step 6: Export/Unload Data"
    ]
    
    # Add SQL code cells with descriptive headers
    for i, script in enumerate(sql_scripts):
        if i < len(section_titles):
            cells.append(nbformat.v4.new_markdown_cell(section_titles[i]))
        
        # Databricks expects SQL cells to start with %%sql
        sql_cell = f"%%sql\n{script.strip()}"
        cells.append(nbformat.v4.new_code_cell(sql_cell))
    
    nb['cells'] = cells
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
