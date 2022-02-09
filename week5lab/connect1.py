#!/usr/bin/env python3

import pexpect

child = pexpect.spawn("telnet 192.168.0.11")

child.expect("Username:")
child.sendline("cisco")
child.expect("Password:")
child.sendline("cisco")

child.expect("IT385-CSR1")
child.sendline("conf t")

child.expect("IT385-CSR1")
child.sendline("int g2")
child.expect("IT385-CSR1")
child.sendline("ip addr 10.10.10,")
child.expect("IT385-CSR1")
child.sendline("")
child.expect("IT385-CSR1")
child.sendline("")