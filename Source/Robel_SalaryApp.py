""" 
	This python script can calculate the gross salary and net salayr for a given input acording to the Ehtiopian Income tax law
	It also takes transprtation and pensin contribution payments in consideratin while doing so.
"""
from sys import exit
from time import sleep
from os import system
myTitle = 'Roar Salary Calculator 1.0'
system('title '+myTitle)


#Returns the Gross salary of a given inpute
def GrossSalaryCalc(ReqInp):
	
	if ReqInp<=708:
		return ((ReqInp-0)/1.18)
	elif ReqInp<=1842:
		return ((ReqInp-60)/1.08)
	elif ReqInp<=3438.5:
		return ((ReqInp-142.5)/1.03)
	elif ReqInp<=5447.5:
		return ((ReqInp-302.5)/.98)
	elif ReqInp<=7819:
		return ((ReqInp-565)/.93)
	elif ReqInp<=8699:
		return ((ReqInp-955)/.88)
	elif ReqInp<=10022:
		return ((ReqInp-955-2200)/.63)
	elif ReqInp>10022:
		return ((ReqInp-1500-2200)/.58)

#Returns the Net salary of a given inpute
def NetSalaryCalc(ReqInp):

	if ReqInp<=600:
		return ((ReqInp)-((ReqInp*0)-0)-(ReqInp*.07))
	elif ReqInp<=1650:
		return ReqInp-(((ReqInp*.1)-60)-(ReqInp*.07))
	elif ReqInp<=3200:
		return ((ReqInp)-((ReqInp*.15)-142.5)-(ReqInp*.07))
	elif ReqInp<=5250:
		return ((ReqInp)-((ReqInp*.2)-302.5)-(ReqInp*.07))
	elif ReqInp<=7800:
		return ((ReqInp)-((ReqInp*.25)-565)-(ReqInp*.07))
	elif ReqInp<=10900:
		return ((ReqInp)-((ReqInp*.3)-955)-(ReqInp*.07))
	elif ReqInp>10900:
		return ((ReqInp)-((ReqInp*.35)-1500)-(ReqInp*.07))

#Returns Income Tax

def IncomeTax(ReqInp):
	if ReqInp<=600:
		return 0
	elif ReqInp<=1650:
		return (ReqInp*.1)-60
	elif ReqInp<=3200:
		return (ReqInp*.15)-142.5
	elif ReqInp<=5250:
		return (ReqInp*.2)-302.5
	elif ReqInp<=7800:
		return (ReqInp*.25)-565
	elif ReqInp<=10900:
		return (ReqInp*.3)-955
	elif ReqInp>10900:
		return (ReqInp*.35)-1500

def Greet():
	try:
		gText = 'Salar Calulator 1.1'
		for i in range(19):
			print(gText[i], sep=" ", end=" ", flush=True);sleep(0.1)
		print(" ")
		line="*"*19
		for x in range(19):
			print(line[x], sep=' ', end=' ', flush=True); sleep(0.02)
		sleep(.5)
		print ("\nhint ... press [CTRL+C] to exit\n")
		sleep(.5)
	except (KeyboardInterrupt, SystemExit):
		exit

def NetPayfnc():
	try:		
		inp_np = (input("\nHow much do you want to pay or get paid? >>   "))
		print ("\n")

		GrossSalary	= GrossSalaryCalc(float(inp_np))
			
		if GrossSalary<=8800:
			AllowanceNP = GrossSalary/4
		else:
			AllowanceNP = 2200

		print("Gross Salary:"," "*27,round(GrossSalary,2))
		print("Transportation Allowance:"," "*15,round(AllowanceNP,2))
		print("Income tax:"," "*29,round(IncomeTax(float(GrossSalary)),2))
		print("Pension 7%% (Employee contribiution):"," "*3,round((0.07*GrossSalary),2))
		print("Pension 11%% (Employer contribiution):"," "*2,round((0.11*GrossSalary),2))
		mainMenu()
	except(KeyboardInterrupt, SystemExit):
		exit

def GrossPayfnc():
	try:
		inp_gp = (input("\nHow much is the gross salary do you have? >>   "))
		print ("\n")

		NetSalary = NetSalaryCalc(float(inp_gp))
			
		if float(inp_gp) <=8800:
			AllowanceGP = float(inp_gp)/4
		else:
			AllowanceGP = 2200

		print("Net Salary:"," "*29,round((NetSalary+AllowanceGP),2))
		print("Transportation Allowance:"," "*15,round(AllowanceGP,2))
		print("Income tax:"," "*29,round(IncomeTax(float(inp_gp)),2))
		print("Pension 7%% (Employee contribiution):"," "*3,round((0.07*float(inp_gp)),2))
		print("Pension 11%% (Employer contribiution):"," "*2,round((0.11*float(inp_gp)),2,))
		mainMenu()
	except(KeyboardInterrupt, SystemExit):
		exit

def mainMenu():

	try:
		print("\nSelect by typing the nubers for the menu:\n")
		print("1. Calculate Net Pay GIVEN GROSS PAY")
		print("2. Calculate Gross Pay GIVEN NET PAY")
		print("3. Exit!")
		inp = int(input(">>  "))
	
	except ValueError:
		print ("Invalid Input")
	except(KeyboardInterrupt, SystemExit):
		exit
	else:
		if inp==1:
			NetPayfnc()
		elif inp==2:
			GrossPayfnc()
		elif inp==3:
			exit
		else:
			print("Please slecet by entering the values 1, 2 or 3\n")
			mainMenu()
			
#excution order
Greet()
mainMenu()