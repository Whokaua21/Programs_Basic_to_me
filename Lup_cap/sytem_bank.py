import sqlite3 as sql
from pix_bank import *
import random
import colorama
format_ = "-" * 20

class Bank_accont():
    def __init__(self,email:str,password:str,CPF_:str,Profession:str,Date:str,Weger:int,Name:str,Phone_informat:str) -> None:
        self.email = email
        self.password = password
        self.cpf = CPF_
        self.profe = Profession
        self.date = Date
        self.weger = Weger
        self.name = Name
        self.Phone = Phone_informat 
    def Sql_accont(self):
        connect_data = sql.connect('Lup_cap/Bank_Lu.db')
        cursor_data = connect_data.cursor()
        cursor_data.execute('select ID_recomend from Bank_lup_cap')
        Random = random.randint(1,100000)
        ID_random = cursor_data.fetchall()
        for rando_select in enumerate(ID_random):
            if rando_select[0] == Random:
                Random = random.randint(1,100000)
        cursor_data.execute(f'insert into Bank_lup_cap(CPF,NAME,EMAIL,PASSWORD,PROFESSION,DATE_,ID_recomend,WEGER,TELEFONE) values ("{self.cpf}","{self.name}","{self.email}","{self.password}","{self.profe}","{self.date}","{Random}","{self.weger}","{self.Phone}");')
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
            connect_data.close()
            Bank_p = Pix_bank(select_sql[0][4],select_sql[0][5],select_sql[0][2],select_sql[0][8],select_sql[0][9],select_sql[0][1],select_sql[0][0],select_sql[0][3])
            Bank_p.Frame_log()
        except:
            print('Erro 45:')

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
def recomend_ (number_recomend):
    connect_data = sql.connect('Lup_cap/Bank_Lu.db')
    cursor_data = connect_data.cursor()
    cursor_data.execute('Select ID_recomend from Bank_lup_cap')
    select_sql = cursor_data.fetchall()
    for i,recoment in enumerate(select_sql):
        print(recoment[0])
        if recoment[0] == number_recomend:
                print('ok')
                cursor_data.execute(f'select Weger from Bank_lup_cap where ID_recomend = "{number_recomend}"' )
                select_sql = cursor_data.fetchall()
                value = 5 + select_sql[0][0]
                cursor_data.execute(f'Update Bank_lup_cap set WEGER = "{value}" where ID_recomend = "{number_recomend}" ')
                connect_data.commit()

                return 'ACEITO'
    else:
        return 'ERRO'
connect_data = sql.connect('Lup_cap/Bank_Lu.db')
cursor_data = connect_data.cursor()
cursor_data.execute('Delete from Loan_bank')
connect_data.commit()
