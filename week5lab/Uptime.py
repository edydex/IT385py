#!/usr/bin/env python3

from ipaddress import ip_address
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

ip_addresses = ["192.168.0.121", "192.168.0.122", "192.168.0.111", "192.168.0.112"]
get_uptime("192.168.0.121")