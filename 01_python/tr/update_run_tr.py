from testrail import *
from pprint import pprint
import os.path
import json  

tr_project_name = 'Training_Demo'
tr_testrun_name = 'Test_Run_003'
tr_project_id   = -1
tr_testrun_id   = -1
tr_run_results  = {}

client          = APIClient('https://vbhaskar.testrail.io')
client.user     = 'vbhaskarmtech@gmail.com'
client.password = 'dF4pT57vrDXXSxA'

tr_results_file = open('testrails_results.txt', 'r')
for line in tr_results_file:
    tr_case_pair = line.rstrip().split(":")
    tr_run_results[tr_case_pair[0]] = tr_case_pair[1]
print(tr_run_results)

## Find the project id of given project name - tr_project_name
case = client.send_get('get_projects/1')
for project in case['projects']:
    if project['name'] == tr_project_name:
        tr_project_id = project['id']
        print("The project id of the project named %s is: %s" %(tr_project_name, tr_project_id))

## Find all run id from above project for given run name - tr_testrun_name
case = client.send_get("get_runs/%s"%(tr_project_id))
for run in case['runs']:
    if run['name'] == tr_testrun_name:
        tr_testrun_id = run['id']
        print("The run id of the given run name %s for project %s is: %s"%(tr_testrun_name, tr_project_name, tr_testrun_id))

case = client.send_get("get_test/1")
pprint(case)

## Find all the tests from the given run id
case = client.send_get("get_tests/%s"%(tr_testrun_id))
for test in case['tests']:
    print("Id is %s, Caseid is %s, Title is: %s"%(test['id'], test['case_id'],test['title']))
    print("Result is %s"%(tr_run_results[test['case_id']]))
exit(1)

## POST index.php?/api/v2/add_result_for_case/:run_id/:case_id
#if os.path.isfile(testcase.pass):
result = client.send_post( "add_result_for_case/%s/%s"%(tr_testrun_id, ),
    	{ 'status_id': 1, 'comment': 'This test has been verified successfully.' }
        )
pprint(result)
