#!usr/bin/env python

import sys
from Exscript.protocols import SSH2
from Exscript.Account import Account


confChoices = ['version', 'startup-config', 'running-config', 'all-config', 'all']

def get_configs_ssh(account, host):
	conn = SSH2()
	conn.connect(host)
	conn.login(account)
	conn.execute('term length 0')
	conn.execute('term width 0')
	conn.send('enable\r')
	conn.app_authorize(account)
	conn.execute('show version')
	showver = conn.response.split('\r\n')
	conn.execute('show startup-config')
	showstart = conn.response.split('\r\n')
	conn.execute('show running-config all')
	showrun = conn.response.split('\r\n')
	showrun.pop()
	showstart.pop()
	showver.pop()
	outputbuffer = {'version':showver,
			'startup-config':showstart,
			'running-config':showrun}
	return outputbuffer

def ssh_with_password(host, username, password, enablePassword, timeout, confs):

	account = Account(name=username, password=password, password2=enablePassword)
	configs = get_configs_ssh(account, host)


	if confs == 'version':
		for line in configs['version']:
			print line
	elif confs == 'startup-config':
		for line in configs['startup-config']:
			print line
	elif confs == 'running-config':
		for line in configs['running-config']:
			print line
	elif confs == 'all-config':
		for line in configs['startup-config']:
			print line
		print "*"*40
		for line in configs['running-config']:
			print line
	elif confs == 'all':
		for line in configs['version']:
			print line
		print "*"*40
		for line in configs['startup-config']:
			print line
		print "*"*40
		for line in configs['running-config']:
			print line
	else: 
		for line in configs['running-config']:
			print line
            
def ssh_with_keyfile(host, username, keyfile, enablePassword, timeout, startupconf):
	print "SSH with keyfiles is not yet implemented."
	sys.exit(-1)
	#TODO impelement ssh keyfile support
def telnet(host, username, password, enablePassword, timeout, startupconf):
	print "Telnet support is not yet implemented."
	sys.exit(-1)
	#TODO implement telnetlib support

