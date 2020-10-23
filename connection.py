import pymysql 
from config import DATABASE

def get_connection(db):
    return pymysql.connect(
        user = db['user'],
        password = db['password'],
        host = db['host'],
        port = db['port'],
        database = db['database'],
        cursorclass = pymysql.cursors.DictCursor,
    )
