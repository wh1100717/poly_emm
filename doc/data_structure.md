```python
emm.user={
	'tid':1,
	'user_name':'zq',
	'pwd':'md5('1234')',
	'role':'admin',
	'active':True,
	'token':'135tset24w3452y',
	'email':'zq@qq.com',
	'phone':'13333333333',
	'devices':[
			{
			'phone':'1388888888',
			'active_code':'3er2w4',
			'active':False,
			'owner':'张三',
			'time':'2014-3-31 11:50:21',
			'did':'1212121',
			'imei':'eq2312321123',
			'cid':'3141231'
			'apps':[
					{
					'appName':'QQ',
					'appId':'1',
					'version':'5.0'
					},
					{
					'appName':'wechat',
					'appId':'2',
					'version':'4.3'
					},
				],
			'loc_info':[
					{
					'long':116.404,
					'lat':39.915
					},
					{
					'long':16.44,
					'lat':3.95
					},
				],
			'pull_data':[
				'policy':{
					'policy_id':'2',
					'policy_name':'默认策略',
					...
					},
				'msg':[
					{
						'msg_id':'1',
						'msg_info':'Hello world!'
					},
					{
						'msg_id':'2',
						'msg_info':'How old are you?'
					}
					]
				]
			},
			{
			'phone':'1386666666',
			'active_code':'r4ww3q',
			'active':True,
			'owner':'李四',
			'time':'2014-3-31 13:00:21',
			'did':'124213',
			'imei':'wr242321123',
			'cid':'32145231'
			'apps':[
					{
					'appName':'QQ',
					'appId':'1',
					'version':'5.0'
					},
					{
					'appName':'Evernote',
					'appId':'2',
					'version':'1.0'
					},
				],
			'loc_info':[
					{
					'long':116.404,
					'lat':39.915
					},
					{
					'long':16.44,
					'lat':3.95
					},
				],
			'pull_data':[
				'policy':{
					'policy_id':'2',
					'policy_name':'默认策略',
					...
					},
				'msg':[
					{
						'msg_id':'1',
						'msg_info':'Hello world!'
					},
					{
						'msg_id':'2',
						'msg_info':'How old are you?'
					}
					],
				...
				]
			},
			...
		]

}
```