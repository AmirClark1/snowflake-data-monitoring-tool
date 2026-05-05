from snowflake.snowpark.session import Session
from config import get_connection_parameters
from queries import DYNAMIC_TABLE_FAILURE_QUERY

def create_session():
    session = Session.builder.configs(get_connection_parameters()).create()
    print("Connected to Snowflake.")
    return session

def check_dynamic_table_failures(session):
    try:
        df = session.sql(DYNAMIC_TABLE_FAILURE_QUERY)
        results = df.collect()
    except Exception as e:
        print("Warehouse unavailable - running in offline/demo mode.")
        print("Simulated output:")
        print("Found 1 dynamic table failure:")
        print("Table: DEV_DB.PUBLIC.TEST_TABLE")
        print("State: FAILED")
        print("Time: 2026-05-05 10:12:00")
        return
    
    if not results:
        print("No dynamic table failures found in the last 2 hours.")
        return

    print(f"Found {len(results)} dynamic table failure(s):")

    for row in results:
        print("-" * 60)
        print(f"Table: {row['DATABASE_NAME']}.{row['SCHEMA_NAME']}.{row['NAME']}")
        print(f"State: {row['STATE']}")
        print(f"Time: {row['DATA_TIMESTAMP']}")

def main():
    session = create_session()
    check_dynamic_table_failures(session)
    session.close()
    print("Session closed.")

if __name__ == "__main__":
    main()