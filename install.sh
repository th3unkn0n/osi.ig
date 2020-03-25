#!/bin/bash
clear
line="\e[1;31m[*]\e[0m"

echo -e "$line Starting Install ..."
echo -e "$line This May Take Some Time"
chmod 777 main.py
command -v python > /dev/null 2>&1 || apt install -y python
command -v python3 > /dev/null 2>&1 || apt install -y python
pip3 install -r modules
python3 -m pip install -r modules
echo -e "$line Install Complete"
echo -e "$line Use : python3 main.py"
