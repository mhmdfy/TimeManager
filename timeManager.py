#!/usr/bin/python

#imports
import sys
import os
import re
import json

#global variables
calendar = None

class Event:

	def __init__(self, name, desc, time, date):
		self.name = name
		self.desc = desc
		self.time = time
		self.date = date
		print name + ' Was craeted'

class Calendar:
	def __init__(self, name):
		self.name = name
		self.events = []
		print name + ' calendar was created'

	def addEvent(self, event):
		self.events.append(event)
#end of Calendar

def ensure(path):
	if not os.path.exists(path):
		print 'Directory does not exist'
		os.makedirs(path)
		print 'Created "Data" directory to store data'
	else:
		print '"Data" exists'
	#os.chdir(path)
#end of ensure

def getargs(argv):
	matches = re.search('^[^#]*', argv)
	ans = matches.group(0).split()
	return ans
#end of getargs

def execute(argv):
	if argv[0] == 'exit' or argv[0] == 'logout' or argv[0] == 'quit':
		exit()
	elif argv[0] == 'echo':
		print ' '.join(argv[1:])
	elif argv[0] == 'ls':
		listItems()
	elif argv[0] == 'use':
		switchTo(argv)
	else:
		print "Unknown command '" + argv[0] + "'"
#end of execute

def exit():
	print 'Bye!'
	sys.exit()
#end of exit

def listItems():
	if calendar == None:
		for files in os.listdir("./Data"):
			if files.endswith(".cal"):
				print files[:len(files)-4]
	else:
		for days in calendar.days:
			print days

def switchTo(argv):
	if len(argv) < 2:
		print 'Provide a calendar name to use'
	else:
		global calendar
		calendar = Calendar(argv[1])
#end of switchTo

def timeManager():
	ensure("Data")
	while(1):
		print 'TimeManager:$ ',
		myinput = sys.stdin
		argv = getargs(myinput.readline())
		if len(argv) != 0:
			execute(argv)
#end of timeManager()

#call timeManager()
timeManager()
