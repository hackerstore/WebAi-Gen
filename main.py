import os
import math
import random
import time
import webbrowser
import pyfiglet


output = "Output"

location = os.getcwd()

folder_chk = os.getcwd()
final = folder_chk + "/Output"
isdir = os.path.isdir(final)
if isdir is False:
	os.mkdir(final)
else:
	print("")




def personal():
	personal_theme_list = ['os.system("cd theme/DataSec && python main_obfu.py")', 'os.system("cd theme/ColorLib && python main_obfu.py")']
	exec(random.choice(personal_theme_list))

def company():
	os.system("cd theme/ComData && python main_obfu.py")

def main():
	print("==================================================")
	banner = pyfiglet.figlet_format("WebAi - Gen")
	print(banner)
	print("==================================================")
	print("Developed By Nazim Cp")
	time.sleep(2)
	print("Ai: Hello, Select your theme..")
	print("1] Personal Websites")
	print("2] Company Websites")
	print("3] Internet forum")
	print("4] Developer Info")
	print("----Exit----")
	input1 = input("Enter Your Option: ")
	if input1 == "1":
		personal()
	elif input1 == "2":
		company()
	elif input1 == "3":
		print("Not Working... Coming Soon..")
		print("Return in 5 second")
		time.sleep(5)
		main()
	elif input1 == "exit":
		exit()
	elif input1 == "4":
		webbrowser.open('https://instagram.com/nazimcp7')

	else :
		main()

main()
