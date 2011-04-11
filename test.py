#!usr/bin/env python

from Exscript.protocols import SSH2
from Exscript.Account import Account
a = []
b = []

account = Account(name='admin', password='p4ss')
conn = SSH2()
conn.connect('10.0.1.32')
conn.login(account)
conn.execute('term length 0')
conn.execute('term width 0')
conn.send('enable\r')
conn.app_authorize(account)
conn.execute('show run')
shorun = conn.response.split('\r\n')
shorun.pop()
conn.execute('show version')
shover = conn.response.split('\r\n')
shover.pop()
def print_version():
	print "IOS Version Info:"
	for line in shover:
		print line

def print_config():
	print "IOS Config:"
	for line in shorun:
		if line.strip() == '!':
			continue	
		else:
			print line
	

if __name__ == "__main__":
	print_version()
	print_config()
