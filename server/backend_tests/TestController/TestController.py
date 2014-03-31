#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=======================
#### file: TestController.py ####
#=======================

import sys
import os
import nose
from nose import with_setup
import urllib2
import urllib


c_path = os.getcwd()
base_path = c_path[:c_path.rfind("backend_tests")]
sys.path.append(base_path)

##所有的测试模块import在这下面：
##################UserController##########################

import string
import random
from util import StringUtil
from controller import UserController


def random_tel():
	tel_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	tel_start = ['13','15','14','18']
	b = string.join(random.sample(tel_list,9)).replace(" ","")
	a = random.choice(tel_start)
	tel = a+b
	return tel

tel = random_tel()
random_name = StringUtil.token_generator()
email = StringUtil.token_generator() + '@qq.com'


def test_RegisterHandler_by_tel():
	postData = {
		'email_or_phone':tel,
		'user_name':random_name,
		'pwd':'111111',
		'pwd_confirm':'111111',
		'accept':'on',

	}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request('http://localhost/user/register', postData)
	response = urllib2.urlopen(request) 
	register_tel = response.read() 
	register_tel = eval(register_tel)
	assert register_tel['status'] == 1


def test_RegisterHandler_by_email():
	postData = {
		'email_or_phone':email,
		'user_name':random_name,
		'pwd':'111111',
		'pwd_confirm':'111111',
		'accept':'on'

	}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request('http://localhost/user/register', postData)
	response = urllib2.urlopen(request) 
	register_email = response.read() 
	register_email = eval(register_email)
	assert register_email['status'] == 1


def test_LoginHandler_by_tel():
	postData={
		'email_or_phone':tel,
		'pwd':'111111'
	}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request('http://localhost/user/login', postData) 
	response = urllib2.urlopen(request) 
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1


def test_LoginHandler_by_email():
	postData={
		'email_or_phone':email,
		'pwd':'111111'
	}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request('http://localhost/user/login', postData) 
	response = urllib2.urlopen(request) 
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1



# def test_AddHandler():
# 	cj = cookielib.LWPCookieJar() 
# 	cookie_support = urllib2.HTTPCookieProcessor(cj) 
# 	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
# 	urllib2.install_opener(opener) 


# def test_LogoutHandler():
	