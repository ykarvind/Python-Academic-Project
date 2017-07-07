'''
Created on Jun 1, 2017

@author: macbookpro
'''

import urllib.request 
import json  

class Tour():
    #Tour constructor
    def __init__(self,origin, destination):
        self.origin=origin
        self.destination=destination
    
    #distance method    
    def distance(self,mode='Driving'):        
        originValue=self.origin.replace(' ','+')
        destValue=self.destination.replace(' ','+')
        modeValue=mode.replace(' ','+')    
        parameters='origins='+originValue+'&destinations='+destValue+'&mode='+modeValue+'&sensor=false'
        url='http://maps.googleapis.com/maps/api/distancematrix/json'        
        url=url+'?'+parameters            
        webObj = urllib.request.urlopen(url)
        webStr = webObj.read().decode('utf-8')
        result = json.loads(webStr)         
        topStatus = result["status"] 
        if topStatus == 'OK':
            rows = result["rows"] 
            elements = rows[0]["elements"] 
            status = elements[0]["status"] 
            if status == 'OK':
                distance=elements[0]["distance"]            
                value=distance['value']
            else:
                raise ValueError('Distance between '+self.origin+' and '+self.destination+' not found.')
        else:
            raise ValueError('Distance between '+self.origin+' and '+self.destination+' not found.')
        
        return value