#!/bin/bash
# Code By : th3unkn0n
clear
line="\e[1;31m[*]\e[0m"

install () {
	echo -e "$line Starting Install ..."
	echo -e "$line This May Take Some Time"
	chmod 777 main.py
	command -v python > /dev/null 2>&1 || apt install -y python
	command -v python3 > /dev/null 2>&1 || apt install -y python
	pip3 install -r modules
	rm modules
	echo -e "$line Install Complete"
	echo -e "$line Use : python3 main.py"
}

echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1
if [[ $? -eq 0 ]]; then
	install
else
	echo -e "$line You Are Offline"
	exit 1
fi