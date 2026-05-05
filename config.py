import os

def get_connection_parameters():
    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": "ACCOUNTADMIN",
        "warehouse": "COMPUTE_WH",
        "database": "DEV_DB",
        "schema": "PUBLIC"
    }

    missing = [key for key, value in connection_parameters.items() if not value]
    if missing:
        raise ValueError(f"Missing connection values: {missing}")

    return connection_parameters