# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:32:42 2024

@author: B0060625
"""
#script za prihvashtane na vsichki unikalni IP-ta ot daden log

import re,json,platform

# start = time.time()
regex1 = re.compile(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')

if platform.node() == 'DKHOVL004':
    path = 'C:/Users/B0060625/DiscoveryRule_LogReader/conns_sfgwpprd.txt'
else:
    path = '/home/mqecho/echo/conns_sfgwpprd.txt'       #zamesten s aktualniq path
    
def ListReturn():
    list_ip = []
    # to match the unique IPs (regex1)
    for i,re.MULTILINE in enumerate(open(path)):
    
        for match in re.finditer(regex1, re.MULTILINE):
            if(match.group(0) not in list_ip):
                list_ip.append(match.group(0))
    return list_ip

    
l = ListReturn()
to_json_list = [{"IP" : n} for n in l]
json = json.dumps(to_json_list)    

ipFile = open('/home/mqecho/echo/IPs_extracted.txt' , 'w')  #directoriq s file-a v koito se zapisvat unikalnite IP-ta
                                                            #Promeni directoriqta ako testvash scripta lokalno
ipFile.write(json)
ipFile.close()

# end = time.time()
# res = end - start
# print('\nExecuted for ' + str(res) + " seconds.")