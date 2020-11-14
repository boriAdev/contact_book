''' Contact Book Application'''
from contact_book import *

if __name__=="__main__":

	'''Application Interface'''

	on = True

	while on:
		print("-------Contact Book----------")
		print("Choose an option:")
		print("C - Create New Contact")
		print("U - Update a contact")
		print("D - Delete a Contact")
		print("B - Backup contacts in the Cloud")
		print("Q - Quit")

		starter =input(' : ')


		'''User ends Application'''

		if starter.upper() == "Q":
			on = False
