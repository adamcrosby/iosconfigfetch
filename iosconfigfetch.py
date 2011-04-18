#!/usr/bin/env python
#
# (c) 2011 Adam Crosby
# Licensed under: http://creativecommons.org/licenses/by-nc-sa/3.0/
#
import sys
from optparse import OptionParser
from optparse import OptionGroup

from ioslib import ssh_with_password, ssh_with_keyfile, telnet

def parse_options():
	parser = OptionParser()

	parser.set_defaults(timeout=30, connectionType="ssh", keyfile=None, confs="running-config")
	protoChoices = ["ssh", "telnet"]
	confChoices = ['version', 'startup-config', 'running-config', 'all-config', 'all']
	parser.add_option("--host", dest="host", help="Device IP or hostname to connect to.")
	parser.add_option("--user", dest="username", help="Authentication username (i.e. remote user name).")
	parser.add_option("--pass", dest="password", help="Authentication password.")
	parser.add_option("-e", "--enable", dest="enablePassword", help="Privileged EXEC (\'enable\') password.")
	parser.add_option("-p", "--protocol", type="choice", dest="connectionType", choices=protoChoices, help="Protocol for console connection")

	group = OptionGroup(parser, "Misc. Options")
	group.add_option("--keyfile", dest="keyfile", help="RSA Private Keyfile for use with SSH connection")
	group.add_option("--timeout", type="int", dest="timeout", help="Optional timeout value for use with older, slower hardware")
	group.add_option("-s", action="store_true", dest="silent", help="Disable printed output/status messages, and only return router configuration (for scripting)")
	group.add_option("--config", type="choice", dest="confs", choices=confChoices, help="List of items to retrieve: version, running-config, startup-config, or all items - defaults to only running-config")

	parser.add_option_group(group)

	(options, args) = parser.parse_args()
	
	return options

if __name__ == "__main__":
	options = parse_options()
	
	if not options.silent:
		# Ensure some mandatory items here
		if options.host == None:
			print "Please specify a target host with the '--host' argument. Please see '-h' for help."
			sys.exit(-1)

		# Ensure some mandatory items here
		if options.username == None:
			print "Please specify a username with the '--user' argument.  Please see '-h' for help."
			sys.exit(-1)


		# Figure out what kind of connection is being asked for, and call the apporpriate function
		if options.connectionType == "ssh":
			print "Connecting via SSH"
			print "Connecting to host: %s" % options.host
			print "\tUsername: %s" % options.username

			# Figure out if SSH connection is goign to use a username/password
			# or a keyfile.  If user supplies both, default to the keyfile
			if options.keyfile == None:
				print "\tPassword: %s" % options.password
				print "\tUsing enable password: %s" % options.enablePassword
				ssh_with_password(options.host, options.username, options.password, options.enablePassword, options.timeout, options.confs)
			elif (options.password == "") or (options.password == None):
				print "\tKeyfile: %s" % options.keyfile
				print "\tUsing enable password: %s" % options.enablePassword
				ssh_with_keyfile(options.host, options.username, options.keyfile, options.enablePassword, options.timeout, options.confs)
			else:
				print "\tKeyfile and password both supplied, defaulting to keyfile."
				print "\tKeyfile: %s" % options.keyfile
				print "\tUsing enable password: %s" % options.enablePassword
				ssh_with_keyfile(options.host, options.username, options.keyfile, options.enablePassword, options.timeout, options.confs)


		elif options.connectionType == "telnet":
			print "Connecting via telnet (WARNING: CREDENTIALS WILL BE UNENCRYPTED)"
			print "Connecting to host: %s" % options.host
			print "\tUsername: %s" % options.username
			print "\tPassword: %s" % options.password
			print "\tUsing enable password: %s" % options.enablePassword
			telnet(options.host, options.username, options.password, options.enablePassword, options.timeout, options.confs)
		else:
		# Error, bad protocol type, shouldnt' get here
			print "Incorrect protocol specified."
			sys.exit(-1)
	else:
		
		if options.host == None:
			sys.exit(-1)

		# Ensure some mandatory items here
		if options.username == None:
			sys.exit(-1)

		# Figure out what kind of connection is being asked for, and call the apporpriate function
		if options.connectionType == "ssh":
			# Figure out if SSH connection is goign to use a username/password
			# or a keyfile.  If user supplies both, default to the keyfile
			if options.keyfile == None:
				ssh_with_password(options.host, options.username, options.password, options.enablePassword, options.timeout)
			else: 
				ssh_with_keyfile(options.host, options.username, options.keyfile, options.enablePassword, options.timeout)
		elif options.connectionType == "telnet":
			telnet(options.host, options.username, options.password, options.enablePassword, options.timeout)
		else:
		# Error, bad protocol type, shouldnt' get here
			sys.exit(-1)
