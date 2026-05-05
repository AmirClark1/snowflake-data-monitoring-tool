# Snowflake Dynamic Table Failure Monitor

## Demo

Below is an example of the tool detecting a dynamic table failure:

![Demo Output](demo.png)


## Overview
This project is a Python + Snowpark application that connects to Snowflake and monitors dynamic table refresh failures.

It queries Snowflake ACCOUNT_USAGE views to detect failed refresh events and outputs structured alert-style results.

## Features
- Secure connection using environment variables
- Snowpark (Python) integration
- Querying Snowflake ACCOUNT_USAGE views
- Failure detection logic
- Offline/demo fallback when warehouse is unavailable
- Modular project structure
- Handles real-world constraints such as warehouse availability and resource limits

## Tech Stack
- Python
- Snowflake
- Snowpark
- SQL

## Project Structure



snowflake-dynamic-table-monitor/
├── main.py
├── config.py
├── queries.py
├── README.md
└── .gitignore


## Setup

### 1. Install dependencies
pip install snowflake-snowpark-python

### 2. Set environment variables (PowerShell)
$env:SNOWFLAKE_ACCOUNT="your_account"
$env:SNOWFLAKE_USER="your_user"
$env:SNOWFLAKE_PASSWORD="your_password"


### 3. Run the project
python main.py



## Example Output
Connected to Snowflake.
Found 1 dynamic table failure:
Table: DEV_DB.PUBLIC.TEST_TABLE
State: FAILED
Time: 2026-05-05 10:12:00



If warehouse credits are unavailable:
Warehouse unavailable - running in offline/demo mode.
Simulated output:



## Key Learning Outcomes
- Built secure Snowflake connections using environment variables
- Worked with Snowflake ACCOUNT_USAGE system views
- Implemented monitoring logic for data pipeline failures
- Handled real-world constraints (resource monitors / credit limits)

## Future Improvements
- Email alert integration
- Logging system
- Scheduled execution
- Dashboard/visualization

## Author
Amir Clark  (www.linkedin.com/in/amir-clark-a7127731b)  