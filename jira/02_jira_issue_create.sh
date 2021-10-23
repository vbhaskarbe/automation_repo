#!/bin/zsh
##
## Author: Bhaskar Varadaraju
## A CURL command to create an issue and assign to engineer
## 
## Usage : zsh <script_name> jira_username jira_password
## 	 	   Example: zsh -f 02_jira_issue_create.sh jirauser 'welcome123#'
##

curl -u $1:$2 -X POST -d @./jira_issue_data.json -H "Content-Type: application/json" http://3.7.173.94:8090/rest/api/2/issue


