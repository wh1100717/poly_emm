#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *

class ConfigHandler(BaseHandler):
	def get(self):
		user = self.get_user()
		#TODO 根据UserDao根据user获取相应的配置权限来返回配置信息，以下为假数据
		menulist = [
			{
				'id':'device_menu',
				'icon':'icon-laptop',
				'name':'设备',
				'submenu':[
					{'name':'注册列表','id':'device_register'},
					{'name':'激活设备','id':'device_active'},
					# {'name':'在线记录','id':'device_online'},
					# {'name':'设备组','id':'device_group'}
					]
			},
			# {
			# 	'id':'policy_menu',
			# 	'icon':'icon-key',
			# 	'name':'策略',
			# 	'submenu':[{'name':'策略列表','id':'policy'}]
			# },
			# {
			# 	'id':'app_menu',
			# 	'icon':'icon-list',
			# 	'name':'应用',
			# 	'submenu':[
			# 		{'name':'应用列表','id':'#'},
			# 		{'name':'黑名单管理','id':'#'},
			# 		{'name':'ios应用','id':'#'},
			# 		{'name':'ios应用策略','id':'#'},
			# 		{'name':'ios应用审计','id':'#'}
			# 		]
			# },
			# {
			# 	'id':'content_menu',
			# 	'icon':'icon-folder-open-alt',
			# 	'name':'内容',
			# 	'submenu':[
			# 		{'name':'文件推送','id':'#'},
			# 		{'name':'通讯录管理','id':'#'},
			# 		{'name':'推送消息','id':'#'},
			# 		{'name':'目录推送','id':'#'},
			# 		{'name':'文件加密新华','id':'#'}
			# 		]
			# },
			# {
			# 	'id':'user_menu',
			# 	'icon':'icon-user',
			# 	'name':'用户',
			# 	'submenu':[
			# 		{'name':'用户组管理','id':'#'},
			# 		{'name':'用户列表','id':'#'}
			# 		]
			# },
			# {'id':'setting_html','icon':'icon-cog','name':'设置','submenu':''},
			# {'id':'log_html','icon':'icon-file-alt','name':'日志','submenu':''},
			# {
			# 	'id':'user_menu',
			# 	'icon':'icon-picture',
			# 	'name':'报表',
			# 	'submenu':[{'name':'设备状况统计','id':'#'}]
			# },
			# {
			# 	'id':'my_menu',
			# 	'icon':'icon-desktop',
			# 	'name':'我的设备',
			# 	'submenu':[
			# 		{'name':'我的设备','id':'#'},
			# 		{'name':'手机备份','id':'#'}
			# 		]
			# }
		]
		self.write(
			{
				"back_image":"static/image/logo.png",
				"back_title":"企业移动管理平台",
				"back_username":"郑罡",
				"back_userrole":"用户管理员",
				"back_menulist":menulist
			})

class StatusCheckHandler(BaseHandler):
	def get(self):
		user = self.get_user()
		#TODO 根据UserDao根据user获取相应的配置权限来返回配置信息，以下为假数据
		data = {
			'task': [
				{'name':'Software Update','percent':65,'url':'#'},
				{'name':'Hardware Upgrade','percent':35,'url':'#'},
				{'name':'Unit Testing','percent':15,'url':'#'},
				{'name':'Bug Fixed','percent':90,'url':'#'},
			]
		}
		self.write(data)

handlers = [
	(r"/base/config", ConfigHandler),
	(r"/base/status_check", StatusCheckHandler),
]
