#!/bin/bash
## Author : Bhaskar Varadaraju

## Type: Functional, Regressio, Negative

testname=`echo "$0" | sed 's/.sh$//'`

echo "Testcase_005   : Execute 03_case_esac.sh with 'querty' as input"
tc_exp_result='invalid tool querty. valid inputs are: jenkins, git, jira, sonarqube.'
tc_act_result=`bash 03_case_esac.sh querty`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_005   : PASS"
	touch ${testname}.pass
else
	echo "Expected Result: $tc_exp_result" > ${testname}.fail
	echo "Actual Result  : $tc_act_result" >> ${testname}.fail
	echo "Testcase_005   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

