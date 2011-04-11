#!usr/bin/env python

import sys
from Exscript.protocols import SSH2
from Exscript.Account import Account


def ssh_with_password(host, username, password, enablePassword, timeout):
	account = Account(name=username, password=password, password2=enablePassword)
	conn = SSH2()
	conn.connect(host)
	conn.login(account)
	conn.execute('term length 0')
	conn.execute('term width 0')
	conn.send('enable\r')
	conn.app_authorize(account)
	conn.execute('show running-config all')
	showrun = conn.response.split('\r\n')
	showrun.pop() # clean off last line which is the router's prompt
	conn.execute('show version')
	showver = conn.response.split('\r\n')
	showver.pop() # clean off last line which is the router's prompt
	
	for line in showrun:
		print line
            
def ssh_with_keyfile(host, username, keyfile, enablePassword, timeout):
	print "SSH with keyfiles is not yet implemented."
	sys.exit(-1)
	#TODO impelement ssh keyfile support
def telnet(host, username, password, enablePassword, timeout):
	print "Telnet support is not yet implemented."
	sys.exit(-1)
	#TODO implement telnetlib support

