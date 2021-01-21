
Welcome to bsoder's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Simple API Docs
==================





.. py:function:: simplest__bsod(self)
	
Call`s simple bsod using simle cmd command that is called by os module in python
For fact ths command is working on broswer : **\\.\globalroot\device\condrv\kernelconnect**
You can call it using :
	bsod.simplest__bsod()
	
	
.. py:function:: taskmanger_way(self)	
	
Call`s simple bsod using simple cmd command that is called by os module in python
For fact ths command is on powershell : **runas /user:administrator TASKKILL /IM svchost.exe /F**
Also runas is just for as admin rights.
You can call it using :
	bsod.taskmanger_way()

	
.. py:function:: use_external(self)

Runs simple tool by Microsoft and let you manualy run bsod.
You can run it as :
	bsod.use_external()
	
..	

Minimal Example of code:
==================================
.. code-block:: python

	
    
	#This example will just import lib , and call BSOD,
	#Author: Alex Zaslavskis
	
	import bsoder as bsoder # imports lib
	bsod=bsoder.Bsoder() # inits lib
	bsod.simplest__bsod()# calls bsod
	


