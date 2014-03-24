#POLY_EMM（windows版）
##1、安装Python
*	下载并安装[Python]
*	安装后在系统环境变量PATH中[配置Python相关的环境变量]
*	`$ python -V`查看是否安装并配置成功（注意：是大写的-V）

##2、SetupTools安装

*	下载脚本[ez_setup.py]至本地，例如D盘根目录
*	终端执行`$ python d:/ez_setup.py`进行SetupTools的安装
*	在运行的时候会发生一个错误，该错误为"ascii codec can't decode byte 0xe8 in position 0:ordinal not in range(128)",大意为ascii编码不能解析byte 0xe8。解决方法：找到并打开python根目录/Lib/mimetypes.py文件，在`import urllib`后，添加代码:

	```python
	reload(sys)
	sys.setdefaultencoding('gbk')
	```

*	把默认编码方式改为gbk（网上有写用utf8的，在这个脚本中是无效的，需要改成gbk格式）。重新执行`$ python d:/ez_setup.py`，如果出现刷屏的安装信息，则说明安装成功了。此时，在python目录下多了一个Script文件夹，easy\_install就在里面。

##3、Pip安装
*	接下来进入easy\_install所在的文件夹，即Python根目录\Scripts执行以下命令进行pip安装：

	```
	C:\Python27\Scripts> easy_install.exe pip
	```
*	执行`$ pip -V`来查看pip是否安装成功以及相应的安装版本

	

##4、环境变量设置和检查
*       检查PATH中是否添加了`C:\Python27;`，如果没有则添加上。
*       检查PATH中是否添加了`C:\Python27\Scripts;`，如果没有则添加上。
*       检查PATHEXT中是否添加了`.EXE;`，如果没有则添加上。
*       检查PATHEXT中是否添加了`.PY;`，如果没有则添加上。
*       检查PATHEXT中是否添加了`.PYM`，如果没有则添加上。
##5、依赖包安装
###PyMongo安装
*	`$ easy_install pymongo`
*	`$ easy_install -U pymongo`
###Tornado安装
*	`$ pip install tornado`
###Mako安装
*	`pip install Mako`
###nose安装
*	`easy_install nose`
##6、启动项目
###配置settings.py
	__mongo_config__ = {
		'host': '10.0.1.202',#配置mongodb的host
		'port': 27017,#配置mongodb的port
		'db': 'emm',#配置mongo使用的数据库
	}
###启动项目
*	执行`poly_emm/server/server.py`即可
##7、项目结构


	
	├─backend_tests     #server端测试模块
	├─controller        #controller模块
	├─dao               #dao模块
	├─static            #静态文件
	│  ├─assets         #ACE自带的资源文件
	│  ├─highstock      #highstock插件
	│  ├─image          #图片存放在这里
	│  ├─css            #CSS文件存放在这里
	│  └─js             #js文件存放在这里
	├─templates         模版
	├─base.py           这里封装了handler请求，进行权限验证，错误页面跳转等操作
	├─handler.py        配置handler路由，详细请求处理，根据不同的业务逻辑封装在不同的controller中
	├─server.py         起始文件，执行`python server.py`来运行该项目
	└─setting.py        配置文件，配置了路径信息、服务器配置、模版信息、数据库信息等
	

*   handler.py:只有一个handlers数组，存放着在每个controller层定义的handler
*   handler: 一个元组，格式为(url, SpecificHandler)，用来记录url和SpecificHandler的映射关系
*   SpecificHandler：特定的Handler处理函数，用来针对具体的request请求进行请求解析以及对dao层返回的数据进行封装并返回response数据
*   Controller: 特定业务逻辑的SpecificHandlers的模块化集合，比如UserController中包含了处理url为`/user/*`的SpecificHandler，另外包含一个handlers数组，该数组最终会汇集到handlers.py中的handlers数组中，被tornado模块加载。
*   Dao: 特定数据逻辑的模块化集合，主要用来处理与数据库缓存方面的交互，被controller中的SpecificHandler调用。


[Python]:http://www.python.org/
[配置Python相关的环境变量]:http://blog.csdn.net/liguo9860/article/details/6829610
[ez_setup.py]:https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py