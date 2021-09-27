#!/bin/bash
## Author : Bhaskar Varadaraju

echo "Testcase_005   : Execute 03_case_esac.sh with 'querty' as input"
tc_exp_result='invalid tool querty. valid inputs are: jenkins, git, jira, sonarqube.'
tc_act_result=`bash 03_case_esac.sh querty`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_005   : PASS"
else
	echo "Expected Result: $tc_exp_result"
	echo "Actual Result  : $tc_act_result"
	echo "Testcase_005   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

