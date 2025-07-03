import streamlit as st
from agents.query_executor import QueryExecutor
from agents.data_analyzer import DataAnalyzer
from agents.data_cleaner import DataCleaner
from agents.visualizer import Visualizer
from utils.export_utils import save_to_csv, create_pptx
from utils.config_loader import load_llm_config, load_db_config


def main():
    st.title("AI Data Analyst")

    # Load configurations
    llm_config = load_llm_config()
    db_config = load_db_config()

    # Initialize agents
    query_agent = QueryExecutor(
        model_name=llm_config["model_name"], base_url=llm_config["base_url"]
    )
    cleaner = DataCleaner(
        model_name=llm_config["model_name"], base_url=llm_config["base_url"]
    )

    # User inputs
    query = st.text_area("Enter SQL Query:")
    context = st.text_area("Context:")
    metadata = st.text_area("Metadata:")
    export_button = st.button("Extract Analysis")

    if export_button and query:
        with st.spinner("Processing..."):
            try:
                # Execute query
                df = query_agent.execute(query)

                # Clean and analyze
                cleaned_df, eda = cleaner.execute(df, context)

                st.success("Analysis completed successfully!")
                st.write("EDA Report:")
                st.write(eda)
            except Exception as e:
                st.error(f"Pipeline failed: {str(e)}")


if __name__ == "__main__":
    main()
