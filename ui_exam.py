from tkinter import*
from tkinter import messagebox
from dbexam import Database
db1=Database("C:/test/db_exam.db")

#========================
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
    ent_fname.focus_set()

def insert():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    if email=="" or password=="":
        eror_1=messagebox.showerror("Eror","You should fill all the blanks")
        return
    db1.insert(fname,lname,email,password)
    clear()
def signin():
    email=ent_email.get()
    password=ent_password.get()
    if email=="" or password=="":
        eror_1=messagebox.showerror("Eror","You should fill all the blanks")
        return
    record=db1.select_records(email,password)
    if len(record) == 0:
        messagebox.showinfo("Warning", "No person sing up")
    else:
        win2=Tk()
        win2.geometry("200x200")
        win2.resizable(0,0)
        lbl_welcome=Label(win2,text="Welcome",font="arial 12 bold")
        lbl_welcome.place(x=70,y=100)
        win2.mainloop()

#========================
win= Tk()
win.geometry("600x400")
win.title("login form")
win.resizable(0,0)
win.config(bg="#2e8b57")

lbl_fname=Label(win,text="Fname:",font="arial 17 bold",bg="#2e8b57",fg="white")
lbl_fname.place(x=100,y=20)
ent_fname=Entry(win,font="arial 17 bold")
ent_fname.place(x=200,y=20)

lbl_lname=Label(win,text="Lname:",font="arial 17 bold",bg="#2e8b57",fg="white")
lbl_lname.place(x=100,y=80)
ent_lname=Entry(win,font="arial 17 bold")
ent_lname.place(x=200,y=80)

lbl_email=Label(win,text="*Email:",font="arial 17 bold",bg="#2e8b57",fg="white")
lbl_email.place(x=100,y=140)
ent_email=Entry(win,font="arial 17 bold")
ent_email.place(x=200,y=140)

lbl_password=Label(win,text="*Password:",font="arial 17 bold",bg="#2e8b57",fg="white")
lbl_password.place(x=65,y=200)
ent_password=Entry(win,font="arial 17 bold")
ent_password.place(x=200,y=200)
#=====================================================

btn_signup=Button(text="sign up", font = "arial 17 bold", width=10,command=insert)
btn_signup.place(x=120,y=270)

btn_signin=Button(text="sign in", font = "arial 17 bold", width=10,command=signin)
btn_signin.place(x=315,y=270)
win.mainloop()