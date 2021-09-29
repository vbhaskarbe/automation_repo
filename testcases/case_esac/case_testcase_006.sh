#!/bin/bash
## Author : Bhaskar Varadaraju

## Functional, Regressio, Negative

testname=`echo "$0" | sed 's/.sh$//'`

echo "Testcase_006   : Execute 03_case_esac.sh with no cli input"
tc_exp_result='ERROR: At least one argument is required for this script'
tc_act_result=`bash 03_case_esac.sh`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_006   : PASS"
	touch ${testname}.pass
else
	echo "Expected Result: $tc_exp_result" > ${testname}.fail
	echo "Actual Result  : $tc_act_result" >> ${testname}.fail
	echo "Testcase_006   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

