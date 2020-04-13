#!/bin/env python3

import os, sys
sys.path.append(os.getcwd()+"/.lib/")
import argparse
from api import *

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=True, help="username of account to scan")
ap.add_argument("-p", "--postscrap", action='store_true', help="scrape all uploaded images info ")
ap.add_argument("-s", "--savedata", action='store_true', help="save data to file")
args = vars(ap.parse_args())
	
os.system("clear")
ig = main(user=args["username"])
ig.print_data()

if args['postscrap']:
	ig.scrap_uploads()

if args['savedata']:
	ig.save_data()
