import requests
url = "https://www.baidu.com"
headers = ""
response = requests.get(url)

print(response.encoding)
print(response.headers)
print(response.status_code)
#print(response.text)
print(response.content)