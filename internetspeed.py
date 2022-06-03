from cProfile import label
from tkinter import*


def speedcheck():
    import speedtest
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" mbps"
    up = str(round(sp.upload()/(10**6),3))+" mbps"
    button_down.config(text=down)
    button_up.config(text=up)

sp = Tk()
sp.title ("INTERNET SPEED TESTER")
sp.geometry("500x500")
sp.config(bg= "#2F3C7E")

lab = Label(sp , text="INTERNET SPEED TEST", font=("Harmony",38,"bold",),bg="#2F3C7E",fg="#E2D1F9")
lab.place (x=10,y=40,height=50,width=500)

lab = Label(sp , text="DOWNLOADING SPEED", font=("Harmony",20,"bold",),bg="#2F3C7E",fg="#E2D1F9")
lab.place (x=50,y=130,height=50,width=380)

button_down = Button(sp ,text="00",font=("Harmony",30,"bold"),fg="#2F3C7E")
button_down.place(x=170,y=220,height=40,width=100)

lab = Label(sp , text="UPLOADING SPEED", font=("Harmony",20,"bold",),fg="#E2D1F9",bg="#2F3C7E")
lab.place (x=50,y=290,height=50,width=380)

button_up = Button(sp ,text="00",font=("Harmony",30,"bold"),fg="#2F3C7E")
button_up.place(x=170,y=360,height=40,width=100)

button = Button(sp ,text="CHECK SPEED",font=("Harmony",20,"bold"),relief=RAISED,bg="#E2D1F9",fg="#2F3C7E",command=speedcheck)
button.place(x=110,y=420,height=50,width=250)









sp.mainloop()