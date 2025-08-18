"""
main.py
Entry point for the Databricks SQL code generation pipeline.
Connects to LM Studio, takes input files, and orchestrates the workflow.
"""

from ingest import load_data_table, parse_data_dict, parse_domain_model
from rag_index import RAGIndex
from llm_orchestrator import LLMOrchestrator
from sql_generator import SQLGenerator
from notebook_builder import build_notebook


def main():


    # Hardcoded file paths
    data_path = '../source_file/member_enrollment_file.csv'
    data_dict_path = '../data_dict/member eligibility data dictitonary.xlsx'
    domain_model_path = '../domain_model/Domain Model Eligibility.xlsx'
    output_path = '../output/databricks_notebook.ipynb'

    # Static LM Studio URL
    lmstudio_url = 'http://localhost:1234/v1/completions'
    
    print("Using hardcoded file paths:")
    print(f"Data table: {data_path}")
    print(f"Data dictionary: {data_dict_path}")
    print(f"Domain model: {domain_model_path}")
    print(f"Output: {output_path}")
    print()

    # Load and normalize files
    data = load_data_table(data_path)
    data_dict_df = parse_data_dict(data_dict_path)
    domain_model_df = parse_domain_model(domain_model_path)

    # Prepare RAG context
    rag_index = RAGIndex(data_dict_df, domain_model_df)

    # Connect to LLM via LM Studio
    orchestrator = LLMOrchestrator(rag_index, model_path=lmstudio_url)
    sql_gen = SQLGenerator(orchestrator)


    # Generate SQL scripts in smaller sections, including import
    print("Generating SQL scripts...")
    import_script = sql_gen.generate_import_script()
    create_table_sql = sql_gen.generate_create_table_sql()
    basic_transform_sql = sql_gen.generate_basic_transformation_sql()
    data_conversion_sql = sql_gen.generate_data_type_conversion_sql()
    business_logic_sql = sql_gen.generate_business_logic_sql()
    final_insert_sql = sql_gen.generate_final_insert_sql()
    unload_sql = sql_gen.generate_unload_sql()

    # Build notebook with all SQL sections, import first
    sql_scripts = [
        import_script,
        create_table_sql,
        basic_transform_sql, 
        data_conversion_sql,
        business_logic_sql,
        final_insert_sql,
        unload_sql
    ]
    build_notebook(sql_scripts, output_path)
    print(f"Notebook generated at {output_path}")

if __name__ == "__main__":
    main()
