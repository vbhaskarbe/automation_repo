
from 'testrail' import *
#import testrail

client = APIClient("http://testrail.cisco.com/index.php?/suites/view/217");
client.user = 'bhasvara@cisco.com'
client.password = 'Welcome2Cliqr!'

case = client.send_get('get_case/1')
pprint(case)

