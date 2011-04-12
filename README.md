IOS Configuration Fetch Utility
===============================

Usage
-----
<pre>
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
    --keyfile=KEYFILE   RSA Private Keyfile for use with SSH connection
    --timeout=TIMEOUT   Optional timeout value for use with older, slower
                        hardware
    -s                  Disable printed output/status messages, and only
                        return router configuration (for scripting)
    --config=CONFS      List of items to retrieve: version, running-config,
                        startup-config, or all items - defaults to only
                        running-config

</pre>
Purpose
-------
This script fetches configurations and version information from routers running Cisco IOS.
It should be useful either as a standalone tool, or as a single purpose tool to be included in automation workflows.

Requirements
------------
Requires EXScript (https://github.com/knipknap/exscript)

License
-------
(c) 2011 Adam Crosby 
The code is licensed under: http://creativecommons.org/licenses/by-nc-sa/3.0/
