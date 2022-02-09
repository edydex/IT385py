#!/usr/bin/env python3

import pexpect

child = pexpect.spawn("telnet 192.168.0.11")

child.expect("Username:")
child.sendline("cisco")
child.expect("Password:")
child.sendline("cisco")

child.expect("IT385-CSR.*")
child.sendline("conf t")

child.expect("IT385-CSR.*")
child.sendline("int g2")
child.expect("IT385-CSR.*")
child.sendline("ip addr 10.10.10.3 255.255.255.0")
child.expect("IT385-CSR.*")
child.sendline("desc try 2")
child.expect("IT385-CSR.*")
child.sendline("no shut")

child.expect("IT385-CSR.*")
child.sendline("exit")
child.expect("IT385-CSR.*")
child.sendline("exit")
child.expect("IT385-CSR.*")
child.sendline("exit")