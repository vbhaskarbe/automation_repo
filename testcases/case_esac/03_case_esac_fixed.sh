#!/usr/local/bin/bash
# Author: Bhaskar Varadaraju
#
# A Shell program to check demonstrate use of case..esac construct
#
# Execute is as : bash 03_case_esac.sh <option> 
#TOOL="jenkins"

#echo "Enter a tool (jenkins, jira, git, sonarqube): "
#read TOOL
if test $# -eq 0
then
	echo "ERROR: At least one argument is required for this script"
	exit
fi

TOOL=$1
case "$TOOL" in
   "jenkins") echo "jenkins is a CI/CD tool."
   ;;
   "jira") echo "jira is a bug reporting and agile tool." 
   ;;
   "git") echo "git is one of source-control management tool." 
   ;;
   "sonarqube") echo "sonarqube is code coverage and static analysis tool"
   ;;
   *) echo "invalid tool $TOOL. valid inputs are: jenkins, git, jira, sonarqube."
   ;;
esac


