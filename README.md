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
```
from ATM_CONTROLLER import Controll
```
연동한 DB를 Controll(잔액확인, 입금, 출금)하기 위한 Class입니다.

- 벨리데이션_함수
```
from ATM_CONTROLLER import My_Pin_Format
```
PIN번호의 유효성을 검사하기 위한 함수입니다.

###동작 및 기능
