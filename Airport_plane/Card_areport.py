# Function to Register of Emails
import json
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
                Dict_register[Register_email[0]] = Register_password
                break
            elif len(Register_password) < 8:
                print('Sua senha e muito curta por favor troque')
            continue
        else:
            print('Ops Ocorreu um erro:')
            continue
    return Dict_register
Dict = Accont_plane()
with open('Data_of_user.json','w') as Json_save:
    Salve = json.dump(Dict,Json_save)


