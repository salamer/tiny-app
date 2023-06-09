#/bin/bash
pip3 install --upgrade pip cmake transformers
yum -y update
yum -y install gcc make git build-essential g++ clang
python pre.py