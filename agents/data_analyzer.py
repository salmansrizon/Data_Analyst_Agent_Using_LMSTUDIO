import pandas as pd


class DataAnalyzer:
    def __init__(self, model_name, base_url):
        self.model_name = model_name
        self.base_url = base_url

    def execute(self, df, context, metadata):
        prompt = (
            f"Analyze data:\n{df.head().to_string()}\n"
            f"Context: {context}\nMetadata: {metadata}"
        )
        analysis = self._call_llm(prompt)
        return analysis

    def _call_llm(self, prompt):
        # Simulated LLM analysis
        return "Analysis Report: Sales increased by 50% between dates..."
