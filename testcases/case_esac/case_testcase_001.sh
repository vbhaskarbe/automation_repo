#!/bin/bash
## Author : Bhaskar Varadaraju

echo "Testcase_001   : Execute 03_case_esac.sh with 'git' as input"
tc_exp_result='git is one of source-control management tool.'
tc_act_result=`bash 03_case_esac.sh git`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_001   : PASS"
else
	echo "Expected Result: $tc_exp_result"
	echo "Actual Result  : $tc_act_result"
	echo "Testcase_001   : FAIL"
fi
echo "--------------------------------------------------------------------------------------"

