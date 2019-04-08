import ticketpy
import json
import pandas as pd
from time import sleep

# Initialize client with your Ticketmaster API key.
tm_client = ticketpy.ApiClient('W08meX2jz2HhnqRAGk00YXZf8tJaBDgG')


pages = tm_client.events.find(
    state_code='CA'
#    start_date_time='2019-05-01T00:00:00Z',
#    end_date_time='2019-05-30T00:00:00Z'
)

e = None

i = 0
for page in pages:
    for event in page:
        print(i)
        print(json.dumps(event.json, indent=4, sort_keys=True))
        i += 1
    break
print("done")
        
        
        
        
"""        
        e.json
    ###getName
        name = event['name']
    ###get Time Start 
        start_time =event['sales']['public']['startDateTime']
    ###get Time End
        end_time = event['sales']['public']['endDateTime']
    ###get event type i.e. music
    ###should fix to have subclasses and other classes attached
        event_type = event['classifications'][0]['segment']['name']
    ###get Address
        address = event['_embedded']['venues'][0]['location']
    ###get Event Description
        if 'info' in event.keys():
            description = event['info']
        else:
            description = 'None'
        listx = [name,start_time,end_time,event_type,address,description]
        eventlist.append(listx)
        
df=pd.DataFrame(eventlist,columns = ['Name','Start Time','End Time','Event Type', 'Address','Description'])
        
        
df
"""