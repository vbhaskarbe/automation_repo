#!/usr/local/bin/python
## Author : Bhaskar Varadaraju
##
## A Python script to update results in Testrails for given project and run id
##

from testrail import *
from pprint import pprint
import os.path
import json  

## Testrails Url and credentials
client          = APIClient('https://vbhaskar.testrail.io')
client.user     = 'vbhaskarmtech@gmail.com'
client.password = 'dF4pT57vrDXXSxA'

## The Project name and Run name to update results
#EX:tr_project_name = 'Training_Demo'
#EX:tr_testrun_name = 'Test_Run_003'
tr_project_name = 'TR_PROJECT_NAME'
tr_testrun_name = 'TR_TESTRUN_NAME'

tr_project_id   = -1
tr_testrun_id   = -1
tr_run_results  = {}

tr_results_file = open('./testrails_results.txt', 'r')
for line in tr_results_file:
    tr_case_pair = line.rstrip().split(":")
    tr_run_results[tr_case_pair[0]] = tr_case_pair[1]

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
        print("The run id of the given run name %s is: %s"%(tr_testrun_name, tr_testrun_id))

## Find all the tests from the given run id
case = client.send_get("get_tests/%s"%(tr_testrun_id))
for test in case['tests']:
    case_id     = test['case_id']
    if str(case_id) in tr_run_results.keys():
        print("Id is %s, Caseid is %s, Title is: %s"%(test['id'], test['case_id'],test['title']))
        case_result = tr_run_results[str(case_id)]
    else:
        next
    case_status_id = 1
    if case_result == 'PASS':
        case_status_id = 1
    elif case_result == 'FAIL':
        case_status_id = 5
    ## Update results for the Run in the given project    
    result = client.send_post( "add_result_for_case/%s/%s"%(tr_testrun_id, case_id),
        	    { 'status_id': case_status_id, 'comment': 'This test has been verified successfully.' }
             )

