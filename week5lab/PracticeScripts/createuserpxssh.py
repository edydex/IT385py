#!/usr/bin/env python3
#import
from pexpect import pxssh
#define login function
def newuser(hostname):
    #login phase
    s = pxssh.pxssh()
    username = "justincase"
    password = "Password01"
    s.login(hostname, username, password)
    print("passed login phase")
    #useradd phase
    s.sendline('sudo useradd olis')
    s.prompt()
    #in this situation it won't hurt to put password in
    s.sendline('Password01')
    s.sendline('sudo passwd olis')
    s.prompt()
    s.sendline('p00p')
    s.prompt()
    s.sendline('p00p')
    s.prompt()
    print("passed password phase")
    #i guess this works but extremely slow, i assume its because the pxssh is expecting "$" but never gets it in password prompts. (it gets "$" instead)
    s.logout

ip_addresses = ["192.168.0.111"] #"192.168.0.122", "192.168.0.111", "192.168.0.112"]
for ip_address in ip_addresses:
    newuser(ip_address)