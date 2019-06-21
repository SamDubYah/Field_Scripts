#!/bin/bash
# Simple bash ping sweep program to get list of online hosts. 
# Outputs hosts in nice format for host file creation

for i in {1..254};
        do ping -c 1 -W 1 10.11.1.$i | grep 'from' | cut -d " " -f4 | cut -d ":" -f1;
done
