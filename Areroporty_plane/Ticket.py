def Pay_Ticket(Choice_place:str,Dict_exenple:dict):
    print(f'Você deseja Viajar para {Choice_place}')
    print(f'O valor da passagem foi de')


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
Portugal{Dict_Place["PORTUGAL"]}     Reino Unido:{Dict_Place['REINO UNIDO']}    Italia:{Dict_Place['ITALIA']}    
Angola{Dict_Place['ANGOLA']}         Africa:{Dict_Place['AFRICA']}        Grecia:{Dict_Place['GRECIA']}
_______________________________________________________''')
Choice_a_ticket = str(input('Onde deseja Viajar')).upper()
# The Chois_a_ticket is where client  speak where he what go

if Choice_a_ticket in Dict_Place:
    Values_ = Dict_Place[Choice_a_ticket]
    print(Values_)
