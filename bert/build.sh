#/bin/bash
pip3 install --upgrade pip cmake
yum -y update
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo bash

yum -y install gcc make git build-essential g++ clang git-lfs
git lfs install
git clone git@hf.co:csebuetnlp/mT5_multilingual_XLSum