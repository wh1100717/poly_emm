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
	SUCCESS = {'status':1}
	FAIL = {'status':0}
	UN_ACCEPT = {'status':0, 'desc':'请接受使用条款'}
	DIFF_PASSWORD = {'status':0, 'desc':'您两次输入的密码不同'}
	WRONG_TYPE = {'status':0, 'desc':'请输入正确的手机号或邮箱'}
	EMAIL_EXIST = {'status':0, 'desc':'邮箱已被注册'}
	PHONE_EXIST = {'status':0, 'desc':'手机号已被注册'}
	INVALID_PASSWORD = {'status':0, 'desc':'密码无效'}

