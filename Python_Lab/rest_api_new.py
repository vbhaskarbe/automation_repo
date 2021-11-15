import json
import requests

response = requests.post('https://api.github.com/user/repos',
    data=json.dumps({'name': 'foo'}), auth=('user', 'pass'))
    
assert response.status_code == 201


