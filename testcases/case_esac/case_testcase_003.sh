#!/bin/bash
## Author : Bhaskar Varadaraju

echo "Testcase_003   : Execute 03_case_esac.sh with 'jira' as input"
tc_exp_result='jira is a bug reporting and agile tool.'
tc_act_result=`bash 03_case_esac.sh jira`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_003   : PASS"
else
	echo "Expected Result: $tc_exp_result"
	echo "Actual Result  : $tc_act_result"
	echo "Testcase_003   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

