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
List_delet_something = []
Data_firebse = {}
Delete_us = {}

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
                wind_Id.destroy()
        # Windos of Creat ID 
        winTk.destroy
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
    Delete_Tk.geometry('1100x800')
    Delete_Tk.resizable(width=False,height=False)
    # Frames to the windos delete
    Frame_stripe = Frame(Delete_Tk,width=7000,height=100,bg='Black')
    Frame_Column = Frame(Delete_Tk,height=7000,width=7000,bg='Pink')
    def Delete_clik():
    
        cont = 0
        if Entr_delete.get() == '': 
            messagebox.showerror('Erro de informaçao','Você não colocou nada na caixa de informaçao')
        else:
            for Delet_bye in Json_load:
        
                if Entr_delete.get() == Delet_bye:
                    requests.delete(f'{Link_base}/Produto/{Delet_bye}/.json')

                elif Entr_delete.get() == List_delet_something[cont]:

                    requests.delete(f'{Link_base}/Produtos/{Delet_bye}/.json')
                    messagebox.showinfo('Item Deletado','Item Deletado com sucesso')
                    break
                cont += 1
            if Entr_delete.get() not in Delet_bye or Entr_delete.get() not in List_delet_something:
                messagebox.showerror('Erro de find','Esse ID Não existe veja se você escreveu certo ou se o ID Existe') 
            Entr_delete.delete('0','end')
        
    def Upgrade_buttom():
        
        def DEf_Upgrade():
          
            if Entry_write.get() == '':
                messagebox.showerror('Erro 147','Você não colocou o ID do produto')
            else:  
                cont = 0
                for Delet_bye in Json_load:

                    if Entry_write.get() == Delet_bye:

                        print('AA')
                        if Entry_write_product.get() != '' and Entry_Details_Values_Product.get() != '':
                            print('aaa')

                        elif Entry_write_product.get() != '':
                            Data_firebse = {'Nome_produto':Entry_write_product.get()}
                            o = requests.patch(f'{Link_base}/Produtos/{Delet_bye}/.json',data=json.dumps(Data_firebse))
                            print(o)

                        elif Entry_Details_Values_Product.get() != '':
                            print('Yes')
                            Data_firebse = {'Valor Produto':Entry_Details_Values_Product.get()}
                            a = requests.patch(f'{Link_base}/Produtos/{Delet_bye}/.json',data=json.dumps(Data_firebse))
                            print(a)
                        else:
                            print('Tudo errado')

                        break
                

                    elif Entry_write.get() == List_delet_something[cont]:

                        print('BBB')
                        if Entry_write_product.get() != '' and Entry_Details_Values_Product.get() != '':
                            print('aaa')
                            o = requests.patch(f'{Link_base}/Produtos/{Delet_bye}/.json',data=json.dumps(Data_firebse))
                            a = requests.patch(f'{Link_base}/Produtos/{Delet_bye}/.json',data=json.dumps(Data_firebse))
                            messagebox.showinfo('Alteraçao concluida','Alteraçao deita com sucesso')

                        elif Entry_write_product.get() != '':
                            Data_firebse = {'Nome_produto':Entry_write_product.get()}
                            o = requests.patch(f'{Link_base}/Produtos/{Delet_bye}/.json',data=json.dumps(Data_firebse))
                            messagebox.showinfo('Alteraçao concluida','Alteraçao deita com sucesso')
                            print(o)

                        elif Entry_Details_Values_Product.get() != '':
                            print('Yes')
                            Data_firebse = {'Valor Produto':Entry_Details_Values_Product.get()}
                            a = requests.patch(f'{Link_base}/Produtos/{Delet_bye}/.json',data=json.dumps(Data_firebse))
                            messagebox.showinfo('Alteraçao concluida','Alteraçao deita com sucesso')
                            print(a)
                        else:
                            print('Tudo errado') 
                        break
                    cont += 1


               
                Entry_write_product.delete('0','end')
                Entry_Details_Values_Product.delete('0','end')
                Entry_user.delete('0','and')
                 
            
           
            
        Upgrade_Tk = Tk()
        Upgrade_Tk.geometry('600x800')
        Upgrade_Tk.resizable(width=False,height=False)
        # Frame
        Frame_center = Frame(Upgrade_Tk,width=1000,height=100,bg='Blue')

        # Itens to scree
        LAbel_Upgrade = Label(Frame_center,text='Alteraçao de ID',font='Arial 20')
        Label_write = Label(Upgrade_Tk,text='Escreva o codigo do produto:',font='Arial 20')
        Entry_write = Entry(Upgrade_Tk,font='Arial 20')

        Label_Detail_product = Label(Upgrade_Tk,text='Alterar nome do produto:',font='Arial 20')
        Entry_write_product = Entry(Upgrade_Tk,font='Arial 20')

        Label_Detail_Values_product = Label(Upgrade_Tk,text='Altera Valor do produto:',font='Arial 20')
        Entry_Details_Values_Product = Entry(Upgrade_Tk,font='Arial 20')

        Label_user = Label(Upgrade_Tk,text='Quem esta Alterando:',font='Arial 20')
        Entry_user = Entry(Upgrade_Tk,font='Arial 20')

        Button_Ready_Upgrade = Button(Upgrade_Tk,text='Pronto',padx=100,pady=20,command=DEf_Upgrade)

        # put
        Frame_center.place(x=0)
        LAbel_Upgrade.place(x=200)

        Label_write.place(x=20,y=150)
        Entry_write.place(x=20,y=200,relwidth=0.9)

        Label_Detail_product.place(x=20,y=260)
        Entry_write_product.place(x=20,y=320,relwidth=0.9)

        Label_Detail_Values_product.place(x=20,y=380)
        Entry_Details_Values_Product.place(x=20,y=420,relwidth=0.9)

        Label_user.place(x=20,y=500)
        Entry_user.place(x=20,y=555,relwidth=0.9)

        Button_Ready_Upgrade.place(x=165,y=650)




    # Other things
    Label_delete = Label(Frame_stripe,text='Codigo do Produto:',font='Arial 15')
    Entr_delete = Entry(Frame_stripe,font='Arial 12',)

    Label_Date = Label(text='Data de hoje',font='Arial 15')
    Label_time = Label(text=datetime.now().strftime('%d-%m-%Y'),font='Arial 15')
    print(datetime.today())
    Buttom_delete_wind = Button(Frame_stripe,text='Deletar\nID',padx=20,pady=31,command=Delete_clik)
    Buttom_Upgrade = Button(Frame_stripe,text='Alterar\nID',padx=20,pady=31,command=Upgrade_buttom)


    # Put in Scree
    Frame_stripe.place(x=0)
    Frame_Column.place(y=100)
    # Itens 
    Label_delete.place(x=5,y=5,relwidth=0.035)
    Entr_delete.place(x=5,y=40,relwidth=0.050)

    Label_Date.place(x=400,relwidth=0.2)
    Label_time.place(x=400,y=30,relwidth=0.2)

    Buttom_delete_wind.place(x=1000)
    Buttom_Upgrade.place(x=918)
    # Frame_Column
    Label_Details_Area = Label(Frame_Column,text='ID da Area',font='Arial 10',padx=80)
    Label_Details_ID_p = Label(Frame_Column,text='ID do Produto',font='Arial 10',padx=30)
    Label_Details_Name = Label(Frame_Column,text='Nome Produto',font='Arial 10',padx=50)
    Label_Details_Values = Label(Frame_Column,text='Valor produto',font='Arial 10',padx=40)
    Label_Details_User = Label(Frame_Column,text='Usuario fornecido',font='Arial 10',padx=50)

    # put in scree
    Label_Details_Area.grid(column=0,row=0)
    Label_Details_ID_p.grid(column=1,row=0)
    Label_Details_Name.grid(column=2,row=0)
    Label_Details_Values.grid(column=3,row=0)
    Label_Details_User.grid(column=4,row=0)

    cont_columm = 1
    List_delet_something = []
    for Delet_id in Json_load:
        Local_id  =Json_load[Delet_id]['Id_produto']
        Name_ID = Json_load[Delet_id]['Nome_produto']
        Value_ID = Json_load[Delet_id]['Valor Produto']
        User_data = Json_load[Delet_id]['Usuario']
        List_delet_something.append(Local_id)

        Label_Details_Area_put = Label(Frame_Column,text=Delet_id,font='Arial 11',padx=10,pady=2)
        Label_Details_ID_p_put = Label(Frame_Column,text=Local_id,font='Arial 10',padx=52,pady=3)
        Label_Details_Name_put = Label(Frame_Column,text=Name_ID,font='Arial 11',padx=40,pady=3)
        Label_Details_Values_put = Label(Frame_Column,text=f'{Value_ID}R$',font='Arial 12',padx=100,pady=2)
        Label_Details_User_put = Label(Frame_Column,text=User_data,font='Arial 12',padx=90,pady=2)

        Label_Details_Area_put.grid(column=0,row=cont_columm)
        Label_Details_ID_p_put.grid(column=1,row=cont_columm)
        Label_Details_Name_put.grid(column=2,row=cont_columm)
        Label_Details_Values_put.grid(column=3,row=cont_columm)
        Label_Details_User_put.grid(column=4,row=cont_columm)
        cont_columm +=1


    Scrollbar_windos = Scrollbar(Delete_Tk,orient=VERTICAL)
    Scrollbar_windos.pack(side=RIGHT,fill=Y,)





    mainloop()
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
Bottom_all_buy.place(y=133)
Bottom_Codig.place(y=204)
# Now the Frame_type



if __name__ == '__main__':
    mainloop()