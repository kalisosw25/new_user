import requests
from requests.structures import CaseInsensitiveDict

url = "http://boburbem.beget.tech/"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "code='hellooo'"


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
print(resp.text)
print(resp.content)
