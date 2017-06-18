#!/usr/bin/python

import urllib2
import base64
import time


print ('\n\n\n\n******************************')
print ('***   Light Interface')
print ('******************************')

while(1):
    
    print('\n \\\\\>>>   Light Status   <<<</// \n')

    lights_file  = open('light.txt', 'r')
    lights_str   = lights_file.read()
    
    id = 1
    no_further_lights_found = False
    
    while(False == no_further_lights_found):
        
        index_offset = lights_str.find('light_id: ' + str(id))
        start_index = index_offset + len('light_id: ' + str(id) + '\nrequested_status: ')
        
        if(-1 == lights_str.find('light_id: ' + str(id))):
             no_further_lights_found = True 
        
        elif('on' == lights_str[start_index:(start_index + len('on'))]):
            print 'turn light ' + str(id) + ' on'
            
            req = urllib2.Request('http://192.168.0.50/LED=ON')
            res = urllib2.urlopen(req)
            print 'light has turned ' + res.read()
        
        elif('off' ==  lights_str[start_index:(start_index + len('off'))]):
            print 'turn light ' + str(id) + ' off'
            req = urllib2.Request('http://192.168.0.50/LED=OFF')
            res = urllib2.urlopen(req)
            print 'light has turned ' + res.read()
        
        id = id+1
    
    time.sleep(1)
    
