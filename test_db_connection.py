from sqlalchemy import create_engine
from utils.config_loader import load_db_config


def test_db_connection():
    db_config = load_db_config()

    # Validate the database configuration
    if None in db_config.values():
        raise ValueError("Database configuration is incomplete or invalid.")

    # Create a SQLAlchemy engine for PostgreSQL connection
    connection_string = (
        f"postgresql://{db_config['username']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database_name']}"
    )
    print("Testing Connection String:", connection_string)

    try:
        engine = create_engine(connection_string)
        with engine.connect() as conn:
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {str(e)}")


if __name__ == "__main__":
    test_db_connection()
