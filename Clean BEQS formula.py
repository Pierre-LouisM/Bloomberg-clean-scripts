import blpapi

#CreateSession
session = blpapi.Session()
#Start Session
if not session.start():
    print "Failed start"
if not session.openService("//blp/refdata"):
    print "Failed open"

refDataService = session.getService("//blp/refdata")
request = refDataService.createRequest("BeqsRequest")
request.set("screenName","NAME OF YOUR SCREEN AS YOU SAVED IT ON TERMINAL")
request.set("screenType","PRIVATE")

session.sendRequest(request)

cookies = []

endReached = False
while endReached == False:
    ev = session.nextEvent()
    if ev.eventType() == blpapi.Event.RESPONSE or ev.eventType() == blpapi.Event.PARTIAL_RESPONSE:
        for msg in ev:
            for j in range (0, msg.getElement("data").getElement("securityData").numValues() - 1):
              cookies.append(msg.getElement("data").getElement("securityData").getValue(j).getElement("security").getValue())


    if ev.eventType() == blpapi.Event.RESPONSE:
        endReached = True

requestbdp = refDataService.createRequest("ReferenceDataRequest")

fields = "PX_LAST"

for i in cookies:
    requestbdp.append("securities", i + " Equity")


requestbdp.append("fields", fields)


session.sendRequest(requestbdp)

endReached = False
while endReached == False:
    ev = session.nextEvent()
    if ev.eventType() == blpapi.Event.RESPONSE or ev.eventType() == blpapi.Event.PARTIAL_RESPONSE:
        for msg in ev:
            print msg
    if ev.eventType() == blpapi.Event.RESPONSE:
        endReached = True
