# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:13:46 2017

@author: pmonnot
"""

import blpapi
import datetime

# Create a Session
session = blpapi.Session()
# Start a Session
if not session.start():
    print "Failed to start session."
if not session.openService("//blp/refdata"):
    print "Failed to open //blp/refdata"

refDataService = session.getService("//blp/refdata")
request = refDataService.createRequest("IntradayTickRequest")

request.set("security", "VOD LN Equity")
request.getElement("eventTypes").appendValue("TRADE")
request.getElement("eventTypes").appendValue("AT_TRADE")
request.getElement("eventTypes").appendValue("BEST_ASK")
request.getElement("eventTypes").appendValue("BEST_BID")
request.set("includeConditionCodes", True)

# Date format (YYYY, M, D), Time format (H, M, S)
StartDate = datetime.date(2017,7,03)
StartTime = datetime.time(10,0,0)
Start = datetime.datetime.combine(StartDate,StartTime)
request.set("startDateTime", Start)

EndDate = datetime.date(2017,7,03)
EndTime = datetime.time(10,1,0)
End = datetime.datetime.combine(EndDate,EndTime)
request.set("endDateTime", End)
request.set("includeNonPlottableEvents", True)

print "Sending Request:", request
session.sendRequest(request)


endReached = False
while endReached == False:
    ev = session.nextEvent()
    if ev.eventType() == blpapi.Event.RESPONSE or ev.eventType() == blpapi.Event.PARTIAL_RESPONSE:
        for msg in ev:
            #find how many ticks we have

             numTicks= msg.getElement('tickData').getElement('tickData').numValues()
             for i in range (0,numTicks):    
                     Tick = msg.getElement('tickData').getElement('tickData').getValueAsElement(i)#.getElement('size').getValue()
                     if Tick.hasElement('time'):
                         print Tick.getElement('time').getValue(), "\t",Tick.getElement('type').getValue(), "\t",Tick.getElement('value').getValue(), "\t",Tick.getElement('size').getValue(), "\t"

            
            
            
            
    if ev.eventType() == blpapi.Event.RESPONSE:
        endReached = True