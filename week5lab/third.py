#!/usr/bin/env python3
#import
from pexpect import pxssh
#define login function
def newuser(hostname):
    s = pxssh.pxssh()
    username = "justincase"
    password = "Password01"
    s.login(hostname, username, password)

    s.sendline('sudo useradd olis')
    s.prompt()
    print(s.before)

    s.logout

ip_addresses = ["192.168.0.121", "192.168.0.122", "192.168.0.111", "192.168.0.112"]
for ip_address in ip_addresses:
    newuser(ip_address)