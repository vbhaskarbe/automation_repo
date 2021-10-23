#!/bin/bash
## Author : Bhaskar Varadaraju

## Type: Functional, Regression

testname=`echo "$0" | sed 's/.sh$//'`

echo "Testcase_001   : Execute 03_case_esac.sh with 'git' as input"
tc_exp_result='git is one of source-control management tool.'
tc_act_result=`bash 03_case_esac.sh git`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_001   : PASS"
    touch ${testname}.pass
else
	echo "Expected Result: $tc_exp_result" > ${testname}.fail
	echo "Actual Result  : $tc_act_result" >> ${testname}.fail
	echo "Testcase_001   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

