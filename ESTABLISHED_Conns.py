# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:13:57 2024

@author: B0060625
"""

import re,platform
import sys
from dsk.profilers import DSKProfiler

prof = DSKProfiler()
prof.start_monitoring()

if platform.node() == 'DKHOVL004':
    path = 'C:/Users/B0060625/DiscoveryRule_LogReader/conns_sfgwpprd.txt'
else:
    path = '/home/mqecho/echo/conns_sfgwpprd.txt'
    
def main(ip):
    
    # ip = '10.100.11.46'
    rx = re.compile(r'(?<=ESTABLISHED connections for port:\d\d\d\d\n)(.+)?<<' + str(ip) + '\: (\d{0,2})')

    with open(path) as f:
        
        lines = f.readlines(); 
         
        last_paragraph = lines[-8::1]   #hvashta poslednite 8 reda(1 paragraf) ot loga
        string1 = ""
        for i in last_paragraph:        #konvertira last_paragraph ot list vyv string
            string1 = string1+i+" " 
    
    matches = re.finditer(rx, string1)
    
    if re.search(rx , string1) is not None:     

        for matchNum, match in enumerate(matches, start=1):
            # print ('The IP: '+ ip +' has {group} ESTABLISHED connection/s'.format(group = match.group(2)))
            
            value = match.group(2)
            stats = prof.collect()
            stats.set("ESTABLISHED_connections" , value )
            value1 = stats.export()
            print(value1)
    else:
        # print('The IP: ' +ip+ ' has no ESTABLISHED connections.')
            value_zero = 0
            stats = prof.collect()
            stats.set("ESTABLISHED_connections" ,  value_zero )
            value1 = stats.export()
            print(value1)
        
        
main(sys.argv[1])  #argument koito se vika ot vyn , priema IP-to podadeno ot zabbix discovery rule-a
