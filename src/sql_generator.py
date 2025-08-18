"""
Module: sql_generator.py
Purpose: Generate SQL scripts for transformation and unloading using LLM.
"""
from llm_orchestrator import LLMOrchestrator


class SQLGenerator:
    def generate_import_script(self) -> str:
        prompt = (
            "Write a PySpark script to import/load a CSV file containing healthcare member eligibility data into a DataFrame, "
            "and then save it as a Delta table named 'source.healthcare_data'. Assume the file is available at 'dbfs:/FileStore/member_enrollment_file.csv'. "
            "Include schema inference and header handling."
        )
        return self.orchestrator.generate_sql(prompt, sql_type="PySpark Import Script")
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator

    def generate_create_table_sql(self) -> str:
        prompt = "Write a Databricks SQL CREATE TABLE statement for the target domain model schema. Only create the table structure, no data insertion."
        return self.orchestrator.generate_sql(prompt, sql_type="CREATE TABLE SQL")

    def generate_basic_transformation_sql(self) -> str:
        prompt = "Write a Databricks SQL script to do basic column mapping and renaming from source to target schema. Focus only on direct column mappings without complex business logic."
        return self.orchestrator.generate_sql(prompt, sql_type="Basic Transformation SQL")

    def generate_data_type_conversion_sql(self) -> str:
        prompt = "Write a Databricks SQL script to handle data type conversions (dates, strings, integers) for the healthcare data transformation."
        return self.orchestrator.generate_sql(prompt, sql_type="Data Type Conversion SQL")

    def generate_business_logic_sql(self) -> str:
        prompt = "Write a Databricks SQL script to apply business logic transformations like CASE statements, conditional mappings, and calculated fields."
        return self.orchestrator.generate_sql(prompt, sql_type="Business Logic SQL")

    def generate_final_insert_sql(self) -> str:
        prompt = "Write a Databricks SQL INSERT statement to populate the target table with the transformed data from previous steps."
        return self.orchestrator.generate_sql(prompt, sql_type="Final Insert SQL")

    def generate_unload_sql(self) -> str:
        prompt = "Write a Databricks SQL script to unload/export the transformed data to a file or external location."
        return self.orchestrator.generate_sql(prompt, sql_type="Unload SQL")
