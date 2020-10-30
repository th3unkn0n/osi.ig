#!/bin/env python3

import os, sys
sys.path.append(os.getcwd()+"/.lib/")
import argparse
from api import *

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="username of account to scan")
ap.add_argument("-p", "--post", action="store_true", help="image info of user uploads")
# ap.add_argument("-t", "--tor", action="store_true", help="make all requests over tor")
# ap.add_argument("-s", "--save", action="store_true", help="save all info to file")
# ap.add_argument("-i", "--info", action="store_true", help="reverse lookup img / media")
args = vars(ap.parse_args())
	
os.system("clear")

if args['user']:
	user_info(usrname=args["user"])

if args['post']:
	post_info()

# if args['save']:
# 	pass
# if args['tor']:
# 	pass
# if args['info']:
# 	pass