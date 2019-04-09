from urllib.request import Request, urlopen
import json, re, requests
from time import sleep

# Open a CSV to write the data into.
target_file = "event_data.csv"
csv = open(target_file, "w") 
columnTitleRow = "url, description\n"
csv.write(columnTitleRow)

# Headers and url for the HTTP requests.
headers = {
  'Authorization': 'Bearer 46C7DRU6HYXZWUPZSXPI',
  'Content-Type': 'application/json'
}

url_address = 'https://www.eventbriteapi.com/v3/events/search'
request = Request(url_address, headers=headers)

# Find out total number of pages
response = requests.get(url=url_address+"?page="+str(201), headers=headers).json()
#num_pages = int(response['pagination']["page_count"])
print(json.dumps(response, indent=4, sort_keys=True))


"""
# Loop through all pages.
i = 1
for page_num in range(1, num_pages):
    url = url_address+"?page="+str(page_num)              
    response = requests.get(url=url, headers=headers).json()        
    for element in response["events"]:
        i += 1
        try:
            description = element["description"]["text"]
            description = re.sub("[^a-zA-Z]", " ", str(description))
            url = element["url"]
            # Write data to file.
            row = url + "," + description + "\n"
            csv.write(row)
        except:
            print("Exception at", i)
            continue
    print(i)
    page_num += 1
"""