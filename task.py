import sqlite3
from emolyee import employe

#for the database i use sqlite3 to create the database and manipulate it's data

conn = sqlite3.connect("db.db")
c=conn.cursor()
# this methon should be called only once
# the create method initialize the database with the attribute needed
# the database has the id identity means it's incremented at every new insertion
# the email is uniqe attribute cuz it cannot be duplicated
# the accces to resources such as printer, memory, and phone is set to zero by default once there is new record in the database but it can be modified later
# this list called emolyees holds all the objects of employe once i insert it into the database i insert on object in this list

def create():
    c.execute ("""  CREATE TABLE employees (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    email text UNIQE,
    phone_number text,
    printer_access integer  default 0 ,
    storage_access integer  default 0,
    phone_access integer  default 0
    )""")
    conn.commit()
    print('The database created ^_^ you can insret now you your records')


# the insert method is responsable about inserting data in the databse and inserting it also in the list of employees
def insert(name,
           email,
           phone):
    current_employee = employe(name, email,phone)
    c.execute ("INSERT INTO employees (name, email , phone_number) VALUES ( '{}','{}','{}')".format(name,email,phone))
    conn.commit()

# the methon prints all the records in the database and the list
def show_all_employee():

    c.execute("SELECT * FROM employees")
    print(c.fetchall())

# the method get the record by it's email cuz it's uniqe and then change it's value to 1
# 0 means no accces and 1 means there is accces to the printer
def turn_on_print_access (email):
    c.execute("UPDATE employees SET printer_access = 1 WHERE  email = email")

    conn.commit()

# the method get the record by it's email cuz it's uniqe and then change it's value to 0
# 0 means no accces and 1 means there is accces to the printer
def turn_off_print_access (email):
    c.execute("UPDATE employees SET printer_access = 0 WHERE  email = email")

    conn.commit()

# the method get the record by it's email cuz it's uniqe and then change it's value to 0
# 0 means no accces and 1 means there is accces to the phone
def turn_off_phone_access (email):
    c.execute("UPDATE employees SET phone_access = 0 WHERE  email = email")

    conn.commit()

# the method get the record by it's email cuz it's uniqe and then change it's value to 1
# 0 means no accces and 1 means there is accces to the phone
def turn_on_phone_access (email):
    c.execute("UPDATE employees SET phone_access = 1 WHERE  email = email")

    conn.commit()

# the method get the record by it's email cuz it's uniqe and then change the acces value  value to 1
# 0 means no accces and 1 means there is accces to the storage
def turn_on_storage_access (email):
    c.execute("UPDATE employees SET storage_access = 1 WHERE  email = email")

    conn.commit()

# the method get the record by it's email cuz it's uniqe and then change the acces value  value to 0
# 0 means no accces and 1 means there is accces to the storage
def turn_off_storage_access (email):
    c.execute("UPDATE employees SET storage_access = 0 WHERE  email = email")

    conn.commit()
# ===============================================================================================================================================================

# the main methon is responsable of working the databse with all  functioalitites supported either insertion or printing or updating
# the create method should be called at the first time then shouldn't be called again
def main():
    cmd = input('Enter your command : ')

    if(cmd == 'create'):
        create()

    if(cmd == 'insert'):
        name = input('Your name is : ')
        email = input('Your email is : ')
        phone = input('Your phone is : ')
        insert(name,email,phone)

    if(cmd =='show_all_employee'):
        show_all_employee()

    if(cmd == 'turn_off_phone_access'):
        email = input('Your email is : ')
        turn_off_phone_access(email)

    if(cmd == 'turn_on_phone_access'):
        email = input('Your email is : ')
        turn_on_phone_access(email)

    if(cmd == 'turn_off_storage_access'):
        email = input('Your email is : ')
        turn_off_storage_access(email)

    if(cmd == 'turn_on_storage_access'):
        email = input('Your email is : ')
        turn_on_storage_access(email)

    if(cmd == 'turn_off_print_access'):
        email = input('Your email is : ')
        turn_on_print_access(email)

    if(cmd == 'turn_off_print_access'):
        email = input('Your email is : ')
        turn_on_print_access(email)
#main()
