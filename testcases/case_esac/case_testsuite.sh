#!/bin/bash
## Author: Bhaskar Varadaraju
##

echo "Execute testsuite to test 'case' construct"
for testcase in `ls -1 case_testcase*.sh`
do
	echo "Executing testcase $testcase...."
	bash $testcase
done
