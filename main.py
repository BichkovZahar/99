import urllib.request
opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())
import requests
response = requests.get('https://coinmarketcap.com/')
print(response.text)
response_parse = response.text.split('<span>')
for elen in response_parse:
    if elen.startswith("$"):
        print(elen)
