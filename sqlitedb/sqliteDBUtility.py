# sqlite3 database utility to store the data
# Importing libraries
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        raise
    return conn

def create_table(sqliteConnection):
    """
    Create a new project into the URLTest table
    :param conn:
    """
    try:
        sql = """CREATE TABLE IF NOT EXISTS URLTest
                 (url, regex, timestamp, result)"""
        curser = sqliteConnection.cursor()
        curser.execute(sql)
        curser.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
        raise
    except Exception as error:
        print(type(error))
        raise
    return True

def insertDataIntoTable(sqliteConnection, records):
    """ Insert data into database table URLTest.db """
    try:
        cursor = sqliteConnection.cursor()
        cursor.executemany('INSERT INTO urltest VALUES(?,?,?,?);',records)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
        raise
    except Exception as error:
        print(type(error))
        raise
    return True

def readSqliteTable(sqliteConnection):
    """ Read all table records """
    try:
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from urltest"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each record")
        for row in records:
            print('URL: {} regex: {} timestamp: {} result: {}'.format(row[0], row[1], row[2], row[3]))
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        raise
    except Exception as error:
        print(type(error))
        raise
    return True

def readSqliteTablebasedOnURL(sqliteConnection, url):
    """ Read records based on url"""
    try:
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from urltest where url = ?"""
        cursor.execute(sqlite_select_query, (url,))
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each record")
        for row in records:
            print('URL: {} regex: {} timestamp: {} result: {}'.format(row[0], row[1], row[2], row[3]))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        raise
    except Exception as error:
        print(type(error))
        raise
    return True

def deleteSqliteRecord(sqliteConnection):
    """ Delete all the records"""
    try:
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """DELETE from urltest"""
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record deleted successfully")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
        raise
    except Exception as error:
        print(type(error))
        raise
    return True

def closeSqliteConnection(sqliteConnection):
    """ Close DB Connection"""
    try:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
        raise
    except Exception as error:
        print(type(error))
        raise
    return True
