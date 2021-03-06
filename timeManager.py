#!/usr/bin/python

#imports
import sys
import os
import re
import time
import json

#global variables
level = None
calendar = None
localtime = time.asctime( time.localtime(time.time()) )

## Structure of the calendar
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

## Shell functionality
def timeManager():
	ensure("Data")
	while(1):
		global localtime
		localtime = time.asctime( time.localtime(time.time()) )
		print 'TimeManager:$ ',
		myinput = sys.stdin
		argv = getargs(myinput.readline())
		if len(argv) != 0:
			execute(argv)
#end of timeManager

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
	elif argv[0] == 'help':
		help()
	elif argv[0] == 'show':
		showCalendars()
	elif argv[0] == 'ls':
		listItems()
	elif argv[0] == 'use':
		switchTo(argv)
	elif argv[0] == 'echo':
		print ' '.join(argv[1:])
	else:
		print "Unknown command '" + argv[0] + "'"
		print "Type 'help' for more information."
#end of execute

def exit():
	print 'Bye!'
	sys.exit()
#end of exit

def help():
	print "Known commands:"
	print "'show' shows the list of available calendars."
	print "'use (cal-name)' access the calendar by its name."
	print "'ls [name]' list the current events in the day, or the days in the week."
	print "'cd (name)' access day/week/month by name."
	print "'create (event-name) [date]' create an event on the specified date."
#end of help

def showCalendars():
	for files in os.listdir("./Data"):
		if files.endswith(".cal"):
			print files[:len(files)-4]
#end of showCalendar

def listItems():	
	if not calendar:
		print "You need to access a calendar first."
		print "Type 'help' for more information."
	else:
		availableEvents = []
		for event in calendar.events:
			if event.date 

def switchTo(argv):
	if len(argv) < 2:
		print 'Provide a calendar name to use'
	else:
		global calendar
		calendar = Calendar(argv[1])
#end of switchTo

#call timeManager()
timeManager()
