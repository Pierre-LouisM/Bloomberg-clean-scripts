# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:14:49 2017

@author: pmonnot
"""

import blpapi 

session = blpapi.Session()
session.start() 

session.openService("//blp/pagedata")
service = session.getService("//blp/pagedata")

string = "0708/012/0001"
fields = ["15-18"]

subscriptions = blpapi.SubscriptionList()
subscriptions.add("//blp/pagedata/" + string,
                  fields, 
                  None,
                  blpapi.CorrelationId(string))

session.subscribe(subscriptions)

endReached = False 
while not endReached:
    
    ev = session.nextEvent()
    for msg in ev:
        print msg
        
