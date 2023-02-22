from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

L1=Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

###########
def Button2():
    text='ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text) 


FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='เงินมีอยู่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
#B2.place(x=50,y=200)
############

GUI.mainloop()
