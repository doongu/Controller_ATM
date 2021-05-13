class DB:
    # 클래스의 생성자 항상 함수 형태를 가지고 init이라는 이름 을 가지고 self를 기본으로 가짐

    def db_connect(self, db_collect, *args):
        self.db_connect_args = []
        for i in args:
            self.db_connect_args.append(i)
        self.db_collect = db_collect

    def select_connect(self, select_def, *args):
        self.db_select_args = []
        for i in args:
            self.db_select_args.append(i)
        self.select_def = select_def

    def connect(self):
        self.db_collect(*self.db_connect_args)
    def select(self):
        self.select_def(*self.db_select_args)

class Controll(DB):
    def __init__(self, Controller):
        self.Controller = Controller
    #확인
    def confirm_money(self, confirm):
        self.confirm = confirm

    #입금
    def deposit_money(self, deposit):
        self.deposit = deposit

    #출금
    def withdraw_money(self, withdraw):
        self.withdraw = withdraw


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
