#!/usr/bin/env python3

import pexpect
def get_uptime(remote_ip):
    #login
    child = pexpect.spawn("ssh justincase@" + remote_ip)
    child.expect(".*password:")
    child.sendline("Password01")
    child.expect(".*\$")
    print("login phase done")

    #updating apt and granting sudo privileges:
    child.sendline("sudo apt update")
    child.expect(".*\:") #expecting sudo pass
    child.sendline("Password01") #in this situation its ok to just type ur pass into terminal unprompted
    child.expect(".*\$")
    print("update phase done")
    #desired changes:
    child.sendline("sudo apt install apache2 -y") #installing apache (again, takes time)
    child.expect(".*\$")
    print("apache installed")
    child.sendline("sudo systemctl enable --now apache2")
    child.expect(".*\$")
    print("apache enabled at start and started")

    #check for status just in case
    child.sendline("hostname")

    child.expect(".*\$")
    print("\n",child.after,"\n")
    child.sendline("exit")


ip_addresses = ["192.168.0.111", "192.168.0.112"]
for ip_address in ip_addresses:
    get_uptime(ip_address)