#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import hashlib

def token_generator():
	code = str(time.time()) + str(random.randint(1, 100000))
	return hashlib.md5(code).hexdigest()