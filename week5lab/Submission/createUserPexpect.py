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
    child.sendline("sudo useradd olis")
    child.expect(".*\:") #expecting sudo pass
    child.sendline("Password01") #in this situation its ok to just type ur pass into terminal unprompted
    child.expect(".*\$")
    child.sendline("sudo passwd olis")
    child.expect(".*\:") #expecting to type pass
    child.sendline("p00p")
    child.expect(".*\:") #expecting to retype pass
    child.sendline("p00p")
    print("useradd phase done")
    #Hostnames just in case
    child.expect(".*\$")
    child.sendline("hostname")

    child.expect(".*\$")
    print("\n",child.after,"\n")
    child.sendline("exit")


ip_addresses = ["192.168.0.111", "192.168.0.122", "192.168.0.111", "192.168.0.112"]
for ip_address in ip_addresses:
    get_uptime(ip_address)