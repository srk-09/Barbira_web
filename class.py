import requests

#from bs4 import BeautifulSoup
# Make a GET request to the login page
response = requests.get("https://betalaunchpad.classlink.com/login")

# Parse the HTML response
soup =(response.text, "html.parser")

# Extract the CSRF token from the form
csrf_token = requests.("input", {"name": "csrf_token"})["value"]

# Store the CSRF token for use in future requests
print("CSRF Token:", csrf_token)
