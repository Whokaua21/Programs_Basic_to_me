
from random import randint as Rep_t
from Card_areport import *
Dict_to_play = {}
with open('Data_of_user.json','r') as Jsun:
    Dict = json.load(Jsun)
Keys_Email = Dict.keys()
Value_Password = Dict.values()


    # That function comfirm the pay: 
def Pay_Ticket(Choice_place:str,Values_ticket:dict,Dicionario:dict ):
    Dict_to_Accont = {}
    print(f'Você deseja Viajar para {Choice_place}')
    print(f'O valor da passagem e {Values_ticket}')
    How_pay = str(input('''Para pagar você tem que criar um cartao, 
            Você tem o cartao ?
            [S/N]->''')).upper()
    if How_pay == 'S':
            Accont_email = input('Email:')
            Pass_word = input('Senha:')
            if Accont_email == Keys_Email and Pass_word == Value_Password:
                print('ok')
            return
    elif How_pay == 'N':
            print('Não')
            
while True:
    #Here is a menu to client
    print('Aeroporto do Brasil:')
    Dict_Place = {'CANADA':5.747,'ALEMANHA':5.518,
                'JAPAO':9.230,'REINO UNIDO': 6.744,
                    'PORTUGAL':4.959,'RUSSIA':3.168,
                    'ANGOLA':6.043,'AFRICA':8.069,
                    'ITALIA':5.693,'MEXICO':4.731,
                    'GRECIA':6.478,'COREIA DO SUL':5.994}
    print(f'''___________COMPAINHA AVOAR DO CEU:PASSAGENS___________ 
    Canada:{Dict_Place['CANADA']}        Alemanha:{Dict_Place['ALEMANHA']}      Mexico:{Dict_Place['MEXICO']}
    Japao:{Dict_Place["JAPAO"]}         Russia:{Dict_Place['RUSSIA']}        Coreia do Sul:{Dict_Place['COREIA DO SUL']}
    Portugal:{Dict_Place["PORTUGAL"]}     Reino Unido:{Dict_Place['REINO UNIDO']}    Italia:{Dict_Place['ITALIA']}    
    Angola:{Dict_Place['ANGOLA']}         Africa:{Dict_Place['AFRICA']}        Grecia:{Dict_Place['GRECIA']}
    _______________________________________________________''')
    # The Chois_a_ticket is where client  speak where he what go
    Choice_a_ticket = str(input('Onde deseja Viajar:')).upper()
    if Choice_a_ticket in Dict_Place:
        Values_to_function = Dict_Place[Choice_a_ticket]
        Pay_Ticket(Choice_a_ticket,Values_to_function,Dict_to_play)
        break
    elif Choice_a_ticket not in Dict_Place:
        print('Erro:Certifique que o nome do pais esteja certo')
    # Here  he send to function
