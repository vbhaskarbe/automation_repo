#!/bin/bash
## Author : Bhaskar Varadaraju

## Type: Functional, Regression

testname=`echo "$0" | sed 's/.sh$//'`

echo "Testcase_002   : Execute 03_case_esac.sh with 'jenkins' as input"
tc_exp_result='jenkins is a CI/CD tool.'
tc_act_result=`bash 03_case_esac.sh jenkins`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_002   : PASS"
	touch ${testname}.pass
else
	echo "Expected Result: $tc_exp_result" > ${testname}.fail
	echo "Actual Result  : $tc_act_result" >> ${testname}.fail
	echo "Testcase_002   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

