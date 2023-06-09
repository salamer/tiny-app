#/bin/bash
pip3 install --upgrade pip cmake
yum -y update
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | bash
yum -y install gcc make git build-essential g++ clang git-lfs amazon-linux-extras
amazon-linux-extras install epel -y 
yum-config-manager --enable epel
git lfs install
git clone git@hf.co:csebuetnlp/mT5_multilingual_XLSum