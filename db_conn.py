import sqlite3
from sqlite3 import Error

'''CONNECTING TO DATABASE '''


def create_connection(db_file):
    ''' CREATING CONNECTION TO sqlite3 DATABASE '''
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    finally:
        if conn:
            print("DATABASE CONNECTION SUCESSFUL!")
        else:
            print("DATABASE CONNECTION FAILED!")
        return conn


'''CREATING DATABASE '''

def create_table():

    conn = create_connection(
        'C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
    c = conn.cursor()

    create_table_command = """
	CREATE TABLE IF NOT EXISTS
	contacts(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, phone_no INTEGER, email TEXT)
	"""
    c.execute(create_table_command)
    conn.close()


'''INSERTING USER INPUT INTO THE TABLE '''


def insert_into_DB(first_name, last_name, phone_no, email_add):
    conn = create_connection(
        'C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts(firstname, lastname, phone_no, email) VALUES(?,?,?,?)",
              (first_name, last_name, phone_no, email_add))
    conn.commit()
    conn.close()


''' RETRIVING SPECIFIC CONTACTS FROM DATABASE'''


def retrive_contact_for_update(first_name, last_name):
    conn = create_connection(
        'C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE firstname=? OR lastname=?",
              (first_name, last_name))
    row = c.fetchall()
    contactList = []

    for content in row:
        contactList.append(content)
        print(content)
        # print(type(content))
    return contactList
    conn.close()


''' UPDATING CONTACT IN DATABASE'''


def updating_contact_db(sql_stmt, tbu):
    conn = create_connection(
        'C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
    c = conn.cursor()
    c.execute(sql_stmt, tbu)
    conn.commit()
    conn.close()


'''RETRIVING ALL CONTACTS'''


def retrive_all_contact():
    conn = create_connection(
        'C:/Users/boria/Documents/Python Scripts/contact_book/contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    row = c.fetchall()

    for content in row:
        print(content)
    conn.close()
