from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from random import randint
import requests
import json
from datetime import datetime
Option_Pay = ['Cartao','Debito','Avista']
Json_load = {}
ID_Save = {}
Link_base = 'https://id-prosuct-default-rtdb.firebaseio.com/'
List_id = []
fire_base = requests.get(f'{Link_base}/Produtos/.json')
Json_load = (fire_base.json())


     
Date = datetime.now().date
Month = datetime.now().month
Year = datetime.now().year

class Creat_id:
    '''
    Here is where he is the program of creat fo Id
    he take some infor is put in  bank data
    '''
    def __init__(self,Id:str,Value:float,Pay:str,Lot) -> None:
        self.id = Id
        self.Val = Value
        self.Pay = Pay
        self.Lot = Lot
    def creat_Id(self):
        def Save_ID():
            if Entr_Val_id.get() == '' and Entr_Val_id.get() == '':
                messagebox.showerror('Erro de informaçao','Parece que voce não colocou nada nas lacunas de informaçao do produto')
                
                    
            else:
                ID_Save = {'Id_produto':random_str,
                         'Nome_produto':Entr_id_speak.get(),
                         'Valor Produto':Entr_Val_id.get(),
                         'Usuario':Entr_Who.get()}
                Firebase = requests.post(f'{Link_base}/Produtos/.json',data=json.dumps(ID_Save),)
                print(Firebase)
        # Windos of Creat ID 

        wind_Id = Tk()
        wind_Id.geometry('200x300')
        wind_Id.resizable(width=False,height=False)
        wind_Id.title('Depois Colocar')
        wind_Id.focus()

        random_id = randint(1000,40000) 
        random_str = str(random_id)
        Label_Name_Id = Label(wind_Id,text=f'Numero do ID novo e:{random_str}',font='Arial 12')
        Label_item = Label(wind_Id,text='Nome do item:',font='Arial 11')
        Label_Val_id = Label(wind_Id,text='Valor do item:',font='Arial 11')
        Label_Who = Label(wind_Id,text='Quem esta usando:',font='Arial 11')

        Entr_Val_id = Entry(wind_Id,font='Arial 12')
        Entr_id_speak = Entry(wind_Id,font='Arial 12')
        Entr_Who = Entry(wind_Id,font='Arial 12')
        

        Button_Ready_ID = Button(wind_Id,text='Pronto',padx=30,pady=10,command=Save_ID)
        # Value of product
        Label_Val_id.place(x=10,y=90)
        Entr_Val_id.place(x=10,y=120)
        # Name Item
        Label_item.place(x=10,y=40)
        Entr_id_speak.place(x=10,y=60)
        # Number of ID
        Label_Name_Id.place(x=0,y=0)

        # Who creat the ID
        Label_Who.place(x=10,y=160)
        Entr_Who.place(x=10,y=190)        
        
        # Buttom Ready

        
       
        Button_Ready_ID.place(x=46,y=250)
        

# Ready_Work:he is the button Pronto from Screen
def Ready_Work():
    amount_buy = int(Bottom_Vol.get())
    Values_buy = float(Entr_Val.get())
    print(amount_buy)
    print(Values_buy)

    if Entr_Val.get() == '' or Entr_ID.get() == '' or Box_buttom.get() == '':
                messagebox.showerror('Erro de informaçao','Parece que você não colocou as informaçoes necesserias')
    
    else:
       
        for Dict_product in Json_load:
            Product_show = print(f'ID do produto:',Json_load[Dict_product]['Id_produto'])
            List_id.append(Json_load[Dict_product]['Id_produto']) 


        if Entr_ID.get() in List_id:
            Valor = float(Entr_Val.get())
            Quantidade = Bottom_Vol.get()
            int_quantidade = int(Quantidade)
            Receber = int_quantidade * Valor
            messagebox.showinfo(f'Finalizado',f'O preço de tudo foi {Receber}')
        else:
            messagebox.showerror('ID não existe','Verifique se você digitou certo ou se existe mesmo esse Id')
            print('ua')

def Delete_data():
    winTk.destroy()
    Delete_Tk = Tk()
    Delete_Tk.title('Depois colocar')
    Delete_Tk.geometry('700x600')
    Delete_Tk.resizable(width=False,height=False)
    # Frames to the windos delete
    Frame_stripe = Frame(Delete_Tk,width=7000,height=100,bg='Black')
    Frame_Column = Frame(Delete_Tk,height=7000,width=7000,bg='Pink')

    # Other things
    Label_delete = Label(Frame_stripe,text='Codigo do Produto:',font='Arial 12')
    Entr_delete = Entry(Delete_Tk,font='Arial 12')

    Label_Date = Label(text='Data de hoje',font='Arial 12')
    Label_time = Label(text=datetime.now().strftime('%d-%m-%Y'),font=12)
    print(datetime.today())
    Buttom_delete_wind = Button(Delete_Tk,text='Deletar\nID',padx=20,pady=31)


    # Put Scree
    Frame_stripe.grid(column=0,row=0)
    Frame_Column.place(y=100)
    # Itens 
    Label_delete.place(x=5,y=5)
    Entr_delete.place(x=5,y=40)

    Label_Date.place(x=285)
    Label_time.place(x=230,y=30)
    Buttom_delete_wind.place(x=620)
# put Tkinter

winTk = Tk()
winTk.title('Escolher depois')
winTk.geometry('800x350')
winTk.resizable(width=False,height=False)

Frame_type = Frame(winTk,width=50,height=350,bg='Black')
Frame_Val = Frame(winTk,width=1000,height=100,bg='Red')
Frame_all = Frame(winTk,width=1000,height=600,bg='green')

# put frame in screen
Frame_type.place(x=0,y=0)
Frame_Val.place(x=50,y=0)
Frame_all.place(x=50,y=50)


# Including something in Frame_Vol
Bottom_Vol = Spinbox(Frame_Val,from_=0,to=500)
Label_txt = Label(Frame_Val,text='Quantidade:')
Label_Vol = Label(Frame_Val,text='Valor:')
Label_ID = Label(Frame_Val,text='ID do produto:')
Entr_Val = Entry(Frame_Val)
Entr_ID = Entry(Frame_Val)

Box_buttom = Combobox(Frame_Val,values=Option_Pay)
Id_creat = Creat_id(Entr_ID.get(),Entr_Val.get(),Box_buttom.get(),Bottom_Vol.get())


Buttom_type = Button(Frame_type,text='Novo ID',padx=0,pady=15,command=Id_creat.creat_Id) 
Buttom_Ready = Button(Frame_Val,text='Pronto',padx=15,pady=15,command=Ready_Work)
Bottom_delete = Button(Frame_type,text='Deletar\nID',padx=5,pady=20,command=Delete_data)
Bottom_alter = Button(Frame_type,text='Alterar\nID',padx=5,pady=20,command=...)
Bottom_all_buy = Button(Frame_type,text='Prompras\nID',padx=5,pady=20,font='Arial 7',command=...)
Bottom_Codig = Button(Frame_type,text='Qr\ncode',padx=10,pady=20,command=...)
#Frame_val
Label_txt.place(x=15,y=0)
Label_ID.place(x=15,y=25)
Label_Vol.place(x=500,y=0)
Entr_Val.place(x=536)
Entr_ID.place(x=100,y=26)
Bottom_Vol.place(x=91)
Box_buttom.place(x=280)
Buttom_Ready.place(x=681)

# Frame Type
Buttom_type.place(x=0,y=0)
Bottom_delete.place(x=0,y=54)
Bottom_alter.place(x=0,y=133)
Bottom_all_buy.place(y=212)
Bottom_Codig.place(y=283)
# Now the Frame_type



if __name__ == '__main__':
    mainloop()