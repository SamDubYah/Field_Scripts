#!/bin/bash
#Simpe zone transfer script

# check if an argument was given, if not display usage
if [ -z "$1" ]; then
echo "[*] Simple Zone transfer script"
echo "[*] Usage   :$0 <domain name> "
exit 0
fi


#if an argument was give, identify DNS servers for the domain
for server in $(host -t ns $1 |cut -d " " -f4);do
#for each of these servers, attemps a zone transfer
host -l $1 $server |grep "has address"
done
