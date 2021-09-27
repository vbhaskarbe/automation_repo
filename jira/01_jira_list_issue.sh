#!/bin/zsh
##
## Author: Bhaskar Varadaraju
## A CURL command to list all the issues in a given project in JIRA
## 
## Usage : zsh <script_name> jira_username jira_password project_id
## 	 	   Example: zsh -f 01_jira_list_issue.sh jirauser 'welcome123#' 10000
## 

curl -u $1:$2 -X GET -H "Content-Type: application/json" http://3.7.173.94:8090/rest/api/2/project/$3 | python3 -mjson.tool | grep -e '"id"' -e '"description"'



