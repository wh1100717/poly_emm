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
import urllib
import urllib2
import cookielib
from dao import UserDao

#生成随机电话号码
def random_tel():
	tel_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	tel_start = ['13','15','14','18']
	b = string.join(random.sample(tel_list,9)).replace(" ","")
	a = random.choice(tel_start)
	tel = a+b
	return tel

tel = random_tel()
random_name = StringUtil.token_generator()
# email = StringUtil.token_generator() + '@qq.com'
phone = StringUtil.token_generator()
owner = StringUtil.token_generator()
tid = ''
active_code = ''
token = ''
did = StringUtil.token_generator()
cid = StringUtil.token_generator()
imei = StringUtil.token_generator()



#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}


def test_LogoutHandler():
	request = urllib2.Request('http://localhost/user/logout')
	response = urllib2.urlopen(request) 
	# assert cj._cookies['tid']=='' and cj._cookies['timestamp']==''



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


# def test_RegisterHandler_by_email():
# 	postData = {
# 		'email_or_phone':email,
# 		'user_name':random_name,
# 		'pwd':'111111',
# 		'pwd_confirm':'111111',
# 		'accept':'on'

# 	}
# 	postData = urllib.urlencode(postData) 
# 	request = urllib2.Request('http://localhost/user/register', postData)
# 	response = urllib2.urlopen(request) 
# 	register_email = response.read() 
# 	register_email = eval(register_email)
# 	assert register_email['status'] == 1


def test_LoginHandler_by_tel():
	#print tel
	postData={
		'email_or_phone':tel,
		'pwd':'111111'
	}
	postData = urllib.urlencode(postData) 
	req  = urllib2.Request(
        url = 'http://localhost/user/login',
        data = postData,
        headers = headers
    )
	response = urllib2.urlopen(req) 
	text = response.read() 
	text=eval(text)

	#print "\n", cj._cookies
	assert text['status'] ==1



# def test_LoginHandler_by_email():

# 	#获取一个保存cookie的对象
# 	cj = cookielib.LWPCookieJar()
# 	#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
# 	cookie_support = urllib2.HTTPCookieProcessor(cj)
# 	#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
# 	opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# 	#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
# 	urllib2.install_opener(opener)

# 	postData={
# 		'email_or_phone':email,
# 		'pwd':'111111'
# 	}
# 	postData = urllib.urlencode(postData) 
# 	request = urllib2.Request('http://localhost/user/login', postData) 
# 	response = urllib2.urlopen(request) 
# 	text = response.read() 
# 	text=eval(text)
# 	assert text['status'] ==1


def test_AddHandler():
		
	postData={
		'phone':phone,
		'owner':owner,
	}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request(
        url = 'http://localhost/device/add',
        data = postData,
        headers = headers
    )
	response = urllib2.urlopen(request) 
	text = response.read() 
	text=eval(text)

	#print "\n",cj._cookies

	assert text['status'] ==1



def test_ListHandler():
	postData={
	}
	postData = urllib.urlencode(postData)
	request = urllib2.Request(
		url = 'http://localhost/device/list',
		data = postData,
		headers = headers
	)
	response = urllib2.urlopen(request)
	text = response.read()
	text = text.replace('false','"false"')
	text = eval(text)
	# print text
	
	#模拟激活tid，active_code
	global tid
	global active_code
	tid = text['data'][0]['tid']
	active_code = text['data'][0]['active_code']
	# print tid
	# print active_code

	assert text['status'] == 1

#模拟激活
def test_EnrollHandler():
	
	postData={
			'tid':tid,
			'active_code':active_code,
			'phone':phone
		}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request(
	    url = 'http://localhost/android/enroll',
	    data = postData,
	    headers = headers
	)
	response = urllib2.urlopen(request) 
	text = response.read() 
	text=eval(text)
	
	global token
	token = text['token']

	assert text['status'] ==1

#模拟设备初始化
def test_InitialHandler():
	
	postData={
				'token':token,
				'phone':phone,
				'did':did,
				'cid':cid,
				'imei':imei
			}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request(
	    url = 'http://localhost/android/initial',
		data = postData,
		headers = headers
	)
	response = urllib2.urlopen(request) 
	text = response.read() 
	text=eval(text)

	assert text['status'] ==1














