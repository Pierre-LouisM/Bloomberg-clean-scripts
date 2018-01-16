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
request = refDataService.createRequest("HistoricalDataRequest")

request.append("securities", "AAPL US Equity")

#FIELDS - if simply one field use: #request.append("fields", "PX_LAST")
#If you wish to loop the fields
field_list = ["PX_OPEN","PX_HIGH","PX_LAST","PX_VOLUME"]
for field in field_list:
    request.append("fields", field)

request.set("startDate", "20170101")
request.set("endDate", "20170201")
request.set("adjustmentFollowDPDF", "False")
request.set("adjustmentAbnormal", "True")
request.set("adjustmentNormal", "True")
request.set("adjustmentSplit", "True")
request.set("periodicitySelection", "DAILY")
request.set("nonTradingDayFillOption", "NON_TRADING_WEEKDAYS") #also takes ALL_CALENDAR_DAYS and ACTIVE_DAYS_ONLY
request.set("nonTradingDayFillMethod", "PREVIOUS_VALUE")



print "Sending Request:", request
session.sendRequest(request)


endReached = False
while endReached == False:
    ev = session.nextEvent()
    if ev.eventType() == blpapi.Event.RESPONSE or ev.eventType() == blpapi.Event.PARTIAL_RESPONSE:
           
        for msg in ev:
             numPoints = msg.getElement("securityData").getElement("fieldData").numValues()
             for i in range(0,numPoints):
                 Point = msg.getElement('securityData').getElement('fieldData').getValueAsElement(i)
                 print Point.getElement('date').getValue(),'\t',Point.getElement('PX_LAST').getValue(),'\t'
            
            
    if ev.eventType() == blpapi.Event.RESPONSE:
        endReached = True