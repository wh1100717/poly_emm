#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
response:
	*	status: 1: 注册成功 | 0:注册失败
	*	desc: 
		*	`unaccept`		用户未勾选接受用户使用条款
		*	`diff_password`	用户输入密码和确认密码不符
		*	`wrong_type`	用户输入邮箱或账号格式不符
		*	`email_exist`	邮箱已被注册
		*	`phone_exist`	手机号已被注册
'''

class RESPONSE:
	#成功
	SUCCESS = {'status':1}
	LIST_SUCCESS = {'status':1, 'data':''}
	ENROLL_SUCCESS = {'status':1, 'token':''}
	INITIAL_SUCCESS = {'status':1, 'initial':''}
	PULL_SUCCESS = {'status':1, 'data':''}

	#失败
	FAIL = {'status':0}
	UN_ACCEPT = {'status':0, 'desc':'请接受使用条款'}
	DIFF_PASSWORD = {'status':0, 'desc':'您两次输入的密码不同'}
	WRONG_TYPE = {'status':0, 'desc':'请输入正确的手机号或邮箱'}
	INVALID_PASSWORD = {'status':0, 'desc':'密码无效'}

	#未授权
	UN_AUTHENTIFIC = {'status':0, 'desc':'没有该设备的控制权限'}
	WRONG_TID = {'status':0, 'desc':'错误的tid'}
	WRONG_DID = {'status':0, 'desc':'错误的did'}
	WRONG_TOKEN = {'status':0, 'desc':'错误的token'}
	WRONG_ACTIVE_CODE = {'status':0, 'desc':'错误的active_code'}
	WRONG_PHONE = {'status':0, 'desc':'错误的手机号'}

	#已存在
	EMAIL_EXIST = {'status':0, 'desc':'邮箱已被注册'}
	PHONE_EXIST = {'status':0, 'desc':'手机号已被注册'}
	DEVICE_EXIST = {'status':0, 'desc':'设备已存在'}
	ALREADY_ACTIVED = {'status':0, 'desc':'设备已激活'}



