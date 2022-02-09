#!/usr/bin/env python3

import pexpect
def get_uptime(remote_ip):
    child = pexpect.spawn("ssh justincase@" + remote_ip)
    child.expect(".*password:")
    child.sendline("Password01")

    child.expect(".*\$")
    child.sendline("uptime")

    child.expect(".*\$")
    print("\n",child.after,"\n")
    child.sendline("exit")

get_uptime("192.168.0.121")