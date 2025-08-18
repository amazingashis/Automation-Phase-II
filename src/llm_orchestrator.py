"""
Module: llm_orchestrator.py
Purpose: Orchestrate LLM calls with RAG context to generate SQL code.
"""

import requests

class LLMOrchestrator:
    def __init__(self, rag_index, model_path: str):
        self.rag_index = rag_index
        self.model_path = model_path  # LM Studio API URL

    def generate_sql(self, user_prompt: str, sql_type: str = "SQL") -> str:
        """
        Call LM Studio API with RAG context and user prompt to generate SQL.
        sql_type: A short description of the SQL being generated (for logging).
        """
        context = self.rag_index.get_context()
        full_prompt = f"""
You are an expert in Databricks SQL and US healthcare data.

Context:
{context}

Task: {user_prompt}

Generate only the SQL code without explanations or comments.
"""
        # Call LM Studio API
        try:
            print(f"[LLM] Generating {sql_type}... Calling LM Studio API...")
            response = requests.post(
                self.model_path,
                json={
                    "prompt": full_prompt,
                    "max_tokens": 1024,
                    "temperature": 0.2
                },
                timeout=300  # 5 minutes timeout
            )
            if response.status_code == 200:
                result = response.json().get("choices", [{}])[0].get("text", "-- No SQL generated.")
                print(f"✅ {sql_type} generated successfully")
                return result
            else:
                print(f"❌ LLM API error while generating {sql_type}: {response.status_code}")
                return f"-- LLM API error: {response.status_code}"
        except requests.exceptions.Timeout:
            print(f"⏱️ API call timed out while generating {sql_type}")
            return f"-- LLM API call timed out"
        except Exception as e:
            print(f"❌ API call failed while generating {sql_type}: {e}")
            return f"-- LLM API call failed: {e}"
