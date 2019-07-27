## Synopsis

The Project uses Robot framework collaborated with Python to test API end points.

### Prerequisites

1. Running docker service
2. Requirements file present as requirements.txt file

### Project Structure
src -  directory that consists of keyword file, properties file and python script
properties.robot - Properties file with input values such as URL, input to be given, expected output
api_automation.robot - BDD test cases in Given When Then format. This file uses input from properties.robot file and invokes methods from main_service.py
main_service.py - implementation of each keyword used in api_auromation.robot file.

### Execution Steps
1. Checkout project from github
2. Navigate to directory same as that of Dockerfile
3. Build docker image using following command
docker build -t testapi .
4. Execute docker image created using following command
docker run --rm -it -v ${PWD}:/opt/test/src/output testapi
5. Following files are created:
report.html - Summary of Test Suite execution
log.html - detailed description of test scripts
output.xml - output log
