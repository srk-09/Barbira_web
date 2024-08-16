import requests

url = "https://stg-seithi.mediacorp.sg/api/v1/cia/content-list?_format=json&type=article"

payload = ""
headers = {
  'Authorization': 'Basic bWVkaWFjb3JwI0BjbXM6bWVkaWFjb3JwQCMhMSM='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.title())
