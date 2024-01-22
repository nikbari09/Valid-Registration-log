from tkinter import *
from sqlconnection import *
B1=""
B2=""
name=""
email=""
age=""
password=""
email_sign_in=""
password_sign_in=""

root=Tk()
root.title("Registration form")
root.geometry("500x500")
root.resizable(0,0)

heading=Label(root,text="User Registration Form:",font="arial 15 bold").pack()

def Register():
    Label1=Label(root,text="Enter your name:")
    Label1.pack()
    E1=Entry(root)
    E1.pack()
    Label2=Label(root, text="Enter your Email:")
    Label2.pack()
    E2=Entry(root)
    E2.pack()
    Label3=Label(root, text="Enter your Age:")
    Label3.pack()
    E3=Entry(root)
    E3.pack()
    Label4=Label(root,text="Enter your Password:")
    Label4.pack()
    E4=Entry(root,textvariable=password,show="*")
    E4.pack()
    def submit():
        name = E1.get()
        email = E2.get()
        age = E3.get()
        password = E4.get()
        print("Entered name is:",name)
        print("Entered email is:", email)
        print("Entered age is:", age)
        print("Entered password is:", password)

        mycursor = myDB.cursor()
        sql = "INSERT INTO students(name,email,age,password) VALUES(%s,%s,%s,%s)"
        value = (name, email, age, password)
        mycursor.execute(sql, value)
        myDB.commit()

        Label(root,text="you have registered successfully!!!!",font="arial 18 bold",fg="green").pack()
        E1.destroy()
        E2.destroy()
        E3.destroy()
        E4.destroy()
        def remove_text():
            Label1.config(text="")
            Label2.config(text="")
            Label3.config(text="")
            Label4.config(text="")
        remove_text()
        B1.destroy()

    B1=Button(root,text="submit",command=submit)
    B1.pack(pady=5)

Button(root,text="Register",command=Register).pack(pady=5)

def login():
    Label5=Label(root,text="Enter your Email:")
    Label5.pack()
    E5=Entry(root)
    E5.pack()
    Label6=Label(root,text="Enter your Password:")
    Label6.pack()
    E6=Entry(root,textvariable=password_sign_in,show="*")
    E6.pack()
    def sign_in():
        email_sign_in=E5.get()
        password_sign_in=E6.get()
        print("Entered email is:",email_sign_in)
        print("Entered password is:",password_sign_in)

        mycursor = myDB.cursor()
        mycursor.execute("SELECT email,password FROM students WHERE email='" + email_sign_in + "' OR password= '" + password_sign_in + "'")
        myresult=mycursor.fetchone()
        print(myresult)
        database_email=myresult[0]
        print(database_email)
        database_password=myresult[1]
        print(database_password)

        if(database_email == email_sign_in and database_password == password_sign_in  ):
            Label(root,text="USER EXISTS!!!!",fg="green",font="arial 18 bold").pack()
            E5.destroy()
            E6.destroy()
            B2.destroy()
        else:
            Label(root,text="USER DOES NOT EXISTS!!!!",fg="red",font="arial 18 bold").pack()
            E5.destroy()
            E6.destroy()
            B2.destroy()

        def remove_text():
            Label5.config(text="")
            Label6.config(text="")

        remove_text()

    B2=Button(root,text="sign in",command=sign_in)
    B2.pack()
Button(root,text="login",command=login).pack()

root.mainloop()