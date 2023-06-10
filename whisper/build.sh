#/bin/bash
yum -y update
yum -y install git ffmpeg
pip install git+https://github.com/openai/whisper.git
