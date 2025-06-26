FROM jenkins/ssh-agent:jdk17

RUN apt-get update
RUN apt-get -y install git mc nano vim

RUN apt-get -y install net-tools iproute2 iputils-ping

#######################################################
# Set up scan-host-key script
RUN set -eux
COPY ./scan-host-key.sh /
#######################################################

COPY ./setup-sshd /usr/local/bin/