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
email = StringUtil.token_generator() + '@qq.com'

#随机选取注册方式：手机|邮箱
def random_email_or_phone():
	random_dict = {
		'0':tel,
		'1':email
	}
	random_key = random.choice(random_dict.keys())
	random_value = random_dict[random_key]
	return random_value


def UniversalTest_post(postData,url):
	postData = urllib.urlencode(postData) 
	request = urllib2.Request(
        url = url,
        data = postData,
        headers = headers
    )
	response = urllib2.urlopen(request) 
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1
	


log_way = random_email_or_phone()
random_name = StringUtil.token_generator()
phone = StringUtil.token_generator()
owner = StringUtil.token_generator()
tid = ''
active_code = ''
token = ''
did = StringUtil.token_generator()
cid = StringUtil.token_generator()
imei = StringUtil.token_generator()
title = StringUtil.token_generator()
content = StringUtil.token_generator()
msg_id = ''
policy_name = StringUtil.token_generator()
platform = random.choice(['ios','android'])
policy_content = {
			'policy_pwd':'123456',#密码策略
			'policy_locktime':'1',#锁屏时间
			'policy_device_limit':{
									'camera':'0',#相机0:关闭，1:开启
									'bluetooth':'0',#蓝牙0:关闭，1:开启
									'browser':'0',#浏览器0:关闭，1:开启
									'email':'0',#电子邮件0:关闭，1:开启
									'photo':'0',#图库0:关闭，1:开启
									'settings'：'0' #设置0:关闭，1:开启
								},#设备限制
			'policy_net_limit':{
								'emergency_calls':'0',#紧急电话0:关闭，1:开启
								'mseeage':'0',#短信0:关闭，1:开启
								'wifi':'0',#Wi-fi0:关闭，1:开启 
								},#网络限制
			'policy_wifi':{
							'wifi_name':'polysaas2',
							'wifi_pwd':'1q2w3e4r'
						} #wifi配置
		}
app_name = StringUtil.token_generator()
doc_name = StringUtil.token_generator()

#cookie
#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}

#登出
def test_LogoutHandler():
	request = urllib2.Request('http://localhost/user/logout')
	response = urllib2.urlopen(request) 
	# assert cj._cookies['tid']=='' and cj._cookies['timestamp']==''

#注册
def test_RegisterHandler():
	postData = {
		'email_or_phone':log_way,
		'user_name':random_name,
		'pwd':'111111'
	}
	postData = urllib.urlencode(postData) 
	request = urllib2.Request('http://localhost/user/register', postData)
	response = urllib2.urlopen(request) 
	text = response.read() 
	text = eval(text)
	print log_way
	assert text['status'] == 1



#登录
def test_LoginHandler():

	#print tel
	postData={
		'email_or_phone':log_way,
		'pwd':'111111'
	}
	url = 'http://localhost/user/login'
	UniversalTest_post(postData, url)
	#print "\n", cj._cookies
	

####################DeviceController###############

#添加设备
def test_Devices_AddHandler():
		
	postData={
		'phone':phone,
		'owner':owner
	}
	url = 'http://localhost/devices'
	UniversalTest_post(postData, url)

#设备列表
def test_Devices_ListHandler():

	request = urllib2.Request(
		url = 'http://localhost/devices',
		headers = headers
	)
	response = urllib2.urlopen(request)
	# request = urllib2.Request('http://localhost/devices')
	# response = urllib2.urlopen(request)

	text = response.read()
	#text = text.replace('false','"false"')
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
def test_Devices_EnrollHandler():
	
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
def test_Devices_InitialHandler():
	
	postData={
				'token':token,
				'phone':phone,
				'device_id':did,
				'client_id':cid,
				'imei':imei
			}
	url = 'http://localhost/android/initial'
	UniversalTest_post(postData, url)

#设备详情
def test_Devices_DetailHandler():
	request = urllib2.Request(
		url = ('http://localhost/devices/'+str(did)),
		headers = headers
	)
	response = urllib2.urlopen(request)
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1

#设备位置更新
def test_Loc_UpdateHandler():
	postData = {
				'token':token,
				'device_id':did
			}
	url = ('http://localhost/loc?device_id='+str(did))
	UniversalTest_post(postData, url)


#设备位置记录
def test_Loc_LatestHandler():
	request = urllib2.Request(
		url = ('http://localhost/loc?device_id='+str(did)),
		headers = headers
	)
	response = urllib2.urlopen(request)
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1

#删除设备
def test_Device_DeleteHandler():
	request = urllib2.Request(
		url = ('http://localhost/devices/'+str(did)),
		headers = headers
	)
	request.get_method = lambda:'DELETE'
	response = urllib2.urlopen(request)
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1




###################MsgController###################


#消息添加
def test_Msg_AddHandler():
	postData = {
		'title':title,
		'content':content
	}
	url = 'http://localhost/msgs'
	UniversalTest_post(postData, url)


#消息列表
def test_Msg_ListHandler():

	request = urllib2.Request(
		url = 'http://localhost/msgs',
		headers = headers
	)
	response = urllib2.urlopen(request)
	text = response.read()
	#text = text.replace('false','"false"')
	text = eval(text)
	print text

	#取msg_id
	global msg_id
	msg_id = text['data'][0]['msg_id']
	assert text['status'] == 1

#消息推送
def test_Msg_Push_SandHandler():
	postData = {
		'type':'msg',
		'id':msg_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/send?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)

#消息取消推送
def test_Msg_Push_CancelHandler():
	postData = {
		'type':'msg',
		'id':msg_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/cancel?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)


#消息删除
def test_Msg_DeleHandler():
	request = urllib2.Request(
		url = ('http://localhost/msgs/'+msg_id),
		headers = headers
	)
	request.get_method = lambda:'DELETE'
	response = urllib2.urlopen(request)
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1


#################PolicyController#################

#添加策略
def test_Policy_AddHandler():
	postData = {
		'policy_name' : policy_name,
		'platform' : platform
	}
	url = 'http://localhost/policies'
	UniversalTest_post(postData, url)


#策略列表
def test_Policy_ListHandler():
	
	request = urllib2.Request(
		url = 'http://localhost/policies',
		headers = headers
	)
	response = urllib2.urlopen(request)
	text = response.read()
	#text = text.replace('false','"false"')
	text = eval(text)
	print text

	global policy_id
	policy_id = text['data'][0]['policy_id']
	assert text['status'] == 1

#编辑策略
def test_Policy_EditHandler():
	postData = {
		'policy_content':policy_content
	}
	url = 'http://localhost/policies/'+str(policy_id)
	UniversalTest_post(postData, url)

#策略推送
def test_Policy_Push_SandHandler():
	postData = {
		'type':'policy',
		'id':policy_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/send?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)

#策略取消推送
def test_Policy_Push_CancelHandler():
	postData = {
		'type':'policy',
		'id':policy_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/cancel?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)

#策略删除
def test_Policy_DeleHandler():
	request = urllib2.Request(
		url = ('http://localhost/policies/'+policy_id),
		headers = headers
	)
	request.get_method = lambda:'DELETE'
	response = urllib2.urlopen(request)
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1

##############################AppController################################

#添加应用
def test_App_AddHandler():
	postData = {
		'app_name' : app_name,
	}
	url = 'http://localhost/apps'
	UniversalTest_post(postData, url)


#应用列表
def test_App_ListHandler():
	
	request = urllib2.Request(
		url = 'http://localhost/apps',
		headers = headers
	)
	response = urllib2.urlopen(request)
	text = response.read()
	#text = text.replace('false','"false"')
	text = eval(text)
	print text

	global app_id
	app_id = text['data'][0]['app_id']
	assert text['status'] == 1

#应用推送
def test_App_Push_SandHandler():
	postData = {
		'type':'app',
		'id':app_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/send?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)

#应用取消推送
def test_App_Push_CancelHandler():
	postData = {
		'type':'app',
		'id':app_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/cancel?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)

#应用删除
def test_App_DeleHandler():
	request = urllib2.Request(
		url = ('http://localhost/apps/'+app_id),
		headers = headers
	)
	request.get_method = lambda:'DELETE'
	response = urllib2.urlopen(request)
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1

#########################DocController######################

#添加文档
def test_Doc_AddHandler():
	postData = {
		'doc_name':doc_name,
	}
	url = 'http://localhost/docs'
	UniversalTest_post(postData, url)


#文档列表
def test_Doc_ListHandler():
	
	request = urllib2.Request(
		url = 'http://localhost/docs',
		headers = headers
	)
	response = urllib2.urlopen(request)
	text = response.read()
	#text = text.replace('false','"false"')
	text = eval(text)
	print text

	global doc_id
	doc_id = text['data'][0]['doc_id']
	assert text['status'] == 1

#文档推送
def test_Doc_Push_SandHandler():
	postData = {
		'type':'doc',
		'id':doc_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/send?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)

#文档取消推送
def test_Doc_Push_CancelHandler():
	postData = {
		'type':'doc',
		'id':doc_id,
		'device_list':device_id
	}
	url = 'http://localhost/push/cancel?type='+type+'&id='+id+''
	UniversalTest_post(postData, url)

#文档删除
def test_Doc_DeleHandler():
	request = urllib2.Request(
		url = ('http://localhost/docs/'+doc_id),
		headers = headers
	)
	request.get_method = lambda:'DELETE'
	response = urllib2.urlopen(request)
	text = response.read() 
	text=eval(text)
	assert text['status'] ==1

