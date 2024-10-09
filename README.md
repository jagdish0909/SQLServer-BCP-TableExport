# bcp_with_python
Export SQL Server tables from list from databases dynamically with human intervention in the code.

BCP stands for Bulk copy program. this is Micorsoft utility which is build for expoirting and importing data in sql server parallelly.


# SQL Server Table Export Script

## Overview

This Python script connects to a SQL Server instance, retrieves metadata information about the available databases and tables, and exports the tables into CSV files using the `BCP` (Bulk Copy Program) utility.

## Prerequisites

To use this script, ensure that the following prerequisites are met:

- **Python Version**: Python 3.x
- **Python Libraries**:
  - `pyodbc`: For connecting to SQL Server databases.
  - `pandas`: For data manipulation and handling SQL query results.
  - `subprocess`: For running system commands (used for executing `BCP`).
  - `datetime`: For generating date-based filenames.

You can install the required libraries using the following command:

```bash
pip install pyodbc pandas
```

**SQL Server**: SQL Server must be running and accessible with appropriate credentials.

**BCP Utility**: The BCP utility must be installed and available in the system's PATH. You can download it from the official Microsoft site or as part of SQL Server tools.

# Configuration
Before running the script, you need to configure the following variables within the script:

**servername:** The hostname or IP address of your SQL Server instance.
**userid:** The username to connect to SQL Server.
**password:** The password for the SQL Server connection.
**databasename:** The default database for the initial connection (set to master).

```bash
servername = "hostname"
userid = "Admin"
password = "yourpassword"
databasename = "master"
```

