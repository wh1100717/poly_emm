#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import hashlib
import simplejson

def token_generator():
	code = str(time.time()) + str(random.randint(1, 100000))
	return hashlib.md5(code).hexdigest()

def active_code_generator():
	return str(random.randint(10000,99999))

def string2dict(input_string):
	input_string.replace("'", '"')
	return simplejson.loads(input_string)
