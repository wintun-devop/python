#!/bin/bash
#Win Tun Hlaing(https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos)
#http://www.mmuak.net or https://mmuak.blogspot.com/
#python3.9 installation
add-apt-repository ppa:deadsnakes/ppa -y

#update the packages
apt update -y 

#install python3.9 package
apt install -y python3.9

#for specific pip3.9
apt install python3.9-distutils

#Installing python-devel,python3-pip and mysql-devel
apt install -y python3-dev default-libmysqlclient-dev build-essential python3-pip


