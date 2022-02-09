#!/usr/bin/env python3
import time
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
    print("command 1 in, give a minute to finish")
    child.expect("justincase.*") #expecting sudo pass
    child.sendline("Password01") #in this situation its ok to just type ur pass into terminal unprompted
    time.sleep(65) #must do this cause VMs slow
    #child.expect(".*\$")  tstsrtartsawrstarst
    print("update phase done")
    #desired changes:
    child.sendline("sudo apt install mariadb-server -y") #installing apache (again, takes time)
    print("command 2 in, 1.5 min to finish") 
    time.sleep(90) #must
    child.expect(".*\$")
    print("mariadb installed")
    child.sendline("sudo systemctl enable --now mariadb")
    child.expect(".*\$")
    print("mariadb enabled at start and started")

    #check for status just in case
    child.sendline("hostname")

    child.expect(".*\$")
    print("\n",child.after,"\n")
    child.sendline("exit")


ip_addresses = ["192.168.0.121", "192.168.0.122"]
for ip_address in ip_addresses:
    get_uptime(ip_address)