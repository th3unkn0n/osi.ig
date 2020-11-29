#!/bin/env python3

import re as r
import smtplib
import dns.resolver
from local import *

def validate_mail(mail):
	regex = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$"
	match = r.match(regex, mail)
	if match == None:
		print('regex : fail')
	else:
		print('regex : success')
	splitAddress = mail.split('@')
	domain = str(splitAddress[1])
	records = dns.resolver.resolve(domain, 'MX')
	mxr = records[0].exchange
	mxr = str(mxr)
	print('mx :', mxr.lower())
	fromaddr = 'no-reply@gmail.com'
	connect = smtplib.SMTP()
	connect.set_debuglevel(0)
	connect.connect(mxr)
	connect.helo(connect.local_hostname)
	connect.mail(fromaddr)
	code, message = connect.rcpt(str(mail))
	connect.quit()
	if code == 250:
		print('smtp : success')
	else:
		print('smtp : fail')