import pandas as pd
from sqlalchemy import create_engine
from utils.config_loader import load_db_config


class QueryExecutor:
    def __init__(self, model_name, base_url):
        self.model_name = model_name
        self.base_url = base_url

    def execute(self, query):
        """
        Execute a SQL query on the PostgreSQL database and return the result as a pandas DataFrame.
        """
        db_config = load_db_config()

        # Validate the database configuration
        required_keys = ["username", "password", "host", "port", "database_name"]
        if any(key not in db_config or db_config[key] is None for key in required_keys):
            raise ValueError("Database configuration is incomplete or invalid.")

        # Create a SQLAlchemy engine for PostgreSQL connection
        connection_string = (
            f"postgresql://{db_config['username']}:{db_config['password']}"
            f"@{db_config['host']}:{db_config['port']}/{db_config['database_name']}"
        )
        print("Connection String:", connection_string)

        try:
            engine = create_engine(connection_string)
            df = pd.read_sql(query, engine)
            return df
        except Exception as e:
            raise ValueError(f"Failed to execute query: {str(e)}")
