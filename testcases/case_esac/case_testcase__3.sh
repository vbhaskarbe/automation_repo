#!/bin/bash
## Author : Bhaskar Varadaraju

## Type: Functional, Regression

testname=`echo "$0" | sed 's/.sh$//'`

echo "Testcase_003   : Execute 03_case_esac.sh with 'jira' as input"
tc_exp_result='jira is a bug reporting and agile tool.'
tc_act_result=`bash 03_case_esac.sh jira`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_003   : PASS"
	touch ${testname}.pass
else
	echo "Expected Result: $tc_exp_result" > ${testname}.fail
	echo "Actual Result  : $tc_act_result" >> ${testname}.fail
	echo "Testcase_003   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

