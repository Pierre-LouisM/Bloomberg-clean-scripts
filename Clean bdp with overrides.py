Created on Mon Feb 22 19:14:46 2017

@author: pmonnot
"""



import blpapi

session = blpapi.Session()
if not session.start():
    print "Failed to start session."
if not session.openService("//blp/refdata"):
    print "Failed to open service."

service = session.getService("//blp/refdata")
request = service.createRequest("ReferenceDataRequest")

security_list = ["IBM US Equity","AAPL US Equity","GE US Equity"]
for ticker in security_list:
    request.append("securities", ticker)

request.append("securities","AAPL US Equity")

request.append("fields","RETURN_COM_EQY")

overrides = request.getElement("overrides")

override1 = overrides.appendElement()
override1.setElement("fieldId","FUND_PER")
override1.setElement("value","Q1")

override2 = overrides.appendElement()
override2.setElement("fieldId","EQY_FUND_YEAR")
override2.setElement("value","2015")

session.sendRequest(request)

endReached = False
while endReached == False:
    ev = session.nextEvent()
    if ev.eventType() == blpapi.Event.RESPONSE or ev.eventType() == blpapi.Event.PARTIAL_RESPONSE:
        for msg in ev:
            print msg
    if ev.eventType() == blpapi.Event.RESPONSE:
        endReached = True