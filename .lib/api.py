#!/bin/env python3

import time
import json
import random
import string
import os, sys
import requests
import collections
import urllib.request
from bs4 import BeautifulSoup

nu = '\033[0m'
re = '\033[1;31m'
gr = '\033[1;32m'
cy = '\033[1;36m'

raw_tags = []
tag_lis = []

useragent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7']

class extra():

	def tiny_url(url):
		apiurl = "http://tinyurl.com/api-create.php?url="
		tinyurl = urllib.request.urlopen(apiurl + url).read()
		return tinyurl.decode("utf-8")

	def write(in_text):
		for char in in_text:
			time.sleep(0.1)
			sys.stdout.write(char)
			sys.stdout.flush()

	def extract_hash_tags(stri): 
		return list(part[1:] for part in stri.split() if part.startswith('#'))

	def banner():
		print(f"""{cy}
 ╔═╗  ╔═╗  ╦     ╦  ╔═╗
 ║ ║  ╚═╗  ║     ║  ║ ╦
 ╚═╝  ╚═╝  ╩  {gr}o{cy}  ╩  ╚═╝
 
        {gr}Code By :
  {gr}youtube.com/theunknon{nu}
	            """)

class main():

	def __init__(self, user):
		self.user = user
		self.get_profile()

	def get_profile(self):
		if bs4.__version__ == '4.6.0':
			pass
		else:
			print(f"\n{gr}[!] {nu}currunt verion of bs4 module isn't supported \n{gr}[+] {nu}Downgrading beautifulsoup")
			os.system("python3 -m pip install beautifulsoup4==4.6.0")
			os.execv('main.py', sys.argv)
			
		extra.write(f"\n{gr}[+]{nu} getting profile ...")
		profile = requests.get(f"https://www.instagram.com/{self.user}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'})
		soup = BeautifulSoup(profile.text, 'html.parser')
		more_data = soup.find_all('script', attrs={'type': 'text/javascript'})
		self.data = json.loads(more_data[3].get_text()[21:].strip(';'))
		self.p_data = self.data['entry_data']['ProfilePage'][0]['graphql']['user']
		self.output = {
			"username         ": str(self.p_data['username']),
			"name             ": str(self.p_data['full_name']),
			"url              ": str(f"instagram.com/{self.p_data['username']}"),
			"followers        ": str(self.p_data['edge_followed_by']['count']),
			"following        ": str(self.p_data['edge_follow']['count']),
			"posts            ": str(self.p_data['edge_owner_to_timeline_media']['count']),
			"bio              ": str(self.p_data['biography'].replace('\n', ', ')),
			"external url     ": str(self.p_data['external_url']),
			"private          ": str(self.p_data['is_private']),
			"verified         ": str(self.p_data['is_verified']),
			"profile pic url  ": extra.tiny_url(str(self.p_data['profile_pic_url_hd'])),
			"business account ": str(self.p_data['is_business_account']),
			"connected to fb  ": str(self.p_data['connected_fb_page']),
			"joined recently  ": str(self.p_data['is_joined_recently']),
			"business category": str(self.p_data['business_category_name'])
		}

		if str(self.p_data['is_private']).lower() == 'true':
			print(f"{re}[!]{gr} private profile can't scrap data !\n")
			return 1
		else:
			for index, post in enumerate(self.p_data['edge_owner_to_timeline_media']['edges']):
				try:
					raw_tags.append(extra.extract_hash_tags(post['node']['edge_media_to_caption']['edges'][0]['node']['text']))
				except IndexError:
					pass
			x = len(raw_tags)
			for i in range(x):
				tag_lis.extend(raw_tags[i])
			self.tags = dict(collections.Counter(tag_lis))

		return self.tags
		return self.output

	def print_data_(self):
		os.system("clear")
		extra.banner()
		for key, value in self.output.items():
			print(f"{gr}{key} : {nu}{value}")
		print("")
		print(f"{gr}[+]{nu} most used user tags : \n")
		o = 0
		for key, value in collections.Counter(self.tags).most_common():
			print(f"{gr}{key} : {nu}{value}")
			o += 1
			if o == 5:
				break
		print("")

	def print_data(self):
		os.system("clear")
		extra.banner()
		for key, value in self.output.items():
			print(f"{gr}{key} : {nu}{value}")
		print("")


	def make_dir(self):
		try:
			os.mkdir(self.user)
			os.chdir(self.user)
		except FileExistsError:
			os.chdir(self.user)

	def scrap_uploads(self):
		if self.output["private          "].lower() == 'true':
			print(f"{re}[!]{gr} private profile can't scrap data !\n")
			return 1
		else:
			posts = {}
			print(f"{gr}[+]{nu} user uploads data : \n")
			for index, post in enumerate(self.p_data['edge_owner_to_timeline_media']['edges']):
				# GET PICTURE URL AND SHORTEN IT
				print(f"{gr}picture : {nu}{extra.tiny_url(str(post['node']['thumbnail_resources'][0]['src']))}")
				# IF PIC HAS NO CAPTIONS > SKIP / PRINT
				try:
					print(f"{gr}Caption : {nu}{post['node']['edge_media_to_caption']['edges'][0]['node']['text']}")
				except IndexError:
					pass
				posts[index] = {
					"comments": str(post['node']['edge_media_to_comment']['count']),
					"comments disabled": str(post['node']['comments_disabled']),
					"timestamp": str(post['node']['taken_at_timestamp']),
					"likes": str(post['node']['edge_liked_by']['count']),
					"location": str(post['node']['location']),
					"accessability caption": str(post['node']['accessibility_caption'])}

				for key, value in posts[index].items():
					print(f"{gr}{key} : {nu}{value}")
				print("")

	def most_common_tags(self):
		print(f"{gr}[+]{nu} user uploads tags : \n")
		for key, value in collections.Counter(self.tags).most_common():
			print(f"{gr}{key} : {nu}{value}")

	def save_data(self):
		self.make_dir()
		# DOWNLOAD PROFILE PICTURE
		with open(f"profile_pic.jpg", "wb") as f:
			time.sleep(1)
			r = requests.get(self.output['profile pic url  '], headers={'User-Agent':random.choice(useragent)})
			f.write(r.content)
		print(f"{gr}[+]{nu} saved pic to {os.getcwd()}/profile_pic.jpg")

		# SAVES PROFILE DATA TO TEXT FILE
		self.output_data = {
			"username": str(self.p_data['username']),
			"name": str(self.p_data['full_name']),
			"url": str(f"instagram.com/{self.p_data['username']}"),
			"followers": str(self.p_data['edge_followed_by']['count']),
			"following": str(self.p_data['edge_follow']['count']),
			"posts": str(self.p_data['edge_owner_to_timeline_media']['count']),
			"bio": str(self.p_data['biography']),
			"external url": str(self.p_data['external_url']),
			"private": str(self.p_data['is_private']),
			"verified": str(self.p_data['is_verified']),
			"profile pic url": extra.tiny_url(str(self.p_data['profile_pic_url_hd'])),
			"business account": str(self.p_data['is_business_account']),
			"connected to fb": str(self.p_data['connected_fb_page']),
			"joined recently": str(self.p_data['is_joined_recently']),
			"business category": str(self.p_data['business_category_name'])
		}
		with open(f"profile_data.txt", "w") as f:
			f.write(json.dumps(self.output_data))
		print(f"{gr}[+]{nu} saved data to {os.getcwd()}/profile_data.txt")

		# SAVES POST INFORMATION
		posts = {}
		for index, post in enumerate(self.p_data['edge_owner_to_timeline_media']['edges']):
			posts[index] = {
				"comments": str(post['node']['edge_media_to_comment']['count']),
				"comments disabled": str(post['node']['comments_disabled']),
				"timestamp": str(post['node']['taken_at_timestamp']),
				"likes": str(post['node']['edge_liked_by']['count']),
				"location": str(post['node']['location']),
				"accessability caption": str(post['node']['accessibility_caption'])}

			posts[index]["picture"] = extra.tiny_url(str(post['node']['thumbnail_resources'][0]['src']))			
			try:
				post[index]['caption'] = str(post['node']['edge_media_to_caption']['edges'][0]['node']['text'])
			except KeyError:
				pass

		with open(f"posts_data.txt", 'w') as f:
			f.write(json.dumps(posts))
		print(f"{gr}[+]{nu} saved post info to {os.getcwd()}/posts_data.txt")

		# SAVES TAGS
		with open(f"tags.txt", 'w') as f:
			f.write(json.dumps(tag_lis))
		print(f"{gr}[+]{nu} saved tags to {os.getcwd()}/posts_data.txt\n")
