# 引入 tkinter 模組
#import tkinter as tk
from tkinter import*

def Cauculate():
    a=eval(E_amount.get())
    b=eval(E_years.get())
    c=eval(E_intRate.get())
    d=a/((1-pow((1+(c/1200)),(-b*12)))/(c/1200))
    L6.config(text=('每月攤還新台幣 '+format(d,',.2f')+'元'),font=4)

# 建立主視窗 Frame
#root =tk.Tk()
root = Tk()

root.title('銀貸清償計算系統(Python 視窗版)')
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
w=500
h=145
x=(sw-w)/2
y=(sh-h)/2
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
#圖片路徑
#root.iconbitmap('C:/Users/user/Downloads/1.ico')
#root.iconbitmap('PingDa.ico')
L1=Label(root,text='#本程式是銀貸清償計算系統#',font=4)
L2=Label(root,text='請輸入貸款總金額、貸款總年數及貸款年利率:',font=4)
L1.grid(row=0,columnspan=2,sticky='w')
L2.grid(row=1,columnspan=2,sticky='w')
L3=Label(root,text='貸款總金額例如:5,000,000，請輸入:5000000)',font=4)
L4=Label(root,text='貸款總年數(例如:貸款二十年，請輸入:20)',font=4)
L5=Label(root,text='貸款年利率(例如:年利率35，請輸入:35)',font=4)
L3.grid(row=2,sticky='w')
L4.grid(row=3,sticky='w')
L5.grid(row=4,sticky='w')
E_amount=Entry(root)
E_years=Entry(root)
E_intRate=Entry(root)
E_amount.grid(row=2,column=1)
E_years.grid(row=3,column=1)
E_intRate.grid(row=4,column=1)
B1=Button(root,text='計算>>',font=4,command=Cauculate)
B1.grid(row=5,sticky='w',padx=3)
L6=Label(root,text='每月攤還...',font=4)
L6.grid(row=5,sticky='e')
root.mainloop()
