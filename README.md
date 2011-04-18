IOS Configuration Fetch Utility
===============================

Usage
-----
		Usage: iosconfigfetch.py [options]

		Options:
		  -h, --help            show this help message and exit
		  --host=HOST           Device IP or hostname to connect to.
		  --user=USERNAME       Authentication username (i.e. remote user name).
		  --pass=PASSWORD       Authentication password.
		  -e ENABLEPASSWORD, --enable=ENABLEPASSWORD
								Privileged EXEC ('enable') password.
		  -p CONNECTIONTYPE, --protocol=CONNECTIONTYPE
								Protocol for console connection

		  Misc. Options:
			--keyfile=KEYFILE   RSA Private Keyfile for use with SSH connection (IOS 15+ only)
			--timeout=TIMEOUT   Optional timeout value for use with older, slower
								hardware
			-s                  Disable printed output/status messages, and only
								return router configuration (for scripting)
			--config=CONFS      List of items to retrieve: version, running-config,
								startup-config, or all items - defaults to only
								running-config

Purpose
-------
This script fetches configurations and version information from routers running Cisco IOS.  
It should be useful either as a standalone tool, or as a single purpose tool to be included in automation workflows.  
Multiple configuration items are separated by 40 '*' characters in a row on a line of their own.  

Example
-------
Retrieve the running configuration via SSH:  

		python iosconfigfetch.py --host=10.0.1.1 --user=netadmin --pass=ciscopass --enable=supercisco 

Retrieve the version via telnet:  

		python iosconfigfetch.py --host=10.0.55.3 --user=netman --pass=p4ssw0rd --enable=SEkr3T! --config=version -p telnet

Retrieve the startup and running configurations via SSH  

		python iosconfigfetch.py --host=myrouter.local --user=admin --pass=t3stp4ss --enable=abc123! --config=all-config 

Retrieve the startup configuration via SSH and dump it to a file  

		python iosconfigfetch.py --host=myrouter.local --user=admin --pass=t3stp4ss --enable=abc123! --config=all-config -s > startup-config.ios

Requirements
------------
Requires EXScript (https://github.com/knipknap/exscript)

License
-------
Copyright (c) 2011 Adam Crosby

This program is free software; you can redistribute it and/or modify  
it under the terms of the GNU General Public License version 2, as  
published by the Free Software Foundation.  

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
GNU General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program; if not, write to the Free Software  
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA   


