from tkinter import *

w = Tk()
Barra = Scrollbar(w)
Canva = Canvas(w,yscrollcommand=Barra.set)
Barra.config(command=Canva.yview)

Barra.pack(side='right',fill='y')

Fram = Frame(Canva)
Canva.pack(side='top',fill='both',expand=True)
Canva.create_window(0,0,window=Fram)
for ra in range(200):
    LA = Label(text='Cuscus')
    LA.grid(column=ra,row=0)
mainloop()