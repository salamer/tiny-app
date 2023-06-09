#/bin/bash
pip3 install --upgrade pip cmake
yum -y update
yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum -y install gcc make git build-essential g++ clang git-lfs
git lfs install
git clone git@hf.co:csebuetnlp/mT5_multilingual_XLSum