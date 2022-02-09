#!/usr/bin/env python3

import pexpect
def get_uptime(remote_ip):
    #login
    child = pexpect.spawn("ssh justincase@" + remote_ip)
    child.expect(".*password:")
    child.sendline("Password01")
    print("login phase done")

    child.expect(".*\$")
    child.sendline("sudo apt update")
    child.expect(".*\:") #expecting sudo pass
    print("update phase done")
    child.sendline("Password01") #in this situation its ok to just type ur pass into terminal unprompted
    child.expect(".*\$")
    child.sendline("sudo apt install apache2 -y") #installing apache (again, takes time)
    print("Apache installed")
    child.expect(".*\$")
    child.sendline("sudo systemctl enable --now apache2")
    print("Apache enabled at start and started")

    #check for status just in case
    child.expect(".*\$")
    child.sendline("sudo systemctl status apache2")

    child.expect(".*\$")
    print("\n",child.after,"\n")
    child.sendline("exit")


ip_addresses = ["192.168.0.111", "192.168.0.112"]
for ip_address in ip_addresses:
    get_uptime(ip_address)