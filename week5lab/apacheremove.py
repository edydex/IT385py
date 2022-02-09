#!/usr/bin/env python3

import pexpect
def get_uptime(remote_ip):
    #login
    child = pexpect.spawn("ssh justincase@" + remote_ip)
    child.expect(".*password:")
    child.sendline("Password01")
    print("login phase done")
    #creating user
    child.expect(".*\$")
    child.sendline("sudo apt remove apache2")
    child.expect(".*\:") #expecting sudo pass
    child.sendline("Password01") #in this situation its ok to just type ur pass into terminal unprompted
    print("userdel phase done")
    #Hostnames just in case
    child.expect(".*\$")
    child.sendline("hostname")

    child.expect(".*\$")
    print("\n",child.after,"\n")
    child.sendline("exit")


ip_addresses = ["192.168.0.111", "192.168.0.112"]
for ip_address in ip_addresses:
    get_uptime(ip_address)