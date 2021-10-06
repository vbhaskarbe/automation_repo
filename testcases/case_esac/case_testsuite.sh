#!/bin/bash
## Author: Bhaskar Varadaraju
##
## This is the driver script that runs all tests 
## Usage: bash case_testsuite.sh [Functional|Regression|Negative]
## 

test $# -eq 0 && test_tag='Functional' || test_tag=$1

testname=`echo "$0" | sed 's/.sh$//'`
echo "Execute testcases matching tag $test_tag to test 'case' construct"
for testcase in `grep -l "$test_tag" case_testcase*.sh`
do
	## Remove old pass/fail files for this testcase
	test -f ${testname}.pass && rm -f ${testname}.pass
	test -f ${testname}.fail && rm -f ${testname}.pass

	echo "Executing testcase $testcase...."
	bash $testcase
done

if test ls *.fail
then
	exit 1
else
	exit 0
fi
