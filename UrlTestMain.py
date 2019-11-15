from sqlitedb import sqliteDBUtility
from urltesting import urlTesting
from enum import Enum
import os

class ACTIONS(Enum):
    URL_TESTING = 0
    DELETE_DB = 1
    VIEW_DB = 2
    LIST_URL = 3
    EXIT = 4

if __name__ == '__main__':
    project_root = os.getcwd()
    url_file = project_root + '/' + 'url.txt'
    db_file = project_root + '/' + 'urltestresult.db'
    print('current Dir:',project_root)
    #creating sqlite database
    sqliteConnection = sqliteDBUtility.create_connection(db_file)
    #create table with db connection
    sqliteDBUtility.create_table(sqliteConnection)
    regex_patterns = [
        r'\b((http|https):\/\/?)[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|\/?))',
        r'(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.#?&//=]*)',
        r'\.com',
        r'\.fi']
    while True:
        select = int(input("Select the action to Perform \n"
                           "0      Perform Url Testing\n"
                           "1      Delete DataBase\n"
                           "2      View Records in DB\n"
                           "3      List Urls\n"
                           "4      Exit\n"))
        filename = ""
        if select == ACTIONS.URL_TESTING.value:
            urlTesting.url_test(sqliteConnection, regex_patterns,url_file)
        elif select == ACTIONS.DELETE_DB.value:
            urlTesting.delete_DB(sqliteConnection)
        elif select == ACTIONS.VIEW_DB.value:
            urlTesting.read_DB(sqliteConnection)
        elif select == ACTIONS.LIST_URL.value:
            urlTesting.read_urlFile(url_file)
        elif select == ACTIONS.EXIT.value:
            sqliteDBUtility.closeSqliteConnection(sqliteConnection)
            exit()
        else:
            print('Invalid Option selected exit()')
            sqliteDBUtility.closeSqliteConnection(sqliteConnection)
            exit()
