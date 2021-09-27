#!/bin/bash
## Author : Bhaskar Varadaraju


echo "Testcase_002: Execute 03_case_esac.sh with 'jenkins' as input"
tc_exp_result='jenkins is a CI/CD tool.'
tc_act_result=`bash 03_case_esac.sh jenkins`
if test "X$tc_exp_result" == "X$tc_act_result"
then
	echo "Testcase_002: PASS"
else
	echo "Testcase_002: FAIL"
fi

