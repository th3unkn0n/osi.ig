#!/bin/env python3

import requests
import sys, time
import collections
import re as r

nu = "\033[0m"
re = "\033[1;31m"
gr = "\033[0;32m"
cy = "\033[0;36m"
wh = "\033[0;37m"
ye = "\033[0;34m"

su = f"\033[1;31m[\033[1;36m+\033[1;31m]{nu}"
fa = f"\033[1;31m[\033[1;31m!\033[1;31m]{nu}"
er = f"\033[1;31m[\033[1;34m?\033[1;31m]{nu}"

# 30-33, 48-50, 94-96, 195-210

def urlshortner(url):
    data = requests.get("http://tinyurl.com/api-create.php?url=" + url)
    return data.text

def sort_list(xlist):
    with_count = dict(collections.Counter(xlist))
    output = {k: v for k, v in sorted(with_count.items(), reverse=True, key=lambda item: item[1])}
    return output
    
def find(stri):
    exinfo = {}
    email = r.findall(r"[_a-z0-9-\.]+[＠@]{1}[a-z0-9]+\.[a-z0-9]+", stri)
    exinfo['email'] = email

    tags = r.findall(r"[＃#]{1}([_a-zA-Z0-9\.\+-]+)", stri)
    exinfo['tags'] = tags
	mention = []
    raw_mention = r.findall(r"[＠@]{1}([_a-zA-Z0-9\.\+-]+)", stri)
	for x in raw_mention:
        if x.endswith("."):
            x = x.strip(".")
        mention.append(x)
    exinfo['mention'] = mention

    return exinfo

def banner():
		print(f"""{cy}
 ╔═╗  ╔═╗  ╦     ╦  ╔═╗
 ║ ║  ╚═╗  ║     ║  ║ ╦
 ╚═╝  ╚═╝  ╩  {gr}o{cy}  ╩  ╚═╝
 
        {gr}Code By :
  {gr}youtube.com/theunknon{nu}
	            """)

useragent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2849.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) Crmo/16.0.912.75 Mobile Safari/535.7']
