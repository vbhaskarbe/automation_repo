#!/bin/bash

SCRIPT_PATH="/tmp/cctaf_docker.sh"
WGET_CMD=$(which wget)
USERNAME=cliqr
PASSWORD=welcome
DOCKER_HOST='http://artifacts.cliqrtech.com'

if [ 1 = "$(which wget ; echo $?)" ]; then
        echo "Wget Not present, Please Install Wget and Try again ."
	exit 1
	#brew install wget --with-libressl
else
	#echo "Download updated script file and save it to /tmp"
	#wget -N http://34.240.54.136/cctaf_docker.sh -P /tmp
	echo "INFO: $WGET_CMD -N --user $USERNAME --password $PASSWORD ${DOCKER_HOST}/cctaf_docker.sh"
	$WGET_CMD -N --user $USERNAME --password $PASSWORD ${DOCKER_HOST}/cctaf_docker.sh -P /tmp 2> /dev/null
fi

chmod 777 /tmp/cctaf_docker.sh
/tmp/cctaf_docker.sh  "$@"
