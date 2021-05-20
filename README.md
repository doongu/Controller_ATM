# ATM_Controller Read.me
'''ATM을 Controll할 수 있는 라이브러리입니다.'''

### 요약
밸리데이션 기능을 통해 PIN번호의 유효성을 확인할 수 있습니다. controller 기능을 통해 잔액 확인, 입금, 출금을 할 수 있습니다.

### 종류 및 라이브러리 추가 방법
- db_class
```python
from ATM_CONTROLLER import DB
```
본인의 DB와 연동하고, PIN번호를 가져오기 위한 Class입니다.


- controll_class
```python
from ATM_CONTROLLER import Controll
```
연동한 DB를 Controll(잔액확인, 입금, 출금)하기 위한 Class입니다.

- 벨리데이션_함수
```python
from ATM_CONTROLLER import My_Pin_Format
```
PIN번호의 유효성을 검사하기 위한 함수입니다.

---

### 1. 사용법(db_class)
- DB_CLASS
위 CLASS를 추가해준 뒤, 본인의 DB와 연동하기 위해서는, DB연결 코드를 함수로 작성해주셔야합니다. (pymysql 예시)
```python
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
```

함수를 작성한 후 라이브러리를 활용해 Class를 만들어주시면 됩니다.

DB()의 구성요소는, db_connect, select_connect가 있습니다.

#### db_connect의
인자로는 db_connect( 앞서 작성한 db연결 함수 이름, 앞서 작성한 db연결 함수의 인자들 )을 할당하시면 됩니다. 
#### select_connect의 
인자로는 select_connect( 앞서 작성한 select 함수 이름, 앞서 작성한 select 함수의 인자들 )을 할당하시면 됩니다. 
아래는 라이브러리를 활용한 예제입니다.
```python
Developer_db = DB() #연결하는 생성자 생성
Developer_db.db_connect(db, "localhost", "root", "asd", "study_test", 3306, "utf8") #인자로 (만들어둔 함수, 그 함수의 인자들)로 입력하시면 됩니다.
Developer_db.select_connect(select_pin,"*" , "study_test") #select를 하기 위해 (만들어둔 select 함수, 그 함수의 인자들)을 입력하시면 됩니다.
```
DB()의 db_connect와 select_connect에 값을 전달 하셨다면, connect()와 select()함수로 db를 연동하고, 값을 불러 올 수 있습니다.
아래는 connect()와 select()사용 예제입니다.
```python
Developer_db.connect()
Developer_db.select()
```

### 2.사용법(controll_class)
위와 크게 사용방식은 바뀌지 않습니다.
```python
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
```

```python
my_controller = Controll()
my_controller.confirm_money(confirm, "study_test" )  # (만들어둔 confirm 함수, 인자들)
my_controller.deposit_money(deposit, "pin", "study_test", 1, "user1", "HKJ") # (만들어둔 deposit함수, 인자들)
my_controller.withdraw_money(withdraw, "pin", "study_test", 1, "user1", "HKJ") # (만들어둔 withdraw_money 함수, 인자들)

my_controller.confirm_exe() # 잔액 확인
my_controller.deposit_exe() # 1달러 입금
my_controller.withdraw_exe()  # 1달러 출금
```

### 3.사용법(벨리데이션 함수)
My_Pin_Format을 import한 이후 문자열이 담긴 list형식으로 My_Pin_Format으로 전달해 주면 됩니다.
```python
Pin_list = ["123-11", "11-1", "23-2"]
my_pin_format_list = My_Pin_Format(Pin_list)
```
My_Pin_Format은 위 예제의 return 값으로 ["32", "21", "21"]을 반환해 줍니다.
