#/bin/bash
pip3 install --upgrade pip cmake transformers sentencepiece protobuf==3.20.*
yum -y update
yum -y install gcc make git build-essential g++ clang
python pre.py