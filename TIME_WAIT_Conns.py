# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:41:49 2024

@author: B0060625
"""
import re , sys, platform
from dsk.profilers import DSKProfiler

prof = DSKProfiler()
prof.start_monitoring()

# =============================================================================
# if os.getlogin() == 'wrks_B0059870':
#     path = 'C:/Users/B0060625/DiscoveryRule_LogReader/conns_sfgwpprd.txt'
# else:
#     path = ''
#     
# =============================================================================

if platform.node() == 'DKHOVL004':
    path = 'C:/Users/B0060625/DiscoveryRule_LogReader/conns_sfgwpprd.txt'
else:
    path = '/home/mqecho/echo/conns_sfgwpprd.txt'


def main(ip):
    
    rx = re.compile(r'(?<=TIME_WAIT connections for port:\d\d\d\d\n)(.+)?<<' + str(ip) + '\: (\d{0,2})')

    with open(path) as f:
        
        lines = f.readlines(); 
         
        last_paragraph = lines[-8::1]   #hvashta poslednite 8 reda(1 paragraf) ot loga
        string1 = ""
        for i in last_paragraph:        #konvertira last_paragraph ot list vyv string
            string1 = string1+i+" " 
    
    matches = re.finditer(rx, string1)
    
    if re.search(rx , string1) is not None:
        for matchNum, match in enumerate(matches, start=1):
            
            # print ('The IP: '+ ip +' has {group} TIME_WAIT connection/s'.format(group = match.group(2)))            
            value = match.group(2)
            stats = prof.collect()
            stats.set("TIME_WAIT_connections" , value )
            value1 = stats.export()
            print(value1)

    else:
            value_zero = 0
            stats = prof.collect()
            stats.set("TIME_WAIT_connections" ,  value_zero )
            value1 = stats.export()
            print(value1)
        
main(sys.argv[1])  #argument koito se vika ot vyn






