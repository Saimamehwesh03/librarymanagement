#!/usr/bin/env python
# coding: utf-8

# In[42]:


import mysql.connector
from mysql.connector import Error
 
def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='127.0.0.1',database='python_mysql',user='root',password='mehwesh03') # change to your creds 
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
 
 
if __name__ == '__main__':
    connect()


# In[43]:


from configparser import ConfigParser 
 
def read_db_config(filename='configfile.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
 
    return db


# In[5]:


print(read_db_config())


# In[44]:


from mysql.connector import MySQLConnection, Error
 
def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config) # kwargs 
 
        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')
 
 
if __name__ == '__main__':
    connect()


# In[51]:


import datetime


class lib:
    def __init__(self, location):
        self.location = location


class librarian:
    def __init__(self, lusername, lcontactdetails):  
        self.lfullname = lfullname
        self.lcontactdetails = lcontactdetails
        
    def __str__(self):
        return 'Hello And Welcome' + self.lfullname
    
    def addLibrarian(self, name, contact_information):
        self.name = name
        self.contactin_formation = contactinformation
        librarianx = self.name, self.contactinformation
        return librarianx
    
    def displayLibrarian(self, l):
        self.l = l
        return self.l
    
    def adduser(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        userx = self.name, self.contact_information 
        return userx
    
    def displayuser(self, u):
        self.u = u
        return self.u
    
    def addBooks(self, book_name, author, publisher, rented_user, rented_date):
        self.book_name = book_name
        self.author = author
        self.publisher = publisher
        self.rented_user = rented_user
        self.rented_date = rented_date
        bookx = self.bookname, self.author, self.publisher, self.rented_user, self.rented_date
        return bookx
    
    def displayBooks(self, b):
        self.b = b
        return self.b
    
def update_user(id,contact_info):
    
    db_config = read_db_config()
        
    query = """ UPDATE user
                SET contact_info = %s
                WHERE id = %s """
    data = (contact_info,id)
 
    try:
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, data)
 
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    update_user(2,'8724972840')
    
def update_books(id_book, book_name):
    
    db_config = read_db_config()
 
    
    query = """ UPDATE books
                SET book_name = %s
                WHERE id_book = %s """
 
    data = (book_name, id_book)
    
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, data)
 
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    update_books(3, 'Budden brooks')
    
def delete_user(id):
    db_config = read_db_config()
 
    query = "DELETE FROM user WHERE id = %s"
 
    try:
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    delete_user(2)
    
    
def delete_books(id_book):
    db_config = read_db_config()
 
    query = "DELETE FROM books WHERE id_book = %s"
 
    try:
        
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, (id_book,))
 
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    delete_books(2)


# In[53]:


def query_select():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
query_select()


# In[56]:


def query_select():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
query_select()


# In[ ]:


class user:
    def __init__(self, username, contact_information):
        self.username = username
        self.contact_information = contact_information

    def __str__(self):
        return'Hello' + self.username
    
def sign_in():
    details = View.user_login()

    try:
        c.execute("SELECT * FROM Users WHERE user_name=?", (details[0],))
        user = c.fetchone()
        if user is None:
            print("Unable To Find {}")
            key = False
        
        elif details[1] == user[2]:
            print("Glad To Have You With Us Again {}".format(user[0]))
            print(pd.DataFrame(user))
            key = True
        else:
            raise ValueError
    except ValueError:
        print("The Information Given Is Wrong")
        key = False
    return [details[0], key]

def take(self, bookname):
        self.bookname = bookname
        for h in range(0, len(al)):
            if self.bookname in al[h]:
                z = al.__getitem__(h)
                return 'The Book Taken Is' + str(z)
def return1(self, bookname1, totaldays):
        self.bookname1 = bookname1
        self.totaldays = totaldays
        if self.totaldays <= 20:
            al.append(self.bookname)
            return 'Book Added Back To The Inventory With No Fine'
        elif self.totaldays > 20:
            fine = 20.0
            al.append(self.bookname)
            for i in range(0, self.howmanydays - 20):
                fine += 5
            return'Book Added Back To The Inventory With A Fine To Pay Of :' + str(fine)
        
library = lib('Seattle')
print("The Library Is Situated In :", library.location)
global mem
global mem1
global bookx
global al
global h
global z
global fine
yes = True
while yes:
    print(""" *****@LIBRARY INVASION*****
		1. Librarian Authentication
		2. User Authentication to borrow/return books from the available list """)
    c = int(input("Enter Choice:"))
    if c == 1:
        an = str(input("Enter Admin number:"))
        if(an == "777"):
            libmaster = librarian('Saima Mehwesh', '2302')
            print(libmaster)
            ans = str(input("Enter 1 to add book / 'stop' to exit:"))
            if(ans != "stop"):
                libmaster2 = librarian('Saima Mehwesh', '2302')
                au = str(input("Enter the author name:"))
                bn = str(input("Enter the book name:"))
                pc = str(input("Enter the publication company name:"))
                al = ['Author Name', 'BookName', 'publicationcompany']
                mem = libmaster2.addBooks(au, bn, pc)
                al.append(mem)
                print(al)
                ans1 = str(
                    input("Enter 1 to DisplayBooks and continue adding...Enter 'stop' to stop adding:"))
                while ans1 != 'stop':
                    libmaster1 = librarian('Saima Mehwesh', '2302')
                    z1 = libmaster1.displayBooks(al)
                    print(z1)
                    au1 = str(input("Enter the author name:"))
                    bn1 = str(input("Enter the book name:"))
                    pc1 = str(input("Enter the publication company name:"))
                    mem1 = libmaster1.addBooks(au1, bn1, pc1)
                    al.append(mem1)
                    print(al)
                    ans1 = str(
                        input("Enter 1 to DisplayBooks and continue adding...Enter 'stop' to stop adding:"))
            elif(ans == "2"):
                libmaster2 = librarian('Saima Mehwesh', '2302')
                un = str(input("Enter full name of the user:"))
                uc = str(input("Enter contact information of the user:"))
                bl = ['Name', 'Contact information']
                user = libmaster2.adduser(un, uc)
                bl.append(user)
                print(bl)
                ans1 = str( input("Enter 1 to DisplayInfo of new user and continue adding...Enter 'stop' to stop adding:"))
                
                while ans1 != 'stop':
                    libmaster1 = librarian('Saima Mehwesh', '2302')
                    z1 = libmaster1.displayuser(bl)
                    print(z1)
                    un1 = str(input("Enter full name of the user:"))
                    uc1 = str(input("Enter contact information of the user:"))
                    user1 = libmaster1.adduser(un1, uc1)
                    bl.append(user1)
                    print(bl)
                    ans1 = str(
                        input("Enter 1 to DisplayInfo and continue adding...Enter 'stop' to stop adding:"))
            else:
                break
        else:
            print("Wrong Input *WARNING*")
    elif c == 2:
        i1 = str(input("Enter Your Full Name:"))
        i2 = str(input("Enter Contact Information:"))
        us = user(i1, i2)
        print(us)
        lm = librarian('Saima Mehwesh', '2302')
        gt = lm.displayBooks(al)
        print(gt)
        ch = str(input("Enter 'take' or 'return' a book or 'enter' to quit:"))
        while ch != 'return':
            i = str(input("Enter the book you are proceeding to withdraw:"))
            x = us.take(i)
            datetime_object = datetime.datetime.now()
            print("Time is:", datetime_object)
            date_object = datetime.date.today()
            print("Date is:", date_object)
            print(x)
            ch = str(
                input("Enter 'take' or 'return' a book or 'enter' to quit:"))

        if ch == 'return':
            j = str(input("Enter the name of the book returning:"))
            k = int(
                input("Enter the days you had the book:"))
            y = us.return1(j, k)
            datetime_object1 = datetime.datetime.now()
            print("Time is:", datetime_object1)
            date_object1 = datetime.date.today()
            print("Date is:", date_object1)
            print(y)
            
        else:
            break
    else:
        print("Please enter 1 or 2")
        


# In[ ]:




