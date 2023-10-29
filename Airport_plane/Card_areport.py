# Function to Register of Emails
def Accont_plane():
    List_Emails = ['@GMAIL.COM','@LIVE.COM','@OUTLOK.COM']
    Dict_register = {}
    # Restart to Register
    while True:
        print('-----CADASTRO DO CARTAO-----')
        Register_email = str(input('EMAIL:')).upper()
        Register_password = str(input('SENHA:'))
        if List_Emails[0] in Register_email or List_Emails[1] in Register_email or List_Emails[2] in Register_email :
            if len(Register_password) >= 8:
                Dict_register[Register_email] = Register_password
                break
            print('Sua senha e muito curta por favor troque')
            continue
        if Register_email in Dict_register.keys() and Register_password in Dict_register.values:
            print('Sim')
        else:
            print('Ops Ocorreu um erro:')
            continue
    return Dict_register



