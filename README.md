# ATM_Controller Read.me
'''ATM을 Controller할 수 있는 라이브러리입니다.'''

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


### 3.사용법(controll_class)

