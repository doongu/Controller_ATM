class DB:
    # 클래스의 생성자 항상 함수 형태를 가지고 init이라는 이름 을 가지고 self를 기본으로 가짐

    #db연결 함수 생성
    def db_connect(self, db_collect, *args):
        self.db_connect_args = []
        for i in args:
            self.db_connect_args.append(i)
        self.db_collect = db_collect

    #select 함수 생성
    def select_connect(self, select_def, *args):
        self.db_select_args = []
        for i in args:
            self.db_select_args.append(i)
        self.select_def = select_def

    #db연결 함수 실행
    def connect(self):
        self.db_collect(*self.db_connect_args)

    #db연결 함수 생성
    def select(self):
        self.select_def(*self.db_select_args)

class Controll:
    #확인 함수 생성
    def confirm_money(self, confirm_func, *confirm_args):
        self.confirm_list = []
        for i in confirm_args:
            self.confirm_list.append(i)
        self.confirm_func = confirm_func
    #입금 함수 생성
    def deposit_money(self, deposit_func, *deposit_args):
        self.deposit_list = []
        for i in deposit_args:
            self.deposit_list.append(i)
        self.deposit_func = deposit_func
    #출금 함수 생성
    def withdraw_money(self, withdraw_func, *withdraw_args):
        self.withdraw_list = []
        for i in withdraw_args:
            self.withdraw_list.append(i)
        self.withdraw_func = withdraw_func

    #money 확인 함수 실행
    def confirm_exe(self):
        self.confirm_func(*self.confirm_list)

    #입금 함수 실행
    def deposit_exe(self):
        self.deposit_func(*self.deposit_list)

    #출금 함수 실행
    def withdraw_exe(self):
        self.withdraw_func(*self.withdraw_list)

#list로 입력을 받는다.
def My_Pin_Format(*pin):
    retun_pin_format = []
    for i in pin:
        if PIN(i):
            return_pin_format.append(PIN(i))
        else:
            print("문자열을 제대로 입력해주세요.")
            return False
    else:
        print("당신 은행의 포맷형태들은 다음과 같습니까?")
        for i in retun_pin_format:
            print(i)
        return retun_pin_format

def PIN(pin):
    #벨리데이션

    #type이 문자열인지 체크
    if str(type(pin)) == "<class 'str'>":
        if pin[-1] == "-" or pin[0] == "-":
            print("문자열을 제대로 입력해주세요.")
            return False

        #문자열이 "-"와 "숫자"로 이루어져 있는지 체크
        for check_str in pin:
            if check_str != "-" and check_str.isdigit() == False:
                print("문자열을 제대로 입력해주세요.")
                return False
        else: #for문이 성공적으로 완수하면 벨리데이션값 리턴
            list_key_val = list(map(lambda x : len(x), pin.split("-")))
            return_ket_val = "".join(list_key_val)
            return return_ket_val

    #type이 문자열이 아니면 에러 출력 return False
    else:
        print("문자열을 입력해주세요.")
        return False
