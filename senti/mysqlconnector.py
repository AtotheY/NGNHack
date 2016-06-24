import pymysql
import logging
class MySQLConnector():
    def __init__(self, mid, mpwd, dbName='tweets', logger=None):
        self.mid = mid
        self.mpwd = mpwd
        self.dbconn = None
        self.cur = None
        self.db = dbName
        if logger is None:
            self.__logger = logging.getLogger()
        else:
            self.__logger = logger

    def connect(self):
        if self.dbconn == None:
            self.dbconn = pymysql.connect(host = "localhost",  user = self.mid, passwd = self.mpwd,db = self.db)
        self.cur = self.dbconn.cursor()
        return True

    def isConnected(self):
        if self.cur == None:
            return False

        try:
            self.cur.execute("SELECT VERSION()")
            rt = self.cur.fetchone()
            if rt:
                return True
            else:
                return False
        except pymysql.ProgrammingError, err:
            if err.message == "Cursor closed":
                return False
            else:
                raise Exception("Undefined problem")


if __name__ == "__main__":
    mySQLConnector = MySQLConnector('root', '.....1')
    mySQLConnector.connect()
    print mySQLConnector.isConnected()
