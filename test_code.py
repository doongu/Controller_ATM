import pymysql
from ATM_CONTROLLER import DB, Controll, My_Pin_Format #ATM_CONTROLLER의 DB, Controll, My_Pin_Format을 포함시켜야합니다.

#mysql의 예제입니다.
curs = ""
#작성하셔야되는 db연결 예제입니다.
def db (host, user, password, db, port, charset= 'utf8'):
    global curs
    conn = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset)
    curs = conn.cursor()

#작성하셔야되는 pin번호 조회 예제입니다.
def select_pin(collom_name, table_name):
    global curs
    query = "select %s from %s" % (collom_name, table_name) #사용자 작성 쿼리문
    curs.execute(query)
    print(curs.fetchall())

#작성하셔야되는 잔액확인함수 예제입니다.
def confirm( table_name):
#def confirm(money_collom_name, table_name, pin_collom, pin):
    global curs
    #query = "select %s from %s where %s = %s" % (money_collom_name, table_name, pin_collom, pin)
    query = "select * from %s" % (table_name)
    curs.execute(query)
    print(curs.fetchall())

#작성하셔야되는 입금함수 예제입니다.
def deposit(money_collom_name, table_name, input_money ,pin_collom, pin):
    global curs
    query = '''update %s set %s = %s + %s where %s = "%s"''' % (table_name, money_collom_name, money_collom_name, input_money, pin_collom, str(pin))
    curs.execute(query)
    curs.fetchall()

#작성하셔야되는 출금함수 예제입니다.
def withdraw(money_collom_name, table_name, pin_collom, pin):
    global curs
    query = '''update %s set %s = %s - %s where %s = "%s"''' % (table_name, money_collom_name, money_collom_name, input_money, pin_collom, str(pin))
    curs.execute(query)
    curs.fetchall()

#Pin번호
#Pin번호 유효성을 체크합니다. 반환값은 각 자리수를 붙여서 문자열로 반환해줍니다.
#당신 은행의 벨리데이션과 유사한 형태인 값들만 select하시면 됩니다
Pin_list = ["123-11", "11-1", "23-2"]
my_pin_format_list = My_Pin_Format(Pin_list)


#DB사용
#DB.db_connect , DB.select_connect, DB.connect , DB.select가 있습니다.

#본인 DB를 연결하고 유동적으로 사용하기 위해선 우선 본인 DB를 아래와 같은 형식으로 연결해줘야 합니다.
Developer_db = DB() #연결하는 생성자 생성
Developer_db.db_connect(db, "localhost", "root", "asd", "study_test", 3306, "utf8") #인자로 (만들어둔 함수, 그 함수의 인자들)로 입력하시면 됩니다.
Developer_db.select_connect(select_pin,"*" , "study_test") #select를 하기 위해 (만들어둔 select 함수, 그 함수의 인자들)을 입력하시면 됩니다.

#이전에 넣은 값들을 아래와 같이 편하게 실행할 수 있습니다.
Developer_db.connect()
Developer_db.select()

#Controller 사용법
#위와 같은 방식으로 함수 정의를 해주셔야합니다.
#Controller.confirm_money, Controller.deposit_money, Controller.withdraw_money,

#아래는 실행함수입니다.
#Controller.confirm_exe, Controller.deposit_exe, Controller.withdraw_exe,

#controll 생성자 생성
my_controller = Controll()
my_controller.confirm_money(confirm, "study_test" )  # (만들어둔 confirm 함수, 인자들)
my_controller.deposit_money(deposit, "pin", "study_test", 1, "user1", "HKJ") # (만들어둔 deposit함수, 인자들)
my_controller.withdraw_money(withdraw, "pin", "study_test", 1, "user1", "HKJ") # (만들어둔 withdraw_money 함수, 인자들)

my_controller.confirm_exe() # 잔액 확인
my_controller.deposit_exe() # 1달러 입금
my_controller.withdraw_exe()  # 1달러 출금
