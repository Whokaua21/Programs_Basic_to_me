import sqlite3 as sql
from pix_bank import *
import random

class Bank_accont():
    def __init__(self,email:str,password:str,CPF_:str,Profession:str,Date:str,Weger:int,Name:str) -> None:
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
        cursor_data.execute('select ID_recomend from Bank_lup_cap')
        Random = random.randint(1,100000)
        ID_random = cursor_data.fetchall()
        for rando_select in enumerate(ID_random):
            if rando_select[0] == Random:
                print('Seila')
                Random = random.randint(1,100000)
        cursor_data.execute(f'insert into Bank_lup_cap(CPF,NAME,EMAIL,PASSWORD,PROFESSION,DATE_,ID_recomend,"WEGER") values ("{self.cpf}","{self.name}","{self.email}","{self.password}","{self.profe}","{self.date}","{Random}","{self.weger}");')
        connect_data.commit()
        connect_data.close

class Frame_Bank(Bank_accont):
    def __init__ (self,email,password) -> None:
        self.email_log = email
        self.password_log = password
    def Into_program(self):
        try:
            connect_data = sql.connect('Lup_cap/Bank_Lu.db')
            cursor_data = connect_data.cursor()
            cursor_data.execute(f'Select * from Bank_lup_cap where EMAIL = "{self.email_log}"')
            select_sql = cursor_data.fetchall()
            print(select_sql)
            print(f'''
            --------Interface Bank Lup--------
            NOME:{select_sql[0][2]}
            PROFISSÃO:{select_sql[0][3]}
            SALDO BANCARIO:{select_sql[0][8]}
            [P] PIX
            [E] EMPRESTIMO
            [C] CARTÃO
            [M] METAS 
            ''')    
            print(' Aviso:A Função meta ainda ta em desenvolvimento')
            select_frame = str(input('-->').upper())
            if select_frame == 'P':
               ...
            elif select_frame == 'E':
                ...
            elif select_frame == 'C':
                ...
            elif select_frame == 'M':
                ...
        except:
            print()

    def Sql_login(self):
        connect_data = sql.connect('Lup_cap/Bank_Lu.db')
        cursor_data = connect_data.cursor()
        cursor_data.execute('''
        Select EMAIL,PASSWORD from Bank_lup_cap
        ''')
        select_log = cursor_data.fetchall()
        for i ,verify_log in enumerate(select_log):
            if verify_log[0] == self.email_log and verify_log[1] == self.password_log:
                return 'LOGIN'
        connect_data.close()
        return 'ERROR'
con = sql.connect('Lup_cap/Bank_Lu.db')
cur = con.cursor()
cur.execute('alter table Bank_lup_cap add column TELEFONE')