import os, sys
sys.path.append('modules/')
from scanModules import *
from time import sleep as timeout


def main():

	target = str(input("[?]Enter your Target website : "))
	
	if target == "":
		print("\n[!]Please enter your target website")
		main()
	else:
		pass

	os.system("clear")
	print("Your target is ", target)
	print("Select your scaning options")
	print
	print("	[01] Admin Panel")
	print("	[02] SQLi Vulnerability")
	print("	[03] XSS Vulnerability")
	print
	print("[00] Exit")
	print
	scan = int(input("[?]Your Select : "))
	
		
	if scan == 1:
		admin_scan(target)
		
	elif scan == 2:
		sqli_scan(target)
		
	elif scan == 3:
		xss_scan(target)
		
	elif scan == 0:
		sys.exit()
		
	else:
		print("[!]Please select your scan options")
		main(target)
	


    
os.system("figlet scorpion")
print("python3 web scanner")
print("ver. 0.1 beta")
print("==================================")
print("Make by Thitigorn Pumma (zeroDay)")
print("Member of Anachakhacker")
print("==================================")
print
print("Please delete parameters if will use admin scan")
print("Ctrl+C For exit")
print

main()
    
    
