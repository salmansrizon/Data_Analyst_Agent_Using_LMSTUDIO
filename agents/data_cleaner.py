import pandas as pd
import requests
from utils.config_loader import load_llm_config


class DataCleaner:
    def __init__(self, model_name, base_url):
        self.model_name = model_name
        self.base_url = base_url
        self.llm_config = load_llm_config()

    def execute(self, df, context):
        """
        Clean the data and perform exploratory analysis using LM Studio.
        """
        # Basic data cleaning operations
        df = df.drop_duplicates()
        df = df.dropna()
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])

        # Generate EDA report using LM Studio
        prompt = (
            f"Perform exploratory data analysis (EDA) on the following dataset:\n"
            f"{df.head(5).to_string()}\n"
            f"Provide insights into trends, patterns, and anomalies.\n"
            f"Context: {context}\n"
            f"Instructions: Focus on statistical summaries, correlations, and actionable insights."
        )
        print("Generated Prompt:", prompt)  # Debugging output
        eda_report = self._call_lm(prompt)

        return df, eda_report

    def _call_lm(self, prompt):
        """
        Call the LM Studio API to generate a response based on the prompt.
        """
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.llm_config["model_name"],
            "prompt": prompt,  # Use "prompt" instead of "messages"
            "temperature": self.llm_config["temperature"],
            "max_tokens": self.llm_config["max_tokens"],
        }

        try:
            print("Sending API Request:", payload)  # Debugging output
            response = requests.post(
                self.llm_config["base_url"],
                json=payload,
                headers=headers,
                timeout=self.llm_config["timeout"],
            )
            response.raise_for_status()

            # Debugging: Print the full API response
            print("API Response:", response.json())

            # Extract the response content
            if "choices" in response.json() and len(response.json()["choices"]) > 0:
                return response.json()["choices"][0][
                    "text"
                ].strip()  # Use "text" instead of "message.content"
            else:
                return "No insights available from the LLM."
        except Exception as e:
            return f"Error: {str(e)}"
