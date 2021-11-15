import requests

r = requests.get('https://www.google.com/')
#print(r.status_code)
#print(r.content)
#print(r.headers)
print(r.request.headers)