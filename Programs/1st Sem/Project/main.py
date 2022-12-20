from distutils import command
import math
import datetime as dt
import tkinter as tk
from functools import partial
import mysql.connector as msc




'''
def show_pat(cod):
    sql='select p.First_Name,p.Last_Name from patients p,staff s WHERE p.Doc_code=s.{0};'.format(cod)
    cur.exexcute(sql)
    rows=cur.fetchall()
    return rows
'''
def openNewWindow(status,rows):
    posn=rows[4]
    if status:
        if posn=='Staff':
            new = tk.Toplevel(root)
            new.title("Profile")
            new.geometry("500x300")
            tk.Label(new,text ="This is the staff page").pack()
        else:
            new = tk.Toplevel(root)
            new.title("Profile")
            new.geometry("500x300")
            tk.Label(new,text ="This is the profile page").pack()
    else:
        new = tk.Toplevel(root)
        new.title("Error Page")
        new.geometry("500x300")
        tk.Label(new,text ="ERROR\n \
            You are attempting to use an unauthorised login.\n This will be reported to the relevant authorities").pack()

def user_ver(status,username,password):
    u=username.get()
    p=password.get()
    sql='select * from staff WHERE First_Name={0} AND Emp_Code={1};'.format(username.get(),password.get())
    
    cur.execute(sql)
    rows=cur.fetchall()
    if len(rows)==0:
        status=False
    else:
        status=True
    return status,rows
    
    openNewWindow(status)
    print(status,u,p)

'''
def pat_q(col,val):
    sql='select * from patients WHERE {0}={1};'.format(col,val)
    cur.execute(sql)
    rows=cur.fetchall()
    return rows

def staff_q(col,val):
    sql='select * from staff WHERE {0}={1};'.format(col,val)
    cur.excute(sql)
    rows=cur.fetchall()
    return rows

def med_q(x):
    sql='select * from prescription where {0}={1};'.format(x)
    cur.execute(sql)
    rows=cur.fetchall()
    return rows

def add_pat(x):
    sql='insert into patients {0};'.format(x)
    cur.execute(sql)
    con.commit()

def add_staff(x):
    sql='insert into staff {0};'.format(x)
    cur.execute(sql)
    con.commit()

def add_med(x):
    sql=insert into precription {0};'.format(x)
    cur.execute(sql)
    con.commit()

def bill(x):
    sql='select Stay*Cost_Per_Day as 'Stay Amount';'

'''

status=False
root=tk.Tk()
root.title('Patient Management System')
root.resizable(False,False)

'''bg=tk.PhotoImage(file='login_page.png')

canv=tk.Canvas(root,width=1280,height=853)
canv.pack(fill='both', expand=True)
canv.create_image(0,0,image = bg)
'''


try:
    con=msc.connect(host='localhost', user='root', passwd='#Qwerty112358', database='school')
    cur=con.cursor()
    status=None

    username=tk.StringVar()
    password=tk.StringVar()
    usernamelabel=tk.Label(root, text="Username:",padx=20).grid(row=0, column=0)
    passwordlabel=tk.Label(root,text='Password:').grid(row=1,column=0)
    name=tk.Entry(root,textvariable=username,width=35,borderwidth=2)
    name.grid(column=2,row=0,padx=20,pady=20)
    passw=tk.Entry(root,textvariable=password,width=35,borderwidth=2,show='*')
    passw.grid(column=2,row=1)

    user_ver=partial(user_ver,status,username,password)

    con=tk.Button(root,text='Confirm',padx=10,command=user_ver,pady=5)
    can=tk.Button(root,text='Cancel',command=root.quit,padx=10,pady=5)
    can.grid(column=1,row=3)
    con.grid(column=0,row=3)

    root.mainloop()

except:
    print('A connection error was encountered')

