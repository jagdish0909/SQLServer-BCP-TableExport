# SQL Server Database Exporter

This Python script allows you to export tables from a SQL Server database to CSV files using the `BCP` (Bulk Copy Program) utility. The script connects to a SQL Server instance, retrieves the list of tables from specified databases, and exports each table to a CSV file.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed on your machine.
2. **pyodbc** library installed. You can install it using pip:
   ```bash
   pip install pyodbc
3. pandas library installed. You can install it using pip:
   ```bash
   pip install pandas
4. BCP utility installed and accessible from the command line. BCP is typically included with SQL Server installations
   
## Configuration
Before running the script, you need to configure the following variables in the script:
  **servername:** The hostname or IP address of your SQL Server instance.
  **userid:** The username for SQL Server authentication.
  **password:** The password for SQL Server authentication.
  **databasename:** The name of the database you want to connect to initially.

## Functions
  **getRoster()**
  This function retrieves the list of tables from the INFORMATION_SCHEMA.TABLES view for the specified database.

**gettables(dbname)**
  This function retrieves the list of tables from the INFORMATION_SCHEMA.TABLES view for a given database (dbname).

## ExportTables()
  This function exports all tables from the databases listed in the SQL_DB DataFrame to CSV files. The CSV files are saved in the
       C:\\Users\\bcpexport\\ directory with filenames in the format {database}_{schema_table}_{date}.csv.
  
  main()
  The main function that initializes the connection to the SQL Server and calls the ExportTables() function.

## Usage
  1. Clone the repository or download the script.
  2. Configure the script with your SQL Server credentials and database details.
  3. Run the script using Python:
       ```bash
         python script_name.py
  4. The script will export all tables from the specified databases to CSV files in the C:\\Users\\bcpexport\\ directory.

## Example
  1. servername = "your_server_name"
  2. userid = "your_username"
  3. password = "your_password"
  4. databasename = "your_database_name"

## Output
The script will generate CSV files for each table in the specified databases. The filenames will follow the format:
  C:\Users\bcpexport\{database}_{schema_table}_{date}.csv

## Notes
  Ensure that the BCP utility is properly configured and accessible from the command line.
  The script uses SQL Server authentication. If you are using Windows Authentication, you may need to modify the connection string.
  The script assumes that the INFORMATION_SCHEMA.TABLES view is accessible and contains the necessary table information.
