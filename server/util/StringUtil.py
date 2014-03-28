#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import hashlib
import simplejson
import re

def token_generator():
	code = str(time.time()) + str(random.randint(1, 100000))
	return hashlib.md5(code).hexdigest()

def active_code_generator():
	return str(random.randint(10000,99999))

def string2dict(input_string):
	input_string.replace("'", '"')
	return simplejson.loads(input_string)

def is_email(input_string):
	return True if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", input_string) else False

def is_phone(input_string):
	return True if re.match("^(13|14|15|18)\d{9}$", input_string) else False

def is_email_or_phone(input_string):
	return 'phone' if is_phone(input_string) else ('email' if is_email(input_string) else 'neither') 

