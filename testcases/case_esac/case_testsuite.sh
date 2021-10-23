#!/bin/bash
## Author: Bhaskar Varadaraju
##
## This is the driver script that runs all tests 
## Usage: bash case_testsuite.sh [Functional|Regression|Negative]
## 

test $# -eq 0 && test_tag='Functional' || test_tag=$1

true > testrails_results.txt
echo "Execute testcases matching tag $test_tag to test 'case' construct"
for testcase in `grep -l "$test_tag" case_testcase*.sh`
do
	testname=`echo "${testcase%%.*}"`
	## Remove old pass/fail files for this testcase
	test -f ${testname}.pass && rm -f ${testname}.pass
	test -f ${testname}.fail && rm -f ${testname}.pass

	echo "Executing testcase $testcase...."
	bash $testcase
	tr_case_id=`echo $testname | awk -F'__' '{print $2}'`
	if test -f ${testname}.pass
	then
		echo "$tr_case_id:PASS" >> testrails_results.txt
	elif test -f ${testname}.fail
	then
		echo "$tr_case_id:FAIL" >> testrails_results.txt
	else
		echo "Nothing happened"
	fi
done
echo "Testrails results have been recorded in file: testrails_results.txt"
