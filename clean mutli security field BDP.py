# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:22:37 2017

@author: pmonnot
"""

import blpapi

session = blpapi.Session()

if not session.start():
	print "Failed to start the sesh"
if not session.openService("//blp/refdata"):
	print " Failed to open //blp/refdata"

service = session.getService("//blp/refdata")
request = service.createRequest("ReferenceDataRequest")

sc = ["/isin/US25468PBW59","FP FP Equity"]
for j in sc:
   request.append("securities",j)


fd = ["PX_LAST","PX_BID"]
for i in fd:
    request.append("fields",i)


session.sendRequest(request)

endReached = False
while endReached == False:
    ev = session.nextEvent()
    if ev.eventType() == blpapi.Event.RESPONSE or ev.eventType() == blpapi.Event.PARTIAL_RESPONSE:
        for msg in ev:
            print msg
    if ev.eventType() == blpapi.Event.RESPONSE:
        endReached = True