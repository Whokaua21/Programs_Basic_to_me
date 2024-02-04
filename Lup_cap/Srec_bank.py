import os
from sytem_bank import *
import sqlite3 as sql
from colorama import *

format_ = '-' * 30
list_letter = {'Yes':['SIM','S','SI',],'Not':['N','NÃO','NA','NÃ']}
list_email = ['@GMAIL.COM','@LIVE.COM','@OUTLOK.COM']
# this program is a creat from a bank 
print(f'{format_}LUP BANK{format_}')
Accont_have = str(input('Você tem uma conta no LUP BANK [S/N]:')).upper()
if Accont_have in list_letter['Yes']:
        print(f'{format_}Login de Conta{format_}')
        email_user = str(input('Email:')).upper()
        password_user = str(input('Senha:'))
        print(Sql_login())

       
elif Accont_have in list_letter['Not']:
    try:
        while True:
                os.system('cls')
                print(f'{format_}Creaçao de conta{format_}')
                name_user = str(input('Nome do usuario:')).upper()
                while True:
                    email_user = str(input('Email:')).upper()
                    for Email in range(len(list_email)):
                        print(list_email[Email])
                        if list_email[Email] in email_user:
                            Email = True
                            break
                    if Email == True:
                        break
                    elif len(list_email) == 3:
                        print(Fore.RED+'Email Invalido'+Style.RESET_ALL)
                        continue    
                    break
                while True:
                    password_user = str(input('Senha (minimo 8):'))
                    if len(password_user) < 8:
                        print(Fore.RED +'Erro 27:A Senha deve ter no minimo 8 digitos'+ Style.RESET_ALL)
                        continue
                    break
                Profession_user = str(input('Profissão de usuario:')).upper()
                while True:
                    Date_Birthday = str(input('Data de Aniversario:').strip())
                    if len(Date_Birthday) > 8:
                        print(Fore.RED + 'Erro de Senha' + Style.RESET_ALL)
                    Date_Birthday_format = f'{Date_Birthday[0:2]}/{Date_Birthday[2:5]}/{Date_Birthday[4:7]}'
                    print(Date_Birthday_format)
                    
                    CPF_ = str(input('CPF de usuario:'))
                    CPF_format =f'{CPF_[0:3]}.{CPF_[3:6]}.{CPF_[6:9]}-{CPF_[9:11]}'
                    print(CPF_format)
                    Weger_user = float(input('Salario do usuario:'))
                    Recomend_user = str(input('Você foi recomendado [S/N]:')).upper()
                    if Recomend_user in list_letter['Yes']:
                        print('Obs:Coloque o numero de recomendação que esta no banco do recomendador')
                        Who_recomend = str(input('Numero de Reconmendação:'))
                    Sql_log = Bank_accont(email_user,password_user,CPF_format,Profession_user,Date_Birthday_format,Weger_user,name_user)
                    Sql_log.Sql_accont()
                    print(Fore.GREEN + f'{format_}Login feito com Concluido{format_}' + Style.RESET_ALL)
    except ValueError:
        print('Erro:Valor incoreto')
       
