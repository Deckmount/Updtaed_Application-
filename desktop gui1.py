from tkinter import *
from  tkinter import  ttk
import matplotlib.pyplot as plt
import pymongo
from pymongo import MongoClient
import numpy as np



window = Tk()
window.geometry('450x350')
window.title('Button Widget')
window.configure(bg='aquamarine')

#GLOBAL VARIABLE DECLARED
namev=StringVar()
contact=StringVar()
email=StringVar()
address=StringVar()
gender=IntVar()
city=StringVar()
password=StringVar()
mode=StringVar()
humidifierstate=StringVar()
patientmode=StringVar()
maskstate=StringVar()
v = DoubleVar()
v1 = DoubleVar()

def sub():
    cluster= MongoClient("mongodb+srv://root:root@cluster0.ezpn4es.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["test"]
    collection=db["student"]
    dic={
        'name' : namev.get(),
        'contact no' : contact.get(),
        'email id' : email.get(),
        'address' : address.get(),
        'gender' : gender.get(),
        'city' : city.get(),
        'password' : password.get()
    }
    collection.insert_one(dic)

def sub1():
    cluster= MongoClient("mongodb+srv://root:root@cluster0.ezpn4es.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["test"]
    collection=db["student"]
    dic={
        'Workmode' : mode.get(),
        'Humidifier': humidifierstate.get(),
        'Patient' : patientmode.get(),
        'Mask Type' : maskstate.get(),
        'Pressure Set': v.get(),
        'Ramp Time': v1.get()
    }
    collection.insert_one(dic)

def clearFunc():
    mode.set("")
    humidifierstate.set("")
    patientmode.set("")
    maskstate.set("")
    v.set("0")
    v1.set("0")

def clearFunc1():
    namev.set("")
    contact.set("")
    address.set("")
    email.set("")
    city.set("")
    password.set("")

#GRAPH PAGE
def graphpage():
    
   


# create data
    x = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P']
    y1 = np.array([10, 20, 10, 30,10, 20, 10, 30,10, 20, 10, 30,10, 20, 10, 30])
    y2 = np.array([20, 25, 15, 25,20, 25, 15, 25,20, 25, 15, 25,20, 25, 15, 25])
    y3 = np.array([12, 15, 19, 6,12, 15, 19, 6,12, 15, 19, 6,12, 15, 19, 6])
    y4 = np.array([10, 29, 13, 19,10, 29, 13, 19,10, 29, 13, 19,10, 29, 13, 19])

    # plot bars in stack manner
    plt.bar(x, y1, color='BLUE')
    plt.bar(x, y2, bottom=y1, color='SKYBLUE')
    plt.bar(x, y3, bottom=y1+y2, color='GREY')
    plt.bar(x, y4, bottom=y1+y2+y3, color='g')
    plt.xlabel("Teams")
    plt.ylabel("Score")
    plt.title("Scores by Teams in 4 Rounds")
    plt.show()

   

#SETTING PAGE FUNCTION
def setting_page():
    newWindow = Toplevel(window)
    newWindow.title("SETTING")
    newWindow.geometry("250x150")

    #WORKMODE WIDGET BOX
    workmode = Label(newWindow, text="Work Mode",borderwidth=5, relief="solid",width=10, font=('Times', 30, "bold")).place(x=60, y=30)
    modechoosen=ttk.Combobox(newWindow, width=12,font=('Times', 20,"bold"), textvariable=mode)
    modechoosen['values'] = (' APAP', ' CPAP')
    modechoosen.current()
    modechoosen.place(x=90,y=95)

    #HUMIDIFIER WIDGET BOX
    humidifier = Label(newWindow, text="Humidifier",borderwidth=5, relief="solid",width=10, font=('Times', 30, "bold")).place(x=580, y=30)
    modechoosen=ttk.Combobox(newWindow, width=12,font=('Times', 20,"bold"), textvariable=humidifierstate)
    modechoosen['values'] = ('ON', ' OFF')
    modechoosen.current()
    modechoosen.place(x=610,y=95)

    #PATIENT WIDGET BOX
    patientname = Label(newWindow, text="Patient",borderwidth=5, relief="solid",width=10, font=('Times', 30, "bold")).place(x=60, y=230)
    modechoosen=ttk.Combobox(newWindow, width=12,font=('Times', 20,"bold"), textvariable=patientmode)
    modechoosen['values'] = (' MALE', ' FEMALE')
    modechoosen.current()
    modechoosen.place(x=90,y=295)

    #MASK TYPE WIDGET BOX
    maskname = Label(newWindow, text="Mask Type",borderwidth=5, relief="solid",width=10, font=('Times', 30, "bold")).place(x=580, y=230)
    modechoosen=ttk.Combobox(newWindow, width=12,font=('Times', 20,"bold"), textvariable=maskstate)
    modechoosen['values'] = ('NASAL', 'FULL FACE', 'PILLOW')
    modechoosen.current()
    modechoosen.place(x=610,y=295)

    #PRESSURE SETTING WIDGET BOX
    pressuresetting = Label(newWindow, text="Pressure Setting",borderwidth=5, relief="solid",width=13, font=('Times', 30, "bold")).place(x=50, y=430)
    scale = Scale(newWindow, variable = v, from_ = 6, to = 30,activebackground='red',fg='green', font=('Times', 20, "bold"),length=200,orient = HORIZONTAL).place(x=100,y=495) 

    #RAMP SETTING WIDGET BOX
    rampsetting = Label(newWindow, text="Ramp Time",borderwidth=5, relief="solid",width=13, font=('Times', 30, "bold")).place(x=550, y=430)
    scale = Scale(newWindow, variable = v1, from_ = 0, to = 60,activebackground='red',fg='green', font=('Times', 20, "bold"),length=200,orient = HORIZONTAL).place(x=600,y=495) 

    #RESET BUTTON WIDGET
    border1 = LabelFrame(newWindow, bd=5, bg="black")
    btn1 = Button(border1, text="RESET", width=8,command=clearFunc,
              bg="skyblue",padx=80,pady=20,font=("Times",12,"bold"))
    btn1.pack()
    border1.place(x=980,y=490)

    #SUBMIT BUTTON WIDGET   
    border1 = LabelFrame(newWindow, bd=5, bg="black")
    btn1 = Button(border1, text="SUBMIT", width=8,command=sub1,
              bg="skyblue",padx=80,pady=20,font=("Times",12,"bold"))
    btn1.pack()
    border1.place(x=980,y=590)

    #EXIT BUTTON WIDGET
    border1 = LabelFrame(newWindow, bd=5, bg="black")
    btn1 = Button(border1, text="EXIT", width=8,command=newWindow.destroy,
              bg="skyblue",padx=80,pady=20,font=("Times",12,"bold"))
    btn1.pack()
    border1.place(x=980,y=690)
     

#REGISTRATION PAGE FUNCTION
def registration_page():
    newWindow = Toplevel(window)
    newWindow.title("REGISTRATION")
    newWindow.geometry("200x150")

    
    label=Label(newWindow,width="300", text="Please enter details below", bg="orange",fg="white").pack()

    #name widgets box
    name = Label(newWindow, text="Enter Name *",font=('Times', 20,"bold")).place(x=30, y=50)
    e1 = Entry(newWindow,width=40,text=namev,font=('Times', 12)).place(x=280, y=58)

    #contact widget box
    Contact = Label(newWindow, text="Contact *", font=('Times', 20, "bold")).place(x=30, y=130)
    e1 = Entry(newWindow, width=40,text=contact,font=('Times', 12)).place(x=280, y=138)

    #email widget box
    Email = Label(newWindow, text="Email *", font=('Times', 20, "bold")).place(x=30, y=210)
    e1 = Entry(newWindow, width=40,text=email,font=('Times', 12)).place(x=280, y=217)

    #address widget box
    Address = Label(newWindow, text="Address *", font=('Times', 20, "bold")).place(x=30, y=290)
    e1 = Entry(newWindow, width=40,text=address,font=('Times', 12)).place(x=280, y=297)

    #gender widget box with button
    Gender = Label(newWindow, text="Gender *", font=('Times', 20, "bold")).place(x=30, y=360)
    Radiobutton(newWindow,text="Male",font=('Times', 18),variable=gender,value=1).place(x=280,y=360)
    Radiobutton(newWindow,text="Female",font=('Times', 18),variable=gender,value=2).place(x=410,y=360)

    #city widget box with table
    City = Label(newWindow, text="State *", font=('Times', 20, "bold")).place(x=30, y=440)
    statechoosen=ttk.Combobox(newWindow, width=27,font=('Times', 12), textvariable=city)
    statechoosen['values'] = (' Maharashtra',
                              ' Delhi',
                              ' Haryana',
                              ' UP',
                              ' Bihar',
                              ' Punjab',
                              ' Gujarat',
                              ' Karnataka',
                              ' Rajasthan')
    statechoosen.current()
    statechoosen.place(x=280,y=444)

    #password widget box
    Password = Label(newWindow, text="Enter Password *", font=('Times', 20, "bold")).place(x=30, y=520)
    e1 = Entry(newWindow, width=40,text=password,font=('Times', 12)).place(x=280, y=528)


    #RESET BUTTON WIDGET
    border1 = LabelFrame(newWindow, bd=2, bg="orange")
    btn1 = Button(border1, text="RESET", width=8,command=clearFunc1,
              bg="Orange",padx=60,pady=10,font=("Times",12,"bold"))
    btn1.pack()
    border1.place(x=80,y=590)

    
    #button widgets with border
    border1 = LabelFrame(newWindow, bd=2, bg="orange")
    btn1 = Button(border1, text="SUBMIT", width=8,command=sub,
              bg="Orange",padx=60,pady=10,font=("Times",12,"bold"))
    btn1.pack()
    border1.place(x=350,y=590)

    newWindow.mainloop()


#MAIN MENU CODE FOR MAIN SCREEN
label = Label(window, text="MAIN MENU",width=40, font=('Times', 46,"bold")).place(x=0, y=10)

#BUTTONS PRESENT IN MAIN SCREEN
#Start button widgets
border1 = LabelFrame(window, bd=6, bg="skyblue")
btn1 = Button(border1, text="GRAPH", width=8,command=graphpage,
              fg="black",padx=100,pady=10,font=("Times",24,"bold"))
btn1.pack()
border1.place(x=520,y=130)

#Setting button widget
border2 = LabelFrame(window, bd=6, bg="skyblue")
btn2 = Button(border2, text="SETTING", width=8,command=setting_page,
              fg="black",padx=100,pady=10,font=("Times",24,"bold"))
btn2.pack()
border2.place(x=520,y=250)

#Register button widget
border3 = LabelFrame(window, bd=6, bg="skyblue")
btn3 = Button(border3, text="REGISTER", width=8,command=registration_page,
              fg="black",padx=100,pady=10,font=("Times",24,"bold"))
btn3.pack()
border3.place(x=520,y=380)

#Login button widget
border4 = LabelFrame(window, bd=6, bg="skyblue")
btn4 = Button(border4, text="LOGIN", width=8,
              fg="black",padx=100,pady=10,font=("Times",24,"bold"))
btn4.pack()
border4.place(x=520,y=510)

#Exit button widget
border5 = LabelFrame(window, bd=6, bg="skyblue")
btn5 = Button(border5, text="EXIT", width=8,
              fg="black",padx=100,pady=10,command=window.destroy,font=("Times",24,"bold"))
btn5.pack()
border5.place(x=520,y=640)

window.mainloop()


    





