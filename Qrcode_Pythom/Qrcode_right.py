from tkinter import *
from qrcode import *
def Prepare_Qr():
  try:
    Qrcode = make(Entry_Url.get())
    Qrcode.save('Qrcode.png')

  except:
     print('Veja se seu link e adebito para ser Qrcode:')
Windos_tk = Tk()
Windos_tk.geometry('500x500')
Windos_tk.resizable(width=False,height=False)

Up_frame = Frame(Windos_tk,
                 height=500,
                 width=250,
                 bg='black'
                 )
Up_frame.place(x=250,y=0)
Left_frame = Frame(Windos_tk,
                   height=500,
                   width=250,
                   bg='pink'
                
)
Left_frame.place(x=0,y=0) 
Label_Word = Label(Left_frame,
                   text='Criador de Qrcode',
                   font='Arial 15',
                   )
Label_Word.place(x=20,y=30)
LAbel_Url = Label(Left_frame,
                  text='Url/Link:',
                  font='Arial 12')
LAbel_Url.place(x=20,y=100)
Entry_Url = Entry(Windos_tk,
                  relief='solid',
                  font='Arial 12')
Entry_Url.place(x=20,y=130)

Name_Usu_label = Label(Left_frame,
                       text='Nome do Usuario:',
                       font='Arial 12',
                       )
Name_Usu_label.place(x=20,y=200)

Entry_Name = Entry(Left_frame,
                   relief='solid',
                   font='Arial 12')
Entry_Name.place(x=20,y=230)

Button_Qrcode = Button(Left_frame,
                       text='Pronto',
                       font='Arial 12',
                       relief='solid',
                       command=Prepare_Qr)
Button_Qrcode.place(x=20,y=300)


if __name__ == '__main__':
    mainloop()