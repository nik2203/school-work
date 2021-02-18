import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',passwd='#Goddamn2203',database='school')

def view_data(var1):
    var1.execute('SELECT * from employee')
    res=var1.fetchall()
    for i in res:
        print('ID=',i[0],'Last Name=',i[1],'Title=',i[2],'Manager=',i[3],'Department=',i[4],'Monthly Salary=',i[5],'Annual Salary=',i[6],sep=' ',end='\n')

def add_new(var1,details):
    sql_insert="insert into employee values %s"%(details)
    var1.execute(sql_insert)
    con.commit()
    
def update_manager(var1,var2,var3):
    sql_up_man="update employee set Manager='%s' where Manager like '%s'"%(var3,var2)
    var1.execute(sql_up_man)
    con.commit()

def update_dep(var1,var2,var3):
    sql_up_dep="update employee set Department='%s' where Department like '%s'"%(var3,var2)
    var1.execute(sql_up_dep)
    con.commit()

def update_sal(var1,var2,var3):
    sql_up_sal="update employee set Monthly_Salary='%s' where Last_Name='%s'"%(str(var3),var2)
    sql_up_sal2="update employee set Annual_Salary='%s' where Monthly_Salary like '%s'"%(str(var3*12),var3)
    var1.execute(sql_up_sal)
    var1.execute(sql_up_sal2)
    con.commit()

def delete(var1,name):
    sql_del="delete from employee where Last_Name like '%s'"%(name)
    var1.execute(sql_del)
    con.commit()

def find_emp(var1,name):
    sql_find="select * from employee where Last_Name like '%s'"%(name)
    var1.execute(sql_find)
    rows=var1.fetchall()
    if len(rows)>0:
        print(rows)
    else:
        print('No employee found')

concur=con.cursor()

if con.is_connected():
    x=input('Do you want to begin? (y/n)\n')
    while x=='y' or x=='Y':
        prog=input('Do you want to:\n'
                '1. View all records\n'
                '2. Add a new employee to the table\n'
                '3. Update details\n'
                '4. Delete a user\n'
                '5. Search for an employee\n')
        if prog=='1':        
            view_data(concur)        
        if prog=='2':
            y=input('enter new employee details as a tuple\n')
            add_new(concur,y)
        if prog=='3':
            prog1=input('Do you want to update:\n'
                     'a. Manager\n'
                     'b. Department\n'
                     'c. Salary\n')
            if prog1=='a':
                y=input('enter the manager to be updated\n')
                y2=input('enter updated manager\n')
                update_manager(concur,y,y2)
            if prog1=='b':
                y=input('enter the department to be updated\n')
                y2=input('enter updated department\n')
                update_dep(concur,y,y2)
            if prog1=='c':
                y=input('enter the employee\'s salary to be updated\n')
                y2=int(input('enter updated salary\n'))
                update_sal(concur,y,y2)
        if prog=='4':
            y=input('enter employee to be deleted\n')
            delete(concur,y)
        if prog=='5':
            y=input('enter employee to find\n')
            find_emp(concur,y)
        x=input('Do you want to continue (y/n)\n')
    else:
        con.close()
        print('Connection closed')
else:
    print('connection not establised')
