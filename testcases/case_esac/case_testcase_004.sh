#!/bin/bash
## Author : Bhaskar Varadaraju

echo "Testcase_004   : Execute 03_case_esac.sh with 'sonarqube' as input"
tc_exp_result='sonarqube is code coverage and static analysis tool'
tc_act_result=`bash 03_case_esac.sh sonarqube`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_004   : PASS"
else
	echo "Expected Result: $tc_exp_result"
	echo "Actual Result  : $tc_act_result"
	echo "Testcase_004   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

