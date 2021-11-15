#!/bin/bash


CONFIG_FILE=
SUITE_FILE=
DOCKER_COMMAND=
LOG_DIR="/tmp/cctaf_logs"
SOURCE_CODE="NA"
PYTEST_ARGUMENTS="-v"
USER_DEFINED_VNC_PORT=5900
USER_PROVIDED_VNC_SERVER_PASSWORD="password"
CONTAINER_NAME="DEFAULT_CCTAF_CONTAINER1"

#########################
# The command line help #
#########################
display_help() {
	echo "NAME"
	echo ""
	echo "execute_cctaf.sh"
	echo ""
	echo "SYNOPSIS"
	echo ""
	echo "		Usage: $0 [option...] {config_file|suite_file|source_code_location|log_dir|pytest_arguments|vnc_port|vnc_password|container_name}" >&2
	echo
	echo "DESCRIPTION"
	echo "		-config_file		Mandatory	Provide the config file location e.g /data/anpradha.yaml"
	echo "		-suite_file_location	Mandatory	Provide the suite file to run with location"
	echo "							e.g Single Suite: cctaf/suites/features/amazon/test01_admin/test01_bundles/API/test_api_bundles.py"
	echo "							e.g All Suites  : cctaf/suites/features/amazon/test01_admin/test01_bundles/"
	echo "		-source_code_location	Mandatory 	Provide your Source Code. "
	echo "							Local Run: Please Provide the absolute Path e.g /Users/anpradha/git/optimus2 ."
	echo "							Build Run: Please Provide the Build Tag e.g release-4.10.0-20180926.0"
	echo "		-log_dir		Optional	Default Value /tmp/cctaf_logs"
	echo "		-pytest_arguments	Optional	Default Value -v"
	echo "		-vnc_port		Optional	Default Value 5900"
	echo "		-vnc_password		Optional	Default Value password"
	echo "		-container_name		Optional	Customized Conatiner Name , Default name of the suite"
	exit 1
}

#Check if Docker is installed or not
check_and_run_docker_command()
{
	if [[ $(which docker) && $(docker --version) ]]; then
    		#echo -e "docker is installed and ready to proceed.\n"
    		docker pull "dockerhub.cisco.com/cloudcenter-dev-docker/cctaf_selenium_docker" >> "${LOG_DIR}/cctaf_docker.log" 2>&1 &
		echo "Docker Command : $DOCKER_COMMAND"
		eval $(echo $DOCKER_COMMAND) >  "${LOG_DIR}/cctaf_docker.log" 2>&1 &
  	else
    		echo -e "Please Install docker\n"
    		# command
		exit 1
	fi
	echo -e "End of subroutine\n"
}


while [ "$1" != "" ]; do
    case $1 in
        -h | --help)
         	 display_help  # Call your function
         	 exit 0
         	 ;;

        -config_file)           
				shift
				CONFIG_FILE=$1
                                ;;
        -suite_file_location)
				shift    
				SUITE_FILE=$1
				temp=$SUITE_FILE
				temp=$(echo ${temp//'.py'/""})
				IFS='/'  read -ra NAMES <<< "$temp"
				CONTAINER_NAME=${NAMES[${#NAMES[@]}-1]}
                                ;;
        -source_code_location)
				shift
				SOURCE_CODE=$1
                                ;;
        -pytest_arguments)
                                shift
                                PYTEST_ARGUMENTS=$1
                                ;;
        -vnc_port)
                                shift
                                USER_DEFINED_VNC_PORT=$1
                                ;;
        -vnc_password)
                                shift
                                USER_PROVIDED_VNC_SERVER_PASSWORD=$1
                                ;;
        -container_name)
                                shift
                                CONTAINER_NAME=$1
                                ;;

        -log_dir)         
				shift
				LOG_DIR=$1
                                ;;
        * )                     echo -e "${BIRed}INVALID ARG OPTION {$1} ${Color_Off}"
				display_help
                        	exit 1
    esac
    shift
done


if [ "$CONFIG_FILE" == "" ];then
	echo "ERROR: CONFIG_FILE Value not set Please Pass CONFIG_FILE e.g /data/anpradha.yml"
	display_help
   	exit 1
fi

if [ "$SUITE_FILE" == "" ];then
   	echo "ERROR: SUITE_FILE Value not set Please Pass SUITE_FILE e.g cctaf/suites/features/amazon/test01_admin/test01_bundles/API/test_api_bundles.py"
	display_help
   	exit 1
fi

if [ "$SOURCE_CODE" == "" ];then
   	echo "ERROR: SOURCE_CODE Value not set Please Pass SOURCE_CODE e.g /Users/anpradha/git/optimus2"
	display_help
   	exit 1
fi


# Create Log Directory if Not Present
mkdir -p $LOG_DIR


echo "CONFIGURATION FILE NAME   : ${CONFIG_FILE}" 							2>>  "${LOG_DIR}/cctaf_docker.log"
echo "SUITE FILE NAME           : ${SUITE_FILE}" 							2>>  "${LOG_DIR}/cctaf_docker.log"
echo "SUITE EXECUTION LOG PATH  : ${LOG_DIR}" 								2>>  "${LOG_DIR}/cctaf_docker.log"
echo "SOURCE CODE LOCATION      : ${SOURCE_CODE}" 							2>>  "${LOG_DIR}/cctaf_docker.log"
echo "EXECUTION LOG PATH        : ${LOG_DIR}/cctaf_docker.log" 						2>>  "${LOG_DIR}/cctaf_docker.log"
#echo "VNC PORT                  : ${USER_DEFINED_VNC_PORT}" 						2>>  "${LOG_DIR}/cctaf_docker.log"
#echo "VNC PASSWORD              : ${USER_PROVIDED_VNC_SERVER_PASSWORD}" 				2>>  "${LOG_DIR}/cctaf_docker.log"
#echo "PYTEST ARGUMENTS          : ${PYTEST_ARGUMENTS}" 							2>>  "${LOG_DIR}/cctaf_docker.log"
#echo "ACTIVE CONTAINER NAME     : ${CONTAINER_NAME}" 							2>>  "${LOG_DIR}/cctaf_docker.log"
#echo "DOCKER IMAGE NAME         : dockerhub.cisco.com/cloudcenter-dev-docker/cctaf_selenium_docker" 	2>>  "${LOG_DIR}/cctaf_docker.log"


if [[ $SOURCE_CODE = *"release"* ]]; then
	DOCKER_COMMAND="docker run --rm  \
-p $USER_DEFINED_VNC_PORT:5900 \
-e CONFIG_FILE=$CONFIG_FILE \
-e VNC_SERVER_PASSWORD=$USER_PROVIDED_VNC_SERVER_PASSWORD \
-e SUITE_FILE=$SUITE_FILE \
-e PYTEST_ARGUMENTS="\"${PYTEST_ARGUMENTS}\"" \
-e SOURCE_CODE=$SOURCE_CODE \
-v $LOG_DIR:/tmp/cctaf_logs \
-v $CONFIG_FILE:/tmp/config_file.yml \
--privileged \
--shm-size=2g \
--name=cctaf_docker1 dockerhub.cisco.com/cloudcenter-dev-docker/cctaf_selenium_docker"

else
	# Below steps required for avoiding python cache issue 
	cd $SOURCE_CODE
	find . -name \*.pyc -delete
        DOCKER_COMMAND="docker run --rm \
-p $USER_DEFINED_VNC_PORT:5900 \
-e CONFIG_FILE=$CONFIG_FILE \
-e VNC_SERVER_PASSWORD=$USER_PROVIDED_VNC_SERVER_PASSWORD \
-e SUITE_FILE=$SUITE_FILE \
-e PYTEST_ARGUMENTS="\"${PYTEST_ARGUMENTS}\"" \
-e SOURCE_CODE=$SOURCE_CODE \
-v $LOG_DIR:/tmp/cctaf_logs \
-v $SOURCE_CODE:/optimus2 \
-v $CONFIG_FILE:/tmp/config_file.yml \
--privileged \
--shm-size=2g \
--name=$CONTAINER_NAME dockerhub.cisco.com/cloudcenter-dev-docker/cctaf_selenium_docker"

fi

#$DOCKER_COMMAND  >  "${LOG_DIR}/cctaf_docker.log" 2>&1 &

check_and_run_docker_command

