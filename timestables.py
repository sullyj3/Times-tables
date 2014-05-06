import random
import sys
#menus

def mainmenu(): #potentially later justify explanations right somehow
	print()
	print("Select an option by entering its item number")
	print()
	print("1. UP TO 12: Practice random problems from 1 * 1 to 12 * 12")
	print("2. UP TO 20: Practice random problems from 1 * 1 to 20 * 20")
	print(("3. UP TO 12 * UP TO 20: The first number will be between 1 and 12, and the second "
	"will be between 13 and 20."))
	print("4. 13 to 20: Practice random problems from 13 * 13 to 20 * 20")

	#not yet implemented:
	
	#print("5. SPECIFIC TABLE: Select a specific times table you want to practise")
	
	print()
	print("0. EXIT")
	print()
	selection=input("> ")
	if selection=="0":	#exit selected
		quit()
	else:			#other option selected
		print()
		print("You can return to the main menu at any time by typing 'menu'")
		print()
		if selection=="1":
			one_to_twelve()

		elif selection=="2":
			one_to_twenty()

		elif selection=="3":
			first_twelve_second_twenty()
		
		elif selection=="4":
			thirteen_to_twenty()
		
#modes
#modes

#1
def one_to_twelve():  #1-12 times tables
	while 1==1:
		op1=random.randrange(1,12)
		op2=random.randrange(1,12)
		product=op1*op2
		answer=input(str(op1)+" * "+str(op2)+" = ")
		if answer=="menu":
			return
		elif answer==str(product):
			print("Correct!")
		else:
			print("Incorrect. The correct answer is "+str(product)+".")

#2
def one_to_twenty():  #1-20 times tables
	while 1==1:
		op1=random.randrange(1,21)
		op2=random.randrange(1,21)
		product=op1*op2
		answer=input(str(op1)+" * "+str(op2)+" = ")
		if answer=="menu":
			return
		elif answer==str(product):
			print("Correct!")
		else:
			print("Incorrect. The correct answer is "+str(product)+".")

#3
def first_twelve_second_twenty():
	while 1==1:
		op1=random.randrange(1,12)
		op2=random.randrange(13,21)
		product=op1*op2
		answer=input(str(op1)+" * "+str(op2)+" = ")
		if answer=="menu":
			return
		elif answer==str(product):
			print("Correct!")
		else:
			print("Incorrect. The correct answer is "+str(product)+".")

#4
def thirteen_to_twenty():
	while 1==1:
		op1=random.randrange(13,21)
		op2=random.randrange(13,21)
		product=op1*op2
		answer=input(str(op1)+" * "+str(op2)+" = ")
		if answer=="menu":
			return
		elif answer==str(product):
			print("Correct!")
		else:
			print("Incorrect. The correct answer is "+str(product)+".")


#not yet implemented
'''
#5
def pick_table():
	pass

#6
def set_range():
	pass

#7
def print_table(table):
	pass
'''

while 1==1: #goes back to main menu when other functions exit
	mainmenu()
