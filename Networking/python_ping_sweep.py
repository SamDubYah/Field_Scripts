#!/usr/bin/python
# Simple program to do a ping sweep of a network
# Shows the hosts that are online
# Needs to be optimized 
# Convenience features need to be added

import subprocess
import os


for i in range(1,254):
        response = os.popen('ping -c 1 -W 1 10.11.1.%d' %(i))
        for line in response.readlines():
                if "from" in line:
                        print line,
                else:
                        continue
