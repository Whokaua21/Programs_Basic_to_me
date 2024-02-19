import sqlite3 as sql
import os
from colorama import *
format_ = '-' * 20
class Pix_bank():
    def __init__(self,email_verify,password_pix,name_use,weger,phone,cpf,ID,profct) -> None:
        self.email_pix = email_verify
        self.pix_pass = password_pix
        self.name_verify = name_use
        self.weger = weger
        self.cpf= cpf
        self.phone = phone
        self.ID = ID
        self.Proft = profct
    def Choice_person(self):
        """
        Here it's a sytem from pix, he go receive the key pix to a transfer
        from money, Also can create a key pix and see your Bank statement
        """""
        while True:
                print(self.cpf[0:3] + self.cpf[4:7] + self.cpf[8:11] + self.cpf[12:14])
                print(f'{format_}Pix BankLup{format_}')
                Choise_person = str(input(''' 
        [N] NOVO PIX
        [A] EXTRATO
        [K] NOVA CHAVE
                                          
        <- [V] VOLTAR
        -->''').upper())
                if Choise_person == 'V':
                     break
                while True:
                        os.system('Cls')
                        if Choise_person == 'N':
                            print(Fore.BLUE + f'{format_}Transferencia de Pix{format_}' + Style.RESET_ALL )
                            Choise_key = str(input('Digite a chave Pix do usuario:').upper())
                            connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                            cursor_database = connect_database.cursor()
                            cursor_database.execute(f'Select Key_pix from Bank_lup_cap where Key_pix = "{Choise_key}"')
                            select_sql = cursor_database.fetchall()
                            print(select_sql)
                            cursor_database.execute(f'Select Key_Pix from Bank_lup_cap where ID = "{self.ID}" ')
                            not_verify = cursor_database.fetchall()
                            connect_database.close()
                            if select_sql == [] or not_verify[0][0] == select_sql[0][0]:
                                os.system('Cls')
                                print(Fore.RED + f'{format_}Essa Chave não e Aceita{format_}' + Style.RESET_ALL)
                                print('[V]VOLTAR\n[C]CONTINUAR')
                                yes_not = str(input('--->'))
                                if yes_not == 'V':
                                    os.system('cls')
                                    break
                                else:
                                    os.system('cls')
                                    continue
                            value_pix = int(input('Digite o valor:'))
                            connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                            cursor_database = connect_database.cursor()
                            cursor_database.execute(f'Select WEGER from Bank_lup_cap where WEGER = {self.weger}')
                            select_sql = cursor_database.fetchall()
                            value_select = select_sql[0][0] - value_pix
                            cursor_database.execute(f'Update Bank_lup_cap set WEGER = {value_select} where ID = {self.ID}')
                            connect_database.commit()
                            cursor_database.execute(f'Select * from Bank_lup_cap where Key_pix = "{Choise_key}"')
                            select_sql = cursor_database.fetchall()
                            value_select = select_sql[0][8] + value_pix
                            cursor_database.execute(f'Update Bank_lup_cap set WEGER = {value_select} where Key_pix = "{Choise_key}" ')
                            connect_database.commit()
                            cursor_database.execute(f'insert into Pix_Lup(NAME,Pix_do,ID_Person,Receive_person) values ("{self.name_verify}","-{value_pix}","{self.ID}","{select_sql[0][2]}") ')
                            connect_database.commit()
                            cursor_database.execute(f'insert into Pix_Lup(NAME,Pix_do,ID_Person,Receive_person) values ("{select_sql[0][2]}","+{value_pix}","{select_sql[0][0]}","{self.name_verify}") ')
                            connect_database.commit()
                            connect_database.close()
                            break
                        if Choise_person == 'A':
                            connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                            cursor_database = connect_database.cursor()
                            cursor_database.execute(f'Select Receive_person,Pix_do from Pix_Lup where ID_Person = "{self.ID}" ')
                            select_sql = cursor_database.fetchall()
                            for i,Extrat in enumerate(select_sql):
                                 print(Extrat[0] +'    R$'+ Extrat[1])
                            yes_not = str(input('Deseja Voltar:\n[S]SIm\n[N]NÃO').upper())
                            if yes_not == 'N':
                                 break
                            else:
                                 continue
                        elif Choise_person == 'K':
                            print(Fore.BLUE + f'{format_}CRIAÇAO DE CHAVE{format_}' + Fore.BLUE)    
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
                                    cursor_database.execute(f'Update Bank_lup_cap set Key_pix = "{self.cpf[0:3] + self.cpf[4:7] + self.cpf[8:11] + self.cpf[12:14]}" where CPF = "{self.cpf}";')
                                    connect_database.commit()
                                case 'T':
                                    connect_database = sql.connect('Lup_cap/Bank_Lu.db')
                                    cursor_database = connect_database.cursor()
                                    cursor_database.execute(f'Update Bank_lup_cap set Key_pix = "{self.phone}" where CPF = "{self.cpf}";')
                                    connect_database.commit()
                                    
                        break
    def Imprestimo_(self):
        print(Fore.BLUE + f'{format_}EMPRÉSTIMO{format_}' + Style.RESET_ALL)
        loan_bank = int(input('Valor do Inprestimo ->'))
        loan_do = (self.weger / 100 )* 50
        print(loan_do)
        if loan_bank > loan_do:
            print('Erro')
        else:
             ...
             

    def Frame_log(self):
        print(f'''
            --------Interface Bank Lup--------
            NOME:{self.name_verify}
            PROFISSÃO:{self.Proft}
            SALDO BANCARIO:{self.weger}
            [P] PIX
            [E] EMPRESTIMO
            [M] METAS 
            ''')    
        print(' Aviso:A Função meta ainda ta em desenvolvimento')
        select_frame = str(input('-->').upper())
        if select_frame == 'P':
            self.Choice_person()
        elif select_frame == 'E':
            self.Imprestimo_()
        elif select_frame == 'M':
             ...