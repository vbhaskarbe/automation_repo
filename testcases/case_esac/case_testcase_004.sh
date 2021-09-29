#!/bin/bash
## Author : Bhaskar Varadaraju

## Type: Functional, Regression

testname=`echo "$0" | sed 's/.sh$//'`

echo "Testcase_004   : Execute 03_case_esac.sh with 'sonarqube' as input"
tc_exp_result='sonarqube is code coverage and static analysis tool'
tc_act_result=`bash 03_case_esac.sh sonarqube`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_004   : PASS"
	touch ${testname}.pass
else
	echo "Expected Result: $tc_exp_result" > ${testname}.fail
	echo "Actual Result  : $tc_act_result" >> ${testname}.fail
	echo "Testcase_004   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

