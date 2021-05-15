#test코드 작성

import pymysql
from ATM_CONTROLLER import DB, Controll, My_Pin_Format

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

#controller func 사용자 제작 부분 예제
def confirm( table_name):
#def confirm(money_collom_name, table_name, pin_collom, pin):
    global curs
    #query = "select %s from %s where %s = %s" % (money_collom_name, table_name, pin_collom, pin)
    query = "select * from %s" % (table_name)
    curs.execute(query)
    print(curs.fetchall())

def deposit(money_collom_name, table_name, input_money ,pin_collom, pin):
    global curs
    query = '''update %s set %s = %s + %s where %s = "%s"''' % (table_name, money_collom_name, money_collom_name, input_money, pin_collom, pin)
    curs.execute(query)
    curs.fetchall()

def withdraw(money_collom_name, table_name, input_money, pin_collom, pin):
    global curs
    query = '''update %s set %s = %s - %s where %s = "%s"''' % (table_name, money_collom_name, money_collom_name, input_money, pin_collom, pin)
    curs.execute(query)
    curs.fetchall()

#Pin번호
#Pin번호 유효성을 체크합니다. 반환값은 각 자리수를 붙여서 문자열로 반환해줍니다.
#당신 은행의 벨리데이션과 유사한 형태인 값들만 select하시면 됩니다 .. ?
Pin_list = ["123-11", "11-1", "23-2"]
my_pin_format_list = My_Pin_Format(Pin_list)


#DB사용
#DB.db_connect , DB.select_connect, DB.connect , DB.select
Developer_db = DB() #연결하는 생성자 생성
Developer_db.db_connect(db, "localhost", "root", "asd", "study_test", 3306, "utf8")
Developer_db.select_connect(select_pin,"*" , "study_test")

Developer_db.connect()
Developer_db.select()

#Controller 사용
#Controller.confirm_money, Controller.deposit_money, Controller.withdraw_money,
#Controller.confirm_exe, Controller.deposit_exe, Controller.withdraw_exe,
my_controller = Controll()
my_controller.confirm_money(confirm, "study_test" )
my_controller.confirm_exe()
print("deposit")
my_controller.deposit_money(deposit, "pin", "study_test", 1, "user1", "HKJ")
Developer_db.select()

my_controller.deposit_exe()
Developer_db.select()

my_controller.deposit_exe()
Developer_db.select()

print("withdraw")
my_controller.withdraw_money(withdraw, "pin", "study_test", 1, "user1", "HKJ")
my_controller.withdraw_exe()
Developer_db.select()

my_controller.withdraw_exe()
Developer_db.select()

my_controller.withdraw_exe()
Developer_db.select()

