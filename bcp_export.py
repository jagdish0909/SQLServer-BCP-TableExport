import pyodbc
import pandas as pd
import subprocess
import datetime

servername = "hostname"
userid = "Admin"
password = "yourpassword"
databasename = "master"
conn = pyodbc.connect('Driver={SQL Server};Server='+servername+  ';UID='+userid+';PWD='+password+';Database='+databasename) 
SQL_DB = pd.read_sql_query('''select name from [servername].[databasename].dbo.dbnames''',conn)

def getRoster():
    conn = pyodbc.connect('Driver={SQL Server};Server='+servername+  ';UID='+userid+';PWD='+password+';Database='+databasename)
    sql = '''select TABLE_SCHEMA as schema_name,TABLE_NAME as table_name,TABLE_SCHEMA +'.'+ TABLE_NAME as fultblname from INFORMATION_SCHEMA.TABLES'''
    roster = pd.read_sql(sql,conn)

def gettables(dbname):
    conn = pyodbc.connect('Driver={SQL Server};Server='+servername+  ';UID='+userid+';PWD='+password+';Database='+databasename)
    exportsql = '''select TABLE_SCHEMA as schema_name,TABLE_NAME as table_name,TABLE_SCHEMA +'.'+ TABLE_NAME as fultblname from {}.INFORMATION_SCHEMA.TABLES'''.format(dbname)
    gettable = pd.read_sql(exportsql,conn)
    print(gettable)


def ExportTables():
    now = datetime.datetime.now()
    getRoster()
    for dbrow in SQL_DB.itertuples():
        database = dbrow.name
        gettables(dbrow.name)
        SQL_Query = pd.read_sql_query('''select TABLE_SCHEMA as schema_name,TABLE_NAME as table_name,TABLE_SCHEMA +'.'+ TABLE_NAME as fultblname from {}.INFORMATION_SCHEMA.TABLES'''.format(database), conn)
        for row in SQL_Query.itertuples():
            SQL = row.fultblname
            filename = 'C:\\Users\\bcpexport\\{}_{}_{}.csv'.format(database,SQL, now.strftime("%Y-%m-%d"))
            command = 'BCP "{}" out "{}" -t|| -c -C65001 -S {} -d {} -U {} -P {} -r 0x0a'.format(SQL,filename,servername,database,username,password)
            print (command)
            subprocess.run(command)

def main():	
    databasename = "KESSQLINFA"
    conn = pyodbc.connect('Driver={SQL Server};Server='+servername+  ';UID='+userid+';PWD='+password+';Database='+databasename) 
    print(ExportTables())

if __name__ == "__main__":
    main()