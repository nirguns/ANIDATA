
from tkinter import *
import os

def Restart():
    return os.system("sudo shutdown -r now")
def restart_time():
    return os.system("sudo shutdown -r 5")
def logout():
    return os.system("sudo shutdown -l")
def shutdown():
    return os.system("sudo shutdown -r now")

st = Tk()
st .title("shutdown app")
st.geometry("500x500")
st.config(bg="#2F3C7E")

r_button = Button(st,text="SHUTDOWN APP USING PYYTHON",font=("times new roman",20,"bold"))
r_button.place(x=50,y=30,height=50,width=400)

r_button = Button(st,text="Restart",font=("times new roman",25,"bold"),relief=RAISED,cursor="plus",command=Restart)
r_button.place(x=170,y=130,height=50,width=130)

rt_button = Button(st,text="Restart_time",font=("times new roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=170,y=220,height=50,width=130)

lg_button = Button(st,text="log out",font=("times new roman",25,"bold"),relief=RAISED,cursor="plus",command= logout)
lg_button.place(x=170,y=310,height=50,width=130)

st_button = Button(st,text="shutdown",font=("times new roman",25,"bold"),relief=RAISED,cursor="plus",command= shutdown)
st_button.place(x=170,y=400,height=50,width=130)
st.mainloop()
