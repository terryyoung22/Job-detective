FROM ubuntu:latest

# ENV parameteres
ENV DEBIAN_FRONTEND=noninteractive
ARG WORKING_DIR=/app
WORKDIR ${WORKING_DIR}
COPY ${GITHUB_WORKSPACE} /app

# AWSCreds - Uncomment to move your aws credentials here
# RUN mkdir $HOME/.aws/
# RUN mv ./awscreds/* $HOME/.aws/
# RUN export AWS_PROFILE="yourAWSprofile"

# update
RUN apt update && apt install -y
RUN apt install -yqq curl wget gnupg2 unzip

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt -y update
RUN apt install -y google-chrome-stable

# install chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# install packages
RUN apt install -y python3-pip
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev vim python-dev
RUN pip3 install wheel requests selenium pandas bs4 awscli lxml
# ^ If above does not work: python3 -m pip install requests wheel selenium pandas bs4 lxml awscli
# RUN wget https://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip

## EXECUTE SCRIPT ##
CMD ["python3", "jobDetective.py"]