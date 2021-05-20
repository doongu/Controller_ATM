# ATM_Controller Read.me
'''
##ATM을 Controller할 수 있는 라이브러리입니다.
'''
###요약
밸리데이션 기능을 통해 PIN번호의 유효성을 확인할 수 있습니다.

###종류 및 라이브러리 추가 방법
- DB_CLASS
```python
from ATM_CONTROLLER import DB
```
본인의 DB와 연동하고, PIN번호를 가져오기 위한 Class입니다.


- Controll_CLASS
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

###사용법
- DB_CLASS
본인의 DB와 연동하기 위해서는, DB연결 코드를 함수로 작성해주셔야합니다.
pymysql 예시
```python
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

함수를 작성한 후 라이브러리를 활용해 Class를 만들어주시면 됩니다. 아래는 라이브러리를 활용한 예제입니다.

```python
Developer_db = DB() #연결하는 생성자 생성
Developer_db.db_connect(db, "localhost", "root", "asd", "study_test", 3306, "utf8") #인자로 (만들어둔 함수, 그 함수의 인자들)로 입력하시면 됩니다.
Developer_db.select_connect(select_pin,"*" , "study_test") #select를 하기 위해 (만들어둔 select 함수, 그 함수의 인자들)을 입력하시면 됩니다.
```

이후에는 Class를 호출하면 이전에 만든 함수를 실행시킬 수 있습니다.

```python
Developer_db.connect()
Developer_db.select()
```


