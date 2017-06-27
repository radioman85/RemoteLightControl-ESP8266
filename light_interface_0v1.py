#!/usr/bin/python
from urllib2 import Request, urlopen, URLError, HTTPError
import urllib2
import base64
import time
import string_functions

object_name = 'light'


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
        
        object_id = object_name + '_id: ' + str(id)
        
        ip_address_dict       = string_functions.get_key_word_content(object_id, lights_str, 'ip_address')
        requested_status_dict = string_functions.get_key_word_content(object_id, lights_str, 'requested_status')
                
        
        if('object_id not found' == ip_address_dict['error_msg']):
            no_further_lights_found = True 
            print('no more object found')
            
        else:
            print(object_id)
            
            if('no_error' != ip_address_dict['error_msg']):
                    print('error message: ' + ip_address_dict['error_msg'])

            if('no_error' != requested_status_dict['error_msg']):
                print('error message: ' + requested_status_dict['error_msg'])
        
            print('ip_address: ' + ip_address_dict['key_word_content'])
            print('requested_status: ' + requested_status_dict['key_word_content'])
            print('\n')
        
            index_offset = lights_str.find(object_id)
            start_index = index_offset + len('light_id: ' + str(id) + '\nrequested_status: ')

            print('turn light ' + str(id) + ' on')

            url_request = 'http://192.168.0.50/LED=' + requested_status_dict['key_word_content']
            print(url_request)
            req = urllib2.Request(url_request)

            try:
                response = urlopen(req)
            except HTTPError as e:
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
            except URLError as e:
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            else:
                
                print(req)
                res = urllib2.urlopen(req)
                print('light has turned ' + res.read())
        
        id = id+1
    
    time.sleep(1)
    
    

