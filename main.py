#! /bin/env python3

try:
	import time
	import os, sys
	import zlib, base64
	exec(zlib.decompress(base64.b64decode('eJzLL9ZLzkjJLNJQ18vJTFLXtC6uLNYrSCzJ0EssKEjNS9HIL9ZLTy1JLk/R0NTkAgB0qg90')))
	from api import *
except ImportError:
	print("\033[1;32m[\033[1;31m!\033[1;32m] Use Orignal Script")
	print("\033[1;32m[\033[1;31m!\033[1;32m] github.com/th3unkn0n/osi.ig")
	sys.exit()

try:
	while True:
		try:
			os.system('clear')
			osi_ig.banner()
			ig = osi_ig(username=input(f'{colors.OKGREEN}[{colors.RED}+{colors.OKGREEN}] Enter User name :{colors.CYN} '))
			ig.print_profile_data()
			print(colors.HEADER + "---------------------------------------------" + colors.ENDC)
			sfile=input(f'{colors.OKGREEN}[{colors.RED}+{colors.OKGREEN}] Save Data To File ? [ y / n ] :{colors.CYN} ')
			if sfile.lower() == "y":
				ig.save_data()
			else:
				pass
			print(colors.HEADER + "---------------------------------------------" + colors.ENDC)
			sfile=input(f'{colors.OKGREEN}[{colors.RED}+{colors.OKGREEN}] Save Pictures To File ? [ y / n ] :{colors.CYN} ')
			if sfile.lower() == "y":
				ig.scrape_posts()
			else:
				pass
		except NameError:
			print(f'{colors.OKGREEN}[{colors.RED}!{colors.OKGREEN}] 404 : User Not Found ')
			time.sleep(5)
			pass
except KeyboardInterrupt:
	os.system('clear')
	osi_ig.banner()
	print(f'\n{colors.OKGREEN}[{colors.RED}+{colors.OKGREEN}] Quitting ...\n')
	pass

"""
Code By : th3unkn0n
YouTube : youtube.com/theunknon
"""
