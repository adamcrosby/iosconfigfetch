#!/usr/bin/env python

from optparse import OptionParser
from optparse import OptionGroup
parser = OptionParser()

parser.set_defaults(timeout=60, connectionType="ssh")
protoChoices = ["ssh", "telnet"]
parser.add_option("--host", dest="host", help="Device IP or hostname to connect to.")
parser.add_option("--user", dest="username", help="Authentication username (i.e. remote user name).")
parser.add_option("--pass", dest="password", help="Authentication password.")
parser.add_option("-e", "--enable", dest="enablePassword", help="Privileged EXEC (\'enable\') password.")
parser.add_option("-p", "--protocol", type="choice", dest="connectionType", choices=protoChoices, help="Protocol for console connection")

group = OptionGroup(parser, "Misc. Options")
group.add_option("--keyfile", dest="sshKeyfile", help="RSA Private Keyfile for use with SSH connection")
group.add_option("--timeout", type="int", dest="timeout", help="Optional timeout value for use with older, slower hardware")

parser.add_option_group(group)

(options, args) = parser.parse_args()
