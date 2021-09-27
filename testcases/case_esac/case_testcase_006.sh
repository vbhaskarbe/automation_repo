#!/bin/bash
## Author : Bhaskar Varadaraju

echo "Testcase_006   : Execute 03_case_esac.sh with no cli input"
tc_exp_result='no input given to the program.'
tc_act_result=`bash 03_case_esac.sh`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_006   : PASS"
else
	echo "Expected Result: $tc_exp_result"
	echo "Actual Result  : $tc_act_result"
	echo "Testcase_006   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

