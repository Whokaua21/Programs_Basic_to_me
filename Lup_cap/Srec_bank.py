import tqdm
import os
from time import sleep
from sytem_bank import *
from colorama import *

format_ = '-' * 30
list_letter = {'Yes':['SIM','S','SI',],'Not':['N','NÃO','NA','NÃ']}
list_email = ['@GMAIL.COM','@LIVE.COM','@OUTLOK.COM']
# this program is a creat from a bank
print(f'{format_}LUP BANK{format_}')
Accont_have = str(input('Você tem uma conta no LUP BANK [S/N]:')).upper()
if Accont_have in list_letter['Yes']:
        while True:    
            print(f'{format_}Login de Conta{format_}')
            email_user = str(input('Email:')).upper()
            password_user = str(input('Senha:'))

            verify_log = Frame_Bank(email_user,password_user)
            log_ok = verify_log.Sql_login()
            if log_ok == 'LOGIN':
                os.system('cls')
                print(Fore.GREEN + f'{format_}ACESSO PERMITIDO{format_}' + Style.RESET_ALL)
                break
            else:
                os.system('cls')
                print(Fore.RED + f'{format_}ACESSO NEGADO{format_}' + Style.RESET_ALL)
                continue
        print('Preparando a interface')
        for log_ in tqdm.tqdm(range(5),colour='Green'):
            sleep(1)

elif Accont_have in list_letter['Not']:
    try:
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
        os.system('cls')
        while True:
            password_user = str(input('Senha (minimo 8):'))
            if len(password_user) < 8:
                print(Fore.RED +'Erro 27:A Senha deve ter no minimo 8 digitos'+ Style.RESET_ALL)
                continue
            break
        os.system('cls')
        Profession_user = str(input('Profissão de usuario:')).upper()
        Date_Birthday = str(input('Data de Aniversario:').strip())
        if len(Date_Birthday) > 8 or len(Date_Birthday) < 8:
            print(Fore.RED + 'Erro de Senha' + Style.RESET_ALL)
        Date_Birthday_format = f'{Date_Birthday[0:2]}/{Date_Birthday[2:4]}/{Date_Birthday[4:8]}'
        print(Date_Birthday_format)
        os.system('cls')
        while True:
            CPF_ = str(input('CPF de usuario:'))
            if len(CPF_) < 11 or len(CPF_) > 11:
                print(Fore.RED + f'{format_}Erro no CPF{format_}' + Style.RESET_ALL)
                continue
            break
        os.system('cls')
        CPF_format =f'{CPF_[0:3]}.{CPF_[3:6]}.{CPF_[6:9]}-{CPF_[9:11]}'
        print(CPF_format)
        Weger_user = str(input('Salario do usuario:'))
        if ',' in Weger_user :
            Weger_format = Weger_user.replace(',','')
        elif '.' in Weger_user:
            Weger_format = Weger_user.replace('.','')
        Weger_format = int(Weger_format)
        Recomend_user = str(input('Você foi recomendado [S/N]:')).upper()
        if Recomend_user in list_letter['Yes']:
            print('Obs:Coloque o numero de recomendação que esta no banco do recomendador')
            Who_recomend = str(input('Numero de Reconmendação:'))
        Sql_log = Bank_accont(email_user,password_user,CPF_format,Profession_user,Date_Birthday_format,Weger_format,name_user)
        Sql_log.Sql_accont()
        os.system('cls')
        print(Fore.GREEN + f'{format_}Login feito com Concluido{format_}' + Style.RESET_ALL)
    except ValueError:
        print('Erro:Valor incoreto')
        
