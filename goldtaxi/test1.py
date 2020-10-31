from tkinter import *
from tkinter import ttk
#from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox
import webbrowser
import sqlite3
conn = sqlite3.connect('data1base.db')
c = conn.cursor()
# empty list to later append the ids from the database
ids = []


class Cab:
    def __init__(self,window):
        self.window1 = window
        self.window1.geometry("1350x750")
        self.window1.title("Cab Booking System")
        self.window1.configure(background="pink")
        self.email_or_phone = []
        self.password = []

        self.frame1 = Frame(self.window1, height=690, width=1350, highlightbackground="black", highlightthickness=5, bg="pink")
        self.frame1.propagate(0)
        self.frame1.pack(side=TOP)

        self.label1 = Label(self.window1, font=('georgia 25 bold'), text="goldTAXI", fg="black", bg="pink", cursor="hand2")
        self.label1.place(x=10, y=10, width=200)
        self.label1.bind("<Button-1>", lambda e: self.callback("http://www.google.com"))

        self.button1 = Button(self.window1, font=("Arial", 12, "bold"), text="SignIn", bg="black", fg="gold",command=self.SignIn)
        self.button1.place(x=1000, y=15, width=80)
        self.button2 = Button(self.window1, font=("Arial", 12, "bold"), text="SignUp", bg="black", fg="gold",command=self.SignUp)
        self.button2.place(x=1150, y=15, width=80)
        self.label2 = Label(self.window1, font=("Arial", 25), text="Book a City Taxi to your destination in town", bg="pink",fg="green")
        self.label2.place(x=340, y=100)
        self.label3 = Label(self.window1, font=("Arial", 15), text="Choose from a range of categories and prices", bg="pink",fg="green")
        self.label3.place(x=430, y=150)
        self.canvas1 = Canvas(self.window1, bg='gold', height=150, width=1335, cursor='pencil')
        self.canvas1.place(x=5, y=280)
        self.label4 = Label(self.window1, font=("Arial", 25), text="A car for every occasion", bg="gold", fg="black")
        self.label4.place(x=500, y=300)
        self.label5 = Label(self.window1, font=("Arial", 13),text="greenTAXI offers city taxis, inter-city cabs, and local cabs at hourly packages", bg="gold",fg="black")
        self.label5.place(x=350, y=340)
        self.label6 = Label(self.window1, font=("Arial", 15), text="-CITY TAXI", bg="gold", fg="black")
        self.label6.place(x=350, y=380)
        self.label7 = Label(self.window1, font=("Arial", 15), text="-OUTSTATION", bg="gold", fg="black")
        self.label7.place(x=570, y=380)
        self.label8 = Label(self.window1, font=("Arial", 15), text="-RENTALS", bg="gold", fg="black")
        self.label8.place(x=820, y=380)
        self.canvas2 = Canvas(self.window1, bg='green', height=150, width=1335, cursor='pencil')
        self.canvas2.place(x=5, y=500)
        self.label8 = Label(self.window1, font=("Arial", 15), text="24/7 Customer Support", bg="green", fg="white")
        self.label8.place(x=40, y=520)
        self.label9 = Label(self.window1, font=("Arial", 10,),text="A dedicated 24x7 customer\nsupport team always at your\nservice to help solve any problem",bg="green", fg="white")
        self.label9.place(x=40, y=550)
        self.label10 = Label(self.window1, font=("Arial", 15), text="Your Safety First", bg="green", fg="white")
        self.label10.place(x=560, y=520)
        self.label11 = Label(self.window1, font=("Arial", 10),text="Keep your loved ones informed\nabout your travel routes or call\nemergency services when in need",bg="green", fg="white")
        self.label11.place(x=550, y=550)
        self.label12 = Label(self.window1, font=("Arial", 15), text="Top Rated Driver-Partners", bg="green", fg="white")
        self.label12.place(x=1070, y=520)
        self.label13 = Label(self.window1, font=("Arial", 10),text="All our driver-partners are\nbackground verified and trained to\ndeliver only the best experience",bg="green", fg="white")
        self.label13.place(x=1100, y=550)
        self.label14 = Label(self.window1, font=("Arial", 10),text="Copyright © 2020 goldTAXI Pvt. Ltd. All rights reserved.", bg="pink", fg="black")
        self.label14.place(x=940, y=660)
        self.menubar = Menu(self.window1)


    def callback(self,url):
        webbrowser.open_new(url)



    def SignIn(self):
        self.window2 = Tk()
        self.window2.geometry("1350x750")
        self.window2.title("Cab Booking System")
        self.window2.configure(background="pink")

        self.frame2 = Frame(self.window2, height=508, width=500, highlightbackground="black", highlightthickness=5, bg="gold")
        self.frame2.propagate(0)
        self.frame2.place(x=430,y=80)

        self.label1 = Label(self.window2, font=('georgia 25 bold'), text="goldTAXI", fg="black", bg="pink",cursor="hand2")
        self.label1.place(x=10, y=10, width=200)
        self.label1.bind("<Button-1>", lambda e: self.callback("http://www.google.com"))

        self.label2 = Label(self.window2, font=("Arial", 20), text="Get moving with goldTAXI", bg="gold", fg="black")
        self.label2.place(x=500, y=30)

        self.label3 = Label(self.window2, font=("Arial", 30), text="SignIn", bg="gold", fg="black")
        self.label3.place(x=610, y=120)
        self.label4 = Label(self.window2, font=("Arial", 8), text="Email or mobile number", bg="gold", fg="black")
        self.label4.place(x=600, y=180)
        self.entry1 = Entry(self.window2)
        self.entry1.place(x=600, y=200,width=150)
        self.label5 = Label(self.window2, font=("Arial", 8), text="Enter your password", bg="gold", fg="black")
        self.label5.place(x=600, y=230)
        self.entry2 = Entry(self.window2, show='*')
        self.entry2.place(x=600, y=250, width=150)
        self.label6 = Label(self.window2, font=("Arial", 8), text="Forgot Password?", bg="gold", fg="blue",cursor="hand2")
        self.label6.place(x=660, y=270)
        self.label6.bind("<Button-1>", lambda e: self.ForgotPassword())
        self.button1 = Button(self.window2, font=("Arial", 12, "bold"), text="Next", bg="black", fg="gold",command=self.condition)
        self.button1.place(x=600, y=305, width=150)
        self.label7 = Label(self.window2, font=("Arial", 8), text="Don't have an account?", bg="gold", fg="black")
        self.label7.place(x=600, y=335)
        self.label8 = Label(self.window2, font=("Arial", 8), text="Sign Up", bg="gold", fg="blue",cursor="hand2")
        self.label8.place(x=720, y=335)
        self.label8.bind("<Button-1>", lambda e: self.SignUp())

    def condition(self):
        if self.entry1.get() == "" or self.entry2.get() == "":
            messagebox.showerror("Error", "All fields required")
            self.window2.destroy()
        elif self.entry1.get() =="admin" and self.entry2.get() == "123":
            messagebox.showinfo("Details", f"Welcome : {self.entry1.get()}\nYour Passsword : {self.entry2.get()}")
            self.window2.destroy()
            self.portal1()

        elif self.entry1.get() == "cab" and self.entry2.get() == "123" :
            messagebox.showinfo("Details", f"Welcome : {self.entry1.get()}\nYour Passsword : {self.entry2.get()}")
            self.window2.destroy()
            self.portal2()
        else:
            messagebox.showerror("Error", "Invalid Username or Password\n Try Again")
            self.window2.destroy()

    def ForgotPassword(self):
        self.window3 = Tk()
        self.window3.geometry("1350x750")
        self.window3.title("Cab Booking System")
        self.window3.configure(background="Red")

        self.frame1 = Frame(self.window3, height=550, width=510, highlightbackground="black", highlightthickness=5, bg="gold")
        self.frame1.propagate(0)
        self.frame1.place(x=400, y=80)


        self.label1 = Label(self.window3, font=('georgia 25 bold'), text="goldTAXI", fg="black", bg="Red", cursor="hand2")
        self.label1.place(x=0, y=0, width=200)
        self.label1.bind("<Button-1>", lambda e: self.callback("http://www.google.com"))

        self.label2 = Label(self.window3, font=("Arial", 20), text="Forgot Password", bg="red", fg="black")
        self.label2.place(x=550, y=90)

        self.label3 = Label(self.window3, font=("Arial", 10), text="Enter your phone number / email (required)", bg="gold",fg="black")
        self.label3.place(x=545, y=168)
        self.entry1 = Entry(self.window3)
        self.entry1.place(x=590, y=198)

        self.label4 = Label(self.window3, font=("Arial", 10), text="Enter New Password (required)", bg="gold", fg="black")
        self.label4.place(x=572, y=230)
        self.entry2 = Entry(self.window3)
        self.entry2.place(x=590, y=260)

        self.label5 = Label(self.window3, font=("Arial", 10), text="Confirm New Password (required)", bg="gold",fg="black")
        self.label5.place(x=572, y=292)
        self.entry3 = Entry(self.window3)
        self.entry3.place(x=590, y=322)

        self.button1 = Button(self.window3, font=("Arial", 22, "bold"), text="Next", bg="black", fg="gold",
                              command=self.window3.destroy)
        self.button1.place(x=525, y=390, width=250)


    def portal1(self):
        self.window4 = Tk()
        self.window4.geometry("1350x750")
        self.window4.title("Cab Booking System")
        self.window4.configure(background="pink")

        self.label1 = Label(self.window4, font=('georgia 25 bold'), text="goldTAXI", fg="black", bg="pink",cursor="hand2")
        self.label1.place(x=10, y=10, width=200)
        self.label1.bind("<Button-1>", lambda e: self.callback("http://www.google.com"))
        self.label2=Label(self.window4,font=('arial 18'),text="Admin Account",fg="red",bg="pink" )
        self.label2.place(x=20,y=80)
        self.button1 = Button(self.window4, font=("Arial", 15), text="HELP", bg="steelblue", fg="gold", command=self.help)
        self.button1.place(x=30, y=150)
        self.button2 = Button(self.window4, font=("Arial", 15), text="ADD", bg="steelblue", fg="gold", command=self.add)
        self.button2.place(x=30, y=190)
        self.button3 = Button(self.window4, font=("Arial", 15), text="SEARCH", bg="steelblue", fg="gold", command=self.search)
        self.button3.place(x=30, y=230)

    def search(self):

        self.name = Label(self.window4, text="car no", font=('arial 12'),bg="pink",fg="black")
        self.name.place(x=300, y=380)

        # entry for  the name
        self.namenet = Entry(self.window4, width=30)
        self.namenet.place(x=500, y=380)
        # search button
        self.search = Button(self.window4, text="Search", width=25, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=500, y=410)

        # function to search

    def search_db(self):
        self.input = self.namenet.get()
        # execute sql

        sql = "SELECT * FROM avi WHERE car_no LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.car_no = self.row[1]
            self.car_type = self.row[2]
            self.car_name = self.row[3]
            self.car_rate = self.row[4]
            self.car_driver = self.row[5]
            self.car_driverno = self.row[6]
        # creating the update form
        self.uname = Label(self.window4, text="car no", font=('arial 12'),fg='black', bg='pink')
        self.uname.place(x=300, y=440)

        self.uage = Label(self.window4, text="car type", font=('arial 12'),fg='black', bg='pink')
        self.uage.place(x=300, y=460)

        self.ugender = Label(self.window4, text="car name", font=('arial 12'),fg='black', bg='pink')
        self.ugender.place(x=300, y=480)

        self.ulocation = Label(self.window4, text="car rate", font=('arial 12'),fg='black', bg='pink')
        self.ulocation.place(x=300, y=500)

        self.utime = Label(self.window4, text="car driver", font=('arial 12'),fg='black', bg='pink')
        self.utime.place(x=300, y=520)

        self.uphone = Label(self.window4, text="car driver no", font=('arial 12'),fg='black', bg='pink')
        self.uphone.place(x=300, y=540)

        # entries for each labels
        # filling the search result in the entry box to update
        self.ent1 = Entry(self.window4, width=30)
        self.ent1.place(x=500, y=440)
        self.ent1.insert(END, str(self.car_no))

        self.ent2 = Entry(self.window4, width=30)
        self.ent2.place(x=500, y=460)
        self.ent2.insert(END, str(self.car_type))

        self.ent3 = Entry(self.window4, width=30)
        self.ent3.place(x=500, y=480)
        self.ent3.insert(END, str(self.car_name))

        self.ent4 = Entry(self.window4, width=30)
        self.ent4.place(x=500, y=500)
        self.ent4.insert(END, str(self.car_rate))

        self.ent5 = Entry(self.window4, width=30)
        self.ent5.place(x=500, y=520)
        self.ent5.insert(END, str(self.car_driver))
        self.ent6 = Entry(self.window4, width=30)
        self.ent6.place(x=500, y=540)
        self.ent6.insert(END, str(self.car_driverno))


    def add (self):
        self.car_no = Label(self.window4, text="car no", font=('georgia 12'), fg='black', bg='pink')
        self.car_no.place(x=300, y=200)
        self.car_type = Label(self.window4, text="car type", font=('georgia 12'), fg='black', bg='pink')
        self.car_type.place(x=300, y=220)
        self.car_name = Label(self.window4, text="car name", font=('georgia 12'), fg='black', bg='pink')
        self.car_name.place(x=300, y=240)
        self.car_rate = Label(self.window4, text="car rate", font=('georgia 12'), fg='black', bg='pink')
        self.car_rate.place(x=300, y=260)
        self.car_driver = Label(self.window4, text="driver name", font=('georgia 12'), fg='black', bg='pink')
        self.car_driver.place(x=300, y=280)
        self.car_driverno = Label(self.window4, text="driver no", font=('georgia 12'), fg='black', bg='pink')
        self.car_driverno.place(x=300, y=300)
        # Entries for all labels
        self.car_no_ent = Entry(self.window4, width=30)
        self.car_no_ent.place(x=500, y=200)
        self.car_type_ent = Entry(self.window4, width=30)
        self.car_type_ent.place(x=500, y=220)
        self.car_name_ent = Entry(self.window4, width=30)
        self.car_name_ent.place(x=500, y=240)
        self.car_rate_ent = Entry(self.window4, width=30)
        self.car_rate_ent.place(x=500, y=260)
        self.car_driver_ent = Entry(self.window4, width=30)
        self.car_driver_ent.place(x=500, y=280)
        self.car_driverno_ent = Entry(self.window4, width=30)
        self.car_driverno_ent.place(x=500, y=300)
        # button to perform a command
        self.submit = Button(self.window4, text="submit", width=25, height=1, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=500, y=330)

        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT car_no FROM avi "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        # ordering the ids
        self.new = sorted(ids
        self.final_id = self.new[len(ids) - 1])
        # displaying the logs in our right frame
        self.box = Text(self.window4, width=50, height=5)
        self.box.place(x=800, y=200)
        self.box.insert(END, "Total car availble : " + str(self.final_id) + " \n")
        # funtion to call when the submit button is clicked

    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.car_no_ent.get()
        self.val2 = self.car_type_ent.get()
        self.val3 = self.car_name_ent.get()
        self.val4 = self.car_rate_ent.get()
        self.val5 = self.car_driver_ent.get()
        self.val6 = self.car_driverno_ent.get()
        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'avi' (car_no,car_type,car_name,car_rate,car_driver, car_driverno) VALUES(?, ?, ?,?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            messagebox.showinfo(
                "Success", "car type " + str(self.val2) + " avalaible")
            self.box.insert(END, 'having car no ' + str(self.val1))



    def portal2(self):
        self.window5 = Tk()
        self.window5.geometry("1350x750")
        self.window5.title("Cab Booking System")
        self.window5.configure(background="pink")
        self.frame2 = Frame(self.window5, height=508, width=500, highlightbackground="black", highlightthickness=5,bg="gold")
        self.frame2.propagate(0)
        self.frame2.place(x=50, y=100)
        # labels for the window
        self.heading = Label(self.window5, text="goldTaxi", font=('georgia 40 bold'), fg='black', bg='gold')
        self.heading.place(x=180, y=30)
        self.heading.bind("<Button-1>", lambda e: self.callback("http://www.google.com"))
        self.button1 = Button(self.window5, font=("Arial", 15), text="HELP", bg="black", fg="gold",command=self.help)
        self.button1.place(x=1200, y=20)
        self.checkbutton1=Checkbutton(self.window5, text="CITY TAXI", bg="gold")
        self.checkbutton1.place(x=130,y=200)
        self.checkbutton2=Checkbutton(self.window5, text="OUTSTATION", bg="gold")
        self.checkbutton2.place(x=250, y=200)
        self.checkbutton3=Checkbutton(self.window5, text="RENTALS", bg="gold")
        self.checkbutton3.place(x=390, y=200)
        self.pickup = Label(self.window5, text="PICKUP", font=('georgia 16 bold'), fg='black', bg='gold')
        self.pickup.place(x=130, y=300)
        self.drop = Label(self.window5, text="DROP", font=('georgia 16 bold'), fg='black', bg='gold')
        self.drop.place(x=130, y=340)
        self.when = Label(self.window5, text="WHEN", font=('georgia 16 bold'), fg='black', bg='gold')
        self.when.place(x=130, y=380)
        # Entries for all labels
        self.name_ent = Entry(self.window5, width=30)
        self.name_ent.place(x=280, y=300)
        self.age_ent = Entry(self.window5, width=30)
        self.age_ent.place(x=280, y=340)
        self.gender_ent = Entry(self.window5, width=30)
        self.gender_ent.place(x=280, y=380)
        # button to perform a command
        self.search = Button(self.window5,font=("Arial", 12, "bold"),text="Search Cab",width=30,height=2,fg="gold",bg='black')
        self.search.place(x=145, y=440)

    def help(self):
        self.window6 = Tk()
        self.window6.geometry("1350x750")
        self.window6.title("Cab Booking System")
        self.window6.configure(background="yellow")

        self.label1 = Label(self.window6, font=('georgia 25 bold'), text="goldTAXI", fg="black", bg="yellow",cursor="hand2")
        self.label1.place(x=0, y=0, width=200)
        self.label1.bind("<Button-1>", lambda e: self.callback("http://www.google.com"))

        self.label2 = Label(self.window6, font=("Arial", 18), text="Having trouble?", bg="yellow", fg="black")
        self.label2.place(x=100, y=100)
        self.label3 = Label(self.window6, font=("Arial", 18), text="We're here to help", bg="yellow", fg="black")
        self.label3.place(x=100, y=130)
        self.label4 = Label(self.window6, font=("Arial", 15), text="Describe your issue", bg="white", fg="black")
        self.label4.place(x=100, y=180)
        self.c = ["Have issues with previour ride", "Legal, Terms & Conditiopns","FAQs"]
        self.cb = ttk.Combobox(self.window6, values=self.c, width=10)
        self.cb.place(x=280, y=180, width=160, height=30)
        self.cb.current(0)

    def SignUp(self):
        self.window7 =Tk()
        self.window7.geometry("1350x750")
        self.window7.title("Cab Booking System")
        self.window7.configure(background="pink")
        def Msg():
            messagebox.showinfo("Details",f"Agreed the Terms & Condition and Privacy Policy")

        self.frame2 = Frame(self.window7, height=550, width=510, highlightbackground="black", highlightthickness=5, bg="gold")
        self.frame2.propagate(0)
        self.frame2.place(x=400, y=80)

        self.label1 = Label(self.window7, font=('georgia 25 bold'), text="goldTAXI", fg="black", bg="pink",cursor="hand2")
        self.label1.place(x=0, y=0, width=200)
        self.label1.bind("<Button-1>", lambda e: self.callback("http://www.google.com"))
        self.label11 = Label(self.window7, font=("Arial", 20), text="Get moving with goldTAXI", bg="gold", fg="black")
        self.label11.place(x=500, y=30)
        self.label2 = Label(self.window7, font=("Arial", 25), text="SingUp", bg="gold", fg="black")
        self.label2.place(x=590, y=100)
        self.label3 =Label(self.window7,font=("Arial",10),text="Enter your phone number (required)",bg="gold",fg="black")
        self.label3.place(x=545,y=168)
        self.entry1 = Entry(self.window7)
        self.entry1.place(x=590,y=198)
        self.label4 = Label(self.window7, font=("Arial", 10), text="Enter your email (required)", bg="gold", fg="black")
        self.label4.place(x=572, y=230)
        self.entry2 = Entry(self.window7)
        self.entry2.place(x=590, y=260)
        self.label5 = Label(self.window7, font=("Arial", 14), text="Add your details to create an account", bg="gold", fg="black")
        self.label5.place(x=490, y=300)
        self.label6 = Label(self.window7, font=("Arial", 10), text="First name (required)", bg="gold", fg="black")
        self.label6.place(x=520, y=330)
        self.entry3 = Entry(self.window7)
        self.entry3.place(x=550, y=360,width=70)
        self.label7 = Label(self.window7, font=("Arial", 10), text="Last name (required)", bg="gold", fg="black")
        self.label7.place(x=660, y=330)
        self.entry4 = Entry(self.window7)
        self.entry4.place(x=690, y=360,width=70)
        self.label8 = Label(self.window7, font=("Arial", 14), text="Enter a password (required)", bg="gold", fg="black")
        self.label8.place(x=530, y=400)
        self.entry5 = Entry(self.window7)
        self.entry5.place(x=590, y=440)
        self.button3 = Button(self.window7, font=("Arial", 22, "bold"), text="Next", bg="black", fg="gold",command=self.SignIn)
        self.button3.place(x=525, y=490, width=250)
        self.label9 = Label(self.window7, font=("Arial", 12), text="By continuing, I confirm that I have read and agree to the", bg="gold", fg="black")
        self.label9.place(x=473, y=560)
        self.label10 = Label(self.window7, font=("Arial", 9), text="Terms & Conditions and Privacy Policy.", bg="gold", fg="blue")
        self.label10.place(x=473, y=580)
        self.chb = Checkbutton(self.window7, text="Agree",bg="gold", command=Msg)
        self.chb.place(x=700, y=580)


window = Tk()
obj = Cab(window)
window.mainloop()






