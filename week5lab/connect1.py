#!/usr/bin/env python3

import pexpect

child = pexpect.spawn("telnet 192.168.0.11")

child.expect("Username:")
child.sendline("cisco")
child.expect("Password:")
child.sendline("cisco")

child.expect(".*#")
child.sendline("conf t")

child.expect(".*#")
child.sendline("int g2")
child.expect(".*#")
child.sendline("ip addr 10.10.10.3 255.255.255.0")
child.expect(".*#")
child.sendline("desc try 2")
child.expect(".*#")
child.sendline("no shut")

child.expect(".*#")
child.sendline("exit")
child.expect(".*#")
child.sendline("exit")
child.expect(".*#")
child.sendline("exit")

