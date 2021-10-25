#!/usr/local/bin/python
## Author : Bhaskar Varadaraju
##
##  A Python OOPs script to update jenkins test run results in Testrails
## for given project and run id
##

from testrail import *
from pprint import pprint
import os.path
import json  

class UpdateResultsInTestRails():
    def __init__(self, **kwargs):
        ## Initialize known data params
        for vkey in kwargs.keys():
            self.__setattr__(vkey, kwargs[vkey])
        ## Initialize compute params
        self.tr_test_results = {}
        self.tr_project_id   = -1
        self.tr_testrun_id   = -1
        ## Initialize client 
        self.tr_client          = APIClient(self.tr_url)
        self.tr_client.user     = self.username
        self.tr_client.password = self.password

    ## Load the results from file to a dictionary
    def load_test_results_in_dict(self):
        tr_results_fh = open( self.tr_results_file, 'r')
        for line in tr_results_fh:
            tr_case_pair = line.rstrip().split(":")
            self.tr_test_results[tr_case_pair[0]] = tr_case_pair[1]
        print(self.tr_test_results)
    
    ## Get the project id of given project name - tr_project_name
    def find_project_id_for_name(self):
        case = self.tr_client.send_get('get_projects/1')
        for project in case['projects']:
            if project['name'] == self.tr_project_name:
                self.tr_project_id = project['id']
                print("The Project id of the Project '%s' is: %s" %(self.tr_project_name, self.tr_project_id))

    ## Get all run id from above project for given run name - tr_testrun_name
    def find_run_id_for_name(self):
        case = self.tr_client.send_get("get_runs/%s"%(self.tr_project_id))
        for run in case['runs']:
            if run['name'] == self.tr_testrun_name:
                self.tr_testrun_id = run['id']
                print("The Run id of the given Run '%s' is: %s"%(self.tr_testrun_name, self.tr_testrun_id))
        
    ## Get all the tests from the given run id
    def update_results_for_runid(self):
        case = self.tr_client.send_get("get_tests/%s"%(self.tr_testrun_id))
        for test in case['tests']:
            case_id     = test['case_id']
            if str(case_id) not in self.tr_test_results.keys():
                continue
            print("Id is %s, Caseid is %s, Title is: %s"%(test['id'], test['case_id'],test['title']))
            case_result = self.tr_test_results[str(case_id)]
            case_status_id = 1 if  case_result == 'PASS' else 5
            ## Update results for the Run in the given project    
            result = self.tr_client.send_post( "add_result_for_case/%s/%s"%(self.tr_testrun_id, case_id),
        	            { 'status_id': case_status_id, 'comment': 'This test has been verified successfully.' } )
## Test/Use above locally
if __name__ == '__main__':
    tr_handler = UpdateResultsInTestRails(
                    tr_url   = 'https://vbhaskar.testrail.io',
                    username = 'vbhaskarmtech@gmail.com',
                    password = 'dF4pT57vrDXXSxA',
                    #tr_project_name = 'TR_PROJECT_NAME',
                    #tr_testrun_name = 'TR_TESTRUN_NAME',
                    tr_project_name = 'Training_Demo',
                    tr_testrun_name = 'Test_Run_004',
                    tr_results_file = './testrails_results.txt'
                )
    tr_handler.load_test_results_in_dict()
    tr_handler.find_project_id_for_name()
    tr_handler.find_run_id_for_name()
    tr_handler.update_results_for_runid()
## End of file
