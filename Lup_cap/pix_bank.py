import sqlite3 as sql
format_ = '-' * 20
class Pix_bank():
    def __init__(self,email_verify,password_pix,name_use,weger,phone,cpf,ID) -> None:
        self.email_pix = email_verify
        self.pix_pass = password_pix
        self.name_verify = name_use
        self.weger = weger
        self.cpf= cpf
        self.phone = phone
        self.ID = ID
    def Choice_person(self):
        while True:
                print(f'{format_}Pix BankLup{format_}')
                Choise_person = str(input(''' 
                [N]NOVO PIX
                [A]ANTIGO PIX
                [K] NOVA CHAVE
                -->''').upper())
                while True:
                        if Choise_person == 'N':
                            Choise_key = str(input('Digite a chave Pix do usuario:').upper())
                            connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                            cursor_database = connect_database.cursor()
                            cursor_database.execute(f'Select Key_pix from Bank_lup_cap where Key_pix = "{Choise_key}"')
                            select_sql = cursor_database.fetchall()
                            print(select_sql)
                            connect_database.close()
                            if select_sql == []:
                                print('Essa Chave não existe')
                                print('[V]VOLTAR\n[C]CONTINUAR')
                                yes_not = str(input('--->'))
                                if yes_not == 'V':
                                    break
                                else:
                                    continue
                            value_pix = int(input('Digite o valor:'))
                            connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                            cursor_database = connect_database.cursor()
                            cursor_database.execute(f'Select WEGER from Bank_lup_cap where WEGER = {self.weger}')
                            select_sql = cursor_database.fetchall()
                            value_select = select_sql[0][0] - value_pix
                            print(value_select)
                            print(value_pix)
                            print(select_sql[0][0])
                            cursor_database.execute(f'Update Bank_lup_cap set WEGER = {value_select} where ID = {self.ID}')
                            connect_database.commit()
                            cursor_database.execute(f'Select * from Bank_lup_cap where Key_pix = {Choise_key}')
                            select_sql = cursor_database.fetchall()
                            value_pix
                            cursor_database.execute(f'Update Bank_lup_cap set WEGER = {value_select} where Key_pix = "{Choise_key}" ')
                            connect_database.commit()
                           
                           
                            break
                        if Choise_person == 'A':
                            ...
                        elif Choise_person == 'K':
                            print(f'{format_}CRIAÇAO DE CHAVE{format_}')    
                            key_choice = input('''
                            [E] EMAIL
                            [C] CPF
                            [T] TELEFONE
                            -->''')        
                            match key_choice:
                                case 'E':
                                    connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                                    cursor_database = connect_database.cursor()
                                    cursor_database.execute(f'Update Bank_lup_cap set Key_pix ="{self.email_pix}" where CPF = "{self.cpf}";')
                                    connect_database.commit()
                                    
                                case 'C':
                                    connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                                    cursor_database = connect_database.cursor()
                                    cursor_database.execute(f'Update Bank_lup_cap set Key_pix = "{self.cpf}" where CPF = "{self.cpf}";')
                                    connect_database.commit()
                                case 'T':
                                    connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                                    cursor_database = connect_database.cursor()
                                    cursor_database.execute(f'Update Bank_lup_cap set Key_pix = "{self.phone}" where CPF = "{self.cpf}";')
                                    connect_database.commit()
    