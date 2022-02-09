#!/usr/bin/env python3

from pexpect import pxssh

s = pxssh.pxssh 
hostname = "192.168.0.111"
username = "justincase"
password = "Password01"
s.login(hostname, username, password)

s.sendline('hostname')
s.prompt()
print(s.before)

s.logout