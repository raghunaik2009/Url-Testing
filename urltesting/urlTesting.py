# Python program to check URLs content by Regular Expressions
# Importing libraries and Notebook
import re
import sys, os
from datetime import datetime
from sqlitedb import sqliteDBUtility

class URL_Test():
    """ This class takes a configured grouped list of urls and regular expressions.
    The output results are saved into Sqlite DataBase.

    Example: We have a list of URL eg. www.yahoo.com and
    we run a regular expression eg. '\.com' that finds if
    the given URL is matched with the part '.com'. If it finds
    the match, it will write the SUCESS into the result column if doesn't
    match it will write Failed.
    Result format is
    (url, regex, timestamp, result)
    (google.com, \.com, Date: 14-11-2019 Time: 10:34:12:220233_PM, SUCESS)
    """

    def __init__(self, source_file, sqlite_connection, reg_ex=None):
        """Initializes the class with the parameters

        Args:
        source_file = Name of the file that has the lists of URLS
        sqlite_connection = Sqlite Connection Object
        reg_ex = regular expression
        """
        self.source_file = source_file
        self.sqlite_connection = sqlite_connection
        self.reg_ex = reg_ex

    def url_check(self):
        """ This function checks the list of URLs in according to
        the regular expressions passed in as parameters.
        """
        try:
            patterns = self.reg_ex
            # Reading the regular expressions
            for regex in patterns:
                pattern = re.compile(regex)
                timestamp = datetime.now().strftime("Date: %d-%m-%Y Time: %I:%M:%S:%f_%p")
                # Reading the Source/URL files
                urlList = [url.rstrip('\n') for url in open(self.source_file)]
                selected_urls = list(filter(pattern.match, urlList))
                urlresponseList = ['SUCESS' if url in selected_urls else 'FAILED' for url in urlList]
                timestampList = [timestamp] * len(urlresponseList)
                regexList = [regex] * len(urlresponseList)
                urlFinalResultList = list(zip(urlList, regexList, timestampList, urlresponseList))
                # Writing the result into database
                sqliteDBUtility.insertDataIntoTable(self.sqlite_connection, urlFinalResultList)
            print("Program executed successfully. ")
        except IOError:
            print('There was an error opening the file!')
            raise
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Exception has occured ', e)
            print("exec_type : % s, fname : % s, line no : % s" % (exc_type, fname, exc_tb.tb_lineno))
            raise

def url_test(sqliteConnection, regex_patterns, url_file):
    # Executing the program by class name and required arguments
    # Creating list of regular expressions
    URL_Test(url_file, sqliteConnection, regex_patterns).url_check()
    return True

def delete_DB(sqliteConnection):
    # Delete all Database records
    if not sqliteConnection:
        # creating sqlite database
        print('Creating DB Connection', sqliteConnection)
        sqliteConnection = sqliteDBUtility.create_connection('urltestresult.db')
    sqliteDBUtility.deleteSqliteRecord(sqliteConnection)

def read_DB(sqliteConnection):
    # Read all records
    if not sqliteConnection:
        # creating sqlite database
        sqliteConnection = sqliteDBUtility.create_connection('urltestresult.db')
    sqliteDBUtility.readSqliteTable(sqliteConnection)

def read_urlFile(url_file):
    urls = None
    try:
        with open(url_file, 'r') as file:
            urls = file.read()
            print(urls)
            file.close()
    except IOError:
        print('There was an error opening the file!')
        raise


