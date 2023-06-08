#/bin/bash
pip3 install --upgrade pip cmake
yum -y update
yum -y install gcc make git build-essential g++ clang

git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
cd ..
python3 setup.py install
