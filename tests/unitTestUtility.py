# Python program to check URLs content by Regular Expressions
# Importing libraries and Notebook
import unittest
from urltesting import urlTesting
from sqlitedb import sqliteDBUtility
import os

class TestUrlTestMethods(unittest.TestCase):
    project_root = os.path.dirname(os.path.dirname(__file__))
    url_file = project_root + '/' + 'url.txt'
    db_file = project_root + '/' + 'urltestresult.db'

    def test_url(self):
        regex_patterns = [
            r'\b((http|https):\/\/?)[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|\/?))'
        ]
        # creating sqlite database
        sqliteConnection = sqliteDBUtility.create_connection(self.db_file)
        # create table with db connection
        sqliteDBUtility.create_table(sqliteConnection)
        self.assertTrue(urlTesting.url_test(sqliteConnection, regex_patterns,self.url_file))
        sqliteDBUtility.closeSqliteConnection(sqliteConnection)

    def test_dbconnect(self):
        # creating sqlite database
        sqliteConnection = sqliteDBUtility.create_connection(self.db_file)
        # create table with db connection
        self.assertNotEqual(sqliteDBUtility.create_connection(self.db_file), None)
        sqliteDBUtility.closeSqliteConnection(sqliteConnection)

    def test_deleterecord(self):
        # creating sqlite database
        sqliteConnection = sqliteDBUtility.create_connection(self.db_file)
        # create table with db connection
        self.assertTrue(sqliteDBUtility.deleteSqliteRecord(sqliteConnection))
        sqliteDBUtility.closeSqliteConnection(sqliteConnection)

    def test_viewrecord(self):
        # creating sqlite database
        sqliteConnection = sqliteDBUtility.create_connection(self.db_file)
        # create table with db connection
        self.assertTrue(sqliteDBUtility.readSqliteTable(sqliteConnection))
        sqliteDBUtility.closeSqliteConnection(sqliteConnection)

    def test_closedbconnection(self):
        # creating sqlite database
        sqliteConnection = sqliteDBUtility.create_connection(self.db_file)
        # create table with db connection
        self.assertTrue(sqliteDBUtility.closeSqliteConnection(sqliteConnection))

if __name__ == '__main__':
    unittest.main()