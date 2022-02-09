#!/usr/bin/env python3

import pexpect

child = pexpext.spawn("ssh justincase@192.168.0.121")
child.expect(".*password:")
child.sendline("Password01")

child.expect(".*\$")
child.sendline("uptime")

child.expect(".*\$")
child.sendline("exit")
