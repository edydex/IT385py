#!/usr/bin/env python3

import pexpect

child = pexpect.spawn("ssh justincase@192.168.0.121")
child.expect(".*password:")
child.sendline("Password01")

child.expect(".*\$")
child.sendline("uptime")

child.expect(".*\$")
print(child.after)
child.sendline("exit")
