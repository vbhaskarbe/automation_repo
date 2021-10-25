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
case "`echo $TOOL|tr '[A-Z]' '[a-z]'`" in
   "jenkins") echo "$TOOL is a CI/CD tool."
   ;;
   "jira") echo "$TOOL is a bug reporting and agile tool."
   ;;
   "git") echo "$TOOL is one of source-control management tool." 
   ;;
   "sonarqube") echo "$TOOL is code coverage and static analysis tool"
   ;;
   "*") echo "invalid tool $TOOL. valid inputs are: jenkins, git, jira, sonarqube."
   ;;
esac


