#python-alpine linux base image
FROM python:3-alpine

#docker file maintainer
LABEL maintainer="anushreeshenoy3@gmail.com"

#copy requirements.txt
COPY requirements.txt /requirements.txt
#copy source code to docker workspace
COPY src /opt/test/src/

#set python path environment variable
ENV PYTHONPATH /opt/test/src/

#upgrade pip and setup tools
#install 
RUN pip install --upgrade pip && \
pip install --upgrade setuptools && \
pip install -r requirements.txt

#set working directory
WORKDIR /opt/test/src

#execute robot script
CMD python -m robot -d output/ api_automation.robot;\
