import requests
from requests.auth import HTTPBasicAuth
import json

url = "http://3.7.173.94:8090/rest/api/2/project"

auth = HTTPBasicAuth("jirauser", "welcome123#")

headers = {
   "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


