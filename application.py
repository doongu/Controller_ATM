from ATM_CONTROLLER import conn_db
import pymysql

#나는 몽고인지 MYSQL인지 다른건지 모른다.
#그래서 둘 다 쿼리문으로 확인을 해보고 없으면, MYSQL이나 MONGODB인지 확인해달라고 해야함.
#mysql 쿼리문
#select * from emp where empno >0
# 테이블(emp) , * (모든 컬럼), empno > 0 (조건)
#mongodb 쿼리문
#db.emp.find({empno:{$gt:3}})
# 테이블(emp), find(모든컬럼), empno:{$gt:3} (조건)

#developer가 써줘야하는 부분
#developer가

curs = ""
def db (host, user, password, db, port, charset= 'utf8'):
    global curs
    conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset)
    curs = conn.cursor()

def select_pin(collom_name, table_name):
    global curs
    query = "select %s from %s" % (collom_name, table_name) #사용자 작성 쿼리문
    curs.execute(query)
    print(curs.fetchall())


#input
Developer_db = conn_db(db) #연결하는 생성자 생성
#데이터 값 가져오는 생성자 생성
#conn_db
Developer_db.conn("localhost", "root", "asd", "study", 3306, "utf8")
Developer_db.select_pin_number(select_pin)
Developer_db.select("id", "test")
# Sellector.select_pin_number("id", "test")


