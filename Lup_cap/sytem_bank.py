import sqlite3 as sql


class Bank_accont():
    def __init__(self,email:str,password:str,CPF_:str,Profession:str,Date:str,Weger:float,Name:str) -> None:
        self.email = email
        self.password = password
        self.cpf = CPF_
        self.profe = Profession
        self.date = Date
        self.weger = Weger
        self.name = Name
    def Sql_accont(self):
        connect_data = sql.connect('Lup_cap/Bank_Lu.db')
        cursor_data = connect_data.cursor()
        cursor_data.execute(f'insert into Bank_lup_cap(CPF,NAME,EMAIL,PASSWORD,PROFESSION,WEGER,DATE_) values ("{self.cpf}","{self.name}","{self.email}","{self.password}","{self.profe}","{self.weger}","{self.date}");')
        connect_data.commit()

def Sql_login():
    connect_data = sql.connect('Lup_cap/Bank_Lu.db')
    cursor_data = connect_data.cursor()
    cursor_data.execute('''
    Select EMAIL,PASSWORD from Bank_lup_cap
    ''')
    select_log = cursor_data.fetchall()
    return select_log