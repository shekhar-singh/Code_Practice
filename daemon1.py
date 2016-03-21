#!/usr/bin/env python
import daemon
import time

def action():
    while True:
    	with open("/tmp/readme.txt", "w") as f:
        	f.write("your program is running silently and this file is create at  "+time.ctime())
        time.sleep(10)

def run():
    with daemon.DaemonContext():
        action()

if __name__ == "__main__":
    run()
