poly_emm
========

##Requirements

```bash
pip install tornado
pip install Mako
pip install pyMongo
```
Note: pyMongo在windows下安装比较麻烦，详情请看[这里](http://api.mongodb.org/python/current/installation.html)

##Usage

执行`poly_emm/server/server.py`即可

项目结构如下：

```
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
```

*   handler.py:只有一个handlers数组，存放着在每个controller层定义的handler
*   handler: 一个元组，格式为(url, SpecificHandler)，用来记录url和SpecificHandler的映射关系
*   SpecificHandler：特定的Handler处理函数，用来针对具体的request请求进行请求解析以及对dao层返回的数据进行封装并返回response数据
*   Controller: 特定业务逻辑的SpecificHandlers的模块化集合，比如UserController中包含了处理url为`/user/*`的SpecificHandler，另外包含一个handlers数组，该数组最终会汇集到handlers.py中的handlers数组中，被tornado模块加载。
*   Dao: 特定数据逻辑的模块化集合，主要用来处理与数据库缓存方面的交互，被controller中的SpecificHandler调用。

