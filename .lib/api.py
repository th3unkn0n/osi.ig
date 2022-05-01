#!/bin/env python3

import requests
import random
import json
import sys
from local import *

resp_js = None
is_private = False
total_uploads = 10

def proxy_session():
	session = requests.session()
	session.proxies = {
		'http':  'socks5://127.0.0.1:9050',
		'https': 'socks5://127.0.0.1:9050'
	}
	return session

def get_page(usrname):
	global resp_js
	session = requests.session()
	session.headers = {'User-Agent': random.choice(useragent)}
	resp_js = session.get('https://www.instagram.com/'+usrname+'/?__a=1').text
	return resp_js

def exinfo():

	def xprint(xdict, text):
		if xdict != {}:
			print(f"{su} {re}most used %s :" % text)
			i = 0
			for key, val in xdict.items():
				if len(mail) == 1:
					if key in mail[0]:
						continue
				print(f"  {gr}%s : {wh}%s" % (key, val))
				i += 1
				if i > 4:
					break
			print()
		else:
			pass
	
	raw = find(resp_js)

	mail = raw['email']
	tags = sort_list(raw['tags'])
	ment = sort_list(raw['mention'])

	if mail != []:
		if len(mail) == 1:
			print(f"{su} {re}email found : \n{gr}  %s" % mail[0])
			print()
		else:
			print(f"{su} {re}email found : \n{gr}  ")
			for x in range(len(mail)):
				print(mail[x])
			print()

	xprint(tags, "tags")
	xprint(ment, "mentions")
	
def user_info(usrname):

	global total_uploads, is_private
	
	resp_js = get_page(usrname)
	js = json.loads(resp_js)  # maybe an HTML perser would fix the bug?
	js = js['graphql']['user']
	
	if js['is_private'] != False:
		is_private = True
	
	if js['edge_owner_to_timeline_media']['count'] > 12:
		pass
	else:
		total_uploads = js['edge_owner_to_timeline_media']['count']

	usrinfo = {
		'username': js['username'],
		'user id': js['id'],
		'name': js['full_name'],
		'followers': js['edge_followed_by']['count'],
		'following': js['edge_follow']['count'],
		'posts img': js['edge_owner_to_timeline_media']['count'],
		'posts vid': js['edge_felix_video_timeline']['count'],
		'reels': js['highlight_reel_count'],
		'bio': js['biography'].replace('\n', ', '),
		'external url': js['external_url'],
		'private': js['is_private'],
		'verified': js['is_verified'],
		'profile img': urlshortner(js['profile_pic_url_hd']),
		'business account': js['is_business_account'],
		#'connected to fb': js['connected_fb_page'],  -- requires login
		'joined recently': js['is_joined_recently'],
		'business category': js['business_category_name'],
		'category': js['category_enum'],
		'has guides': js['has_guides'],
	}

	banner()

	print(f"{su}{re} user info")
	for key, val in usrinfo.items():
		print(f"  {gr}%s : {wh}%s" % (key, val))

	print("")

	exinfo()

def highlight_post_info(i):

	postinfo = {}
	total_child = 0
	child_img_list = []

	x = json.loads(resp_js)
	js = x['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']

	# this info will be same on evry post
	info = {
		'comments': js['edge_media_to_comment']['count'],
		'comment disable': js['comments_disabled'],
		'timestamp': js['taken_at_timestamp'],
		'likes': js['edge_liked_by']['count'],
		'location': js['location'],
	}

	# if image dosen't have caption this key dosen't exist instead of null
	try:
		info['caption'] = js['edge_media_to_caption']['edges'][0]['node']['text']
	except IndexError:
		pass

	# if uploder has multiple images / vid in single post get info how much edges are
	if 'edge_sidecar_to_children' in js:
		total_child = len(js['edge_sidecar_to_children']['edges'])

		for child in range(total_child):
			js = x['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_sidecar_to_children']['edges'][child]['node']
			img_info = {
				'typename': js['__typename'],
				'id': js['id'],
				'shortcode': js['shortcode'],
				'dimensions': str(js['dimensions']['height'] + js['dimensions']['width']),
				'image url' : js['display_url'],
				'fact check overall': js['fact_check_overall_rating'],
				'fact check': js['fact_check_information'],
				'gating info': js['gating_info'],
				'media overlay info': js['media_overlay_info'],
				'is_video': js['is_video'],
				'accessibility': js['accessibility_caption']
			}

			child_img_list.append(img_info)

		postinfo['imgs'] = child_img_list
		postinfo['info'] = info

	else:
		info = {
			'comments': js['edge_media_to_comment']['count'],
			'comment disable': js['comments_disabled'],
			'timestamp': js['taken_at_timestamp'],
			'likes': js['edge_liked_by']['count'],
			'location': js['location'],
		}

		try:
			info['caption'] = js['edge_media_to_caption']['edges'][0]['node']['text']
		except IndexError:
			pass

		img_info = {
				'typename': js['__typename'],
				'id': js['id'],
				'shortcode': js['shortcode'],
				'dimensions': str(js['dimensions']['height'] + js['dimensions']['width']),
				'image url' : js['display_url'],
				'fact check overall': js['fact_check_overall_rating'],
				'fact check': js['fact_check_information'],
				'gating info': js['gating_info'],
				'media overlay info': js['media_overlay_info'],
				'is_video': js['is_video'],
				'accessibility': js['accessibility_caption']
			}
		
		child_img_list.append(img_info)
		
		postinfo['imgs'] = child_img_list
		postinfo['info'] = info

	return postinfo

def post_info():
	
	if is_private != False:
		print(f"{fa} {gr}cannot use -p for private accounts !\n")
		sys.exit(1)
	
	posts = []
	
	for x in range(total_uploads):
		posts.append(highlight_post_info(x))

	for x in range(len(posts)):
		# get 1 item from post list
		print(f"{su}{re} post %s :" % x)
		for key, val in posts[x].items():
			if key == 'imgs':
				# how many child imgs post has
				postlen = len(val)
				# loop over all child img
				print(f"{su}{re} contains %s media" % postlen) 
				for y in range(postlen):
					# print k,v of all child img in loop
					for xkey, xval in val[y].items():
						print(f"  {gr}%s : {wh}%s" % (xkey, xval))
			if key == 'info':
				print(f"{su}{re} info :")
				for key, val in val.items():
					print(f"  {gr}%s : {wh}%s" % (key, val))
				print("")	
