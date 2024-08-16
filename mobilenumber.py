# imports random
'''import random
lower_limit =8000000000 # Can be anything
upper_limit =9999999999 # Again, can be anything
number=(random.randint(lower_limit,upper_limit))
#siva=(9,8,7)
# Print it out
print(number)

#############

import requests

url = "https://www.mailinator.com/v4/public/inboxes.jsp?msgid=audri-life-1621576672-238902"

payload="{\r\n    \"high\": \"0.61468\",\r\n    \"last\": \"0.76978\",\r\n    \"timestamp\": \"1613392121\",\r\n    \"bid\": \"0.56949\",\r\n    \"vwap\": \"0.56487\",\r\n    \"volume\": \"98155343.58302319\",\r\n    \"low\": \"0.51100\",\r\n    \"ask\": \"0.57019\",\r\n    \"open\": \"0.59339\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=node0x7azezlke5m7ipguwue31bza127313.node0; SERVERID=s1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)'''


Add =(input("First number= "))
Add1=(input("Second number= "))
print("The Result is",float(Add)+float(Add1))






