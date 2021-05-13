import pymysql
from ATM_CONTROLLER import DB

curs = ""
def db (host, user, password, db, port, charset= 'utf8'):
    global curs
    conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset)
    curs = conn.cursor()

def select_pin(collom_name, table_name, condition):
    global curs
    query = "select %s from %s" % (collom_name, table_name) #사용자 작성 쿼리문
    curs.execute(query)
    print(curs.fetchall())

Developer_db = DB() #연결하는 생성자 생성
Developer_db.db_connect(db, "localhost", "root", "asd", "study", 3306, "utf8")
Developer_db.select_connect(select_pin,"*" , "study_test")

Developer_db.connect()
Developer_db.select()

