from tkinter import *
from tkinter.ttk import Combobox

Option_Pay = ['Cartao','Debito','Avista']
def Buy_things():
    Label_Tit = Label()
# put Tkinter
winTk = Tk()
winTk.title('Escolher depois')
winTk.geometry('800x350')
winTk.resizable(width=False,height=False)

Frame_type = Frame(winTk,width=50,height=350,bg='Black')
Frame_Val = Frame(winTk,width=1000,height=100,bg='Red')
Frame_all = Frame(winTk,width=1000,height=600,bg='green')

Frame_type.place(x=0,y=0)
Frame_Val.place(x=50,y=0)
Frame_all.place(x=50,y=50)
# input frame in screen

# Including something in Frame_Vol
Bottom_Vol = Spinbox(Frame_Val,from_=0,to=500)
Label_txt = Label(Frame_Val,text='Quantidade:')
Label_Vol = Label(Frame_Val,text='Valor:')
Label_ID = Label(Frame_Val,text='ID do produto:')
Entr_Val = Entry(Frame_Val)
Entr_ID = Entry(Frame_Val)
Box_buttom = Combobox(Frame_Val,values=Option_Pay)
Button_Ready = Button(Frame_Val,text='Pronto',padx=12,pady=15)



Label_txt.place(x=15,y=0)
Label_ID.place(x=15,y=25)
Label_Vol.place(x=500,y=0)
Entr_Val.place(x=536)
Entr_ID.place(x=100,y=26)
Bottom_Vol.place(x=91)
Box_buttom.place(x=280)
Button_Ready.place(x=681)
if __name__ == '__main__':
    mainloop()