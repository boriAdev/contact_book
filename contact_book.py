import sqlite3
from sqlite3 import Error
from db_conn import *

'''OPERATIONAL FUNCTIONS '''
class Contacts():

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.phone_no = None
        self.email_add = None

    ''' METHOD TO CREATE CONTACT'''

    def create_new_contact(self, fname, lname, phonenumber, emailaddress):

        self.first_name = fname
        self.last_name = lname
        self.phone_no = phonenumber
        self.email_add = emailaddress

        insert_into_DB(fname, lname, phonenumber, emailaddress)

    '''LIST ALL CONTACTS'''

    def show_all_contacts(self):
        retrive_all_contact()

    '''UPDATEING A CONTACT '''

    def update_contact(self, fname, lname):

        self.first_name = fname
        self.last_name = lname

        list_to_edit = retrive_contact_for_update(fname, lname)
        print(list_to_edit)

        contact_id = int(
            input("ENTER THE ID OF THE CONTACT YOU WOULD LIKE TO EDIT: "))

        options = []

        for lx in list_to_edit:
            options.append(lx[0])

        if contact_id in options:
            onAgain = True
            while onAgain:
                print('------CONTACT UPDATE----------')
                print('1 - First name')
                print('2 - Last Name')
                print('3 - Phone Number')
                print('4 - Email Address')
                print('99 - Cancel')

                to_edit = int(input('What would you like to edit: '))

                while to_edit not in {1: 1, 2: 2, 3: 3, 4: 4, 99: 99}:
                    print('INVALID INPUT')
                    break

                if to_edit == 1:
                    update_detail = input("Enter new First Name: ")
                    sql_stmt = '''UPDATE contacts SET firstname=? WHERE id=?'''
                    try:
                        updating_contact_db(
                            sql_stmt, (update_detail, contact_id))
                        print('SUCCESSFUL UPDATE!')
                    except Error as e:
                        print(e)

                '''does not work yet '''

                # anotherOne = input('Would you like to update another attribute of the same contact?(Y/N) :')
                # while anotherOne is not 'Y' or 'N':
                # 	print('Try Again')
                # 	anotherOne = input(": ")

                # if anotherOne.upper() == "Y":
                # 	break
                # elif anotherOne.upper() == "N":
                # 	onAgain = False

                elif to_edit == 2:
                    update_detail = input("Enter new Last Name: ")
                    sql_stmt = '''UPDATE contacts SET lastname=? WHERE id=?'''
                    try:
                        updating_contact_db(
                            sql_stmt, (update_detail, contact_id))
                        print('SUCCESSFUL UPDATE!')
                        onAgain = False
                    except Error as e:
                        print(e)

                elif to_edit == 3:
                    update_detail = int(input("Enter new Phone Number: "))
                    sql_stmt = '''UPDATE contacts SET phone_no=? WHERE id=?'''
                    try:
                        updating_contact_db(
                            sql_stmt, (update_detail, contact_id))
                        print('SUCCESSFUL UPDATE!')
                        onAgain = False
                    except Error as e:
                        print(e)

                elif to_edit == 4:
                    update_detail = input("Enter new Email Address: ")
                    sql_stmt = '''UPDATE contacts SET email=? WHERE id=?'''
                    try:
                        updating_contact_db(
                            sql_stmt, (update_detail, contact_id))
                        print('SUCCESSFUL UPDATE!')
                        onAgain = False
                    except Error as e:
                        print(e)

                elif to_edit == 99:
                    print('UPDATE CANCELLED.')
                    onAgain = False
                else:
                    print('INVALID INPUT')
                    continue
        else:
            print('FAILED to UPDATE contact')
