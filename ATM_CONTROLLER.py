class conn_db:
    def __init__(self, conn):
        self.conn = conn

    def select_pin_number(self, select):
        self.select = select
