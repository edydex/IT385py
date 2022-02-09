#!/usr/bin/env python3

from pexpect import pxssh

def get_hostname(hostname):
    s = pxssh.pxssh()
    username = "justincase"
    password = "Password01"
    s.login(hostname, username, password)

    s.sendline('hostname')
    s.prompt()
    print(s.before)

    s.logout
ip_addresses = ["192.168.0.121", "192.168.0.122", "192.168.0.111", "192.168.0.112"]
for ip_address in ip_addresses:
    get_hostname(ip_address)