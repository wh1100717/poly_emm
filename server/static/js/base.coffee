###
base.js: 全局js，用来做一些页面初始化的配置工作
Date: 2013/03/03
Author: EricWang
###


#定义show_page()函数,该函数用来加载主页面信息
@show_page = (page, name) ->
	page_url = page.replace(/_/g,'/')
	$.ajax {
		'type': 'get',
		'url': '/' + page_url,
		'success': (data) ->
			$("#sidebar_list li").removeClass "active"
			$("##{page}").addClass "active"
			$("#main").html data
			name = name.split(',')
			console.log name
			$('.breadcrumb').html """
				<li>
					<i class="icon-home home-icon"></i>
					<a href="javascript:void(0)" onclick="show_page('home', '首页')">首页</a>
				</li>

			"""
			if name[0] isnt '首页'
				for n in name
					$('.breadcrumb').append """<li><a href="javascript:void(0)">#{n}</a></li>"""
			return
	}
	return

#页面加载成功以后执行的业务逻辑
$ ->
	#首页配置项
	#*	back_title:	左上角显示的后台名称
	#*	back_username: 当前登录用户的用户名
	#*	back_userrole: 当前登录用户的角色
	#*	back_menulist: 当前登录用户所拥有权限的模块
	$.ajax {
		'type': 'get',
		'url': '/base/config',
		'success': (data) ->
			data = eval(data)
			$('#back_image').attr 'src', data['back_image']
			$("#back_title").html data['back_title']
			$("#back_username").html data['back_username']
			$("#back_userrole").html data['back_userrole']
			menulist = data['back_menulist']
			menu_html = ""
			for menu in menulist
				submenu = menu['submenu']
				if submenu is ""
					menu_html += """
						<li id="#{menu['id']}">
							<a href = "javascript:void(0)" onclick="show_page('#{menu['id']}','#{menu['name']}')">
								<i class="#{menu['icon']}"></i>
								<span class="menu-text"> #{menu['name']} </span>
							</a>
						</li>
					"""
				else
					menu_html += """
						<li id="#{menu['id']}">
							<a href="javascript:void(0)" class="dropdown-toggle">
								<i class="#{menu['icon']}"></i>
								<span class="menu-text"> #{menu['name']} </span>
                                <b class="arrow icon-angle-down"></b>
							</a>
							<ul class="submenu">
					"""
					for sub_m in submenu
						menu_html += """
							<li>
								<a href="javascript:void(0)" onclick="show_page('#{sub_m['id']}','#{menu['name']},#{sub_m['name']}')">
									<i class="icon-double-angle-right"></i>
									#{sub_m['name']}
								</a>
							</li>
						"""
					menu_html += '</ul></li>'


			$('#sidebar_list').append menu_html
			return
	}
	$.ajax {
		'type': 'get'
		'url': '/base/status_check'
		'success': (data) ->
			data = eval(data)
			###
			#处理task
			###
			console.log "处理task"
			tasks = data.task
			task_html = """
				<li class="dropdown-header">
					<i class="icon-ok"></i>
					#{tasks.length} Tasks to complete
				</li>				
			"""
			for task in tasks
				warn_info = ''
				if task.percent > 80
					warn_info = 'progress-bar-success'
				else if task.percent > 60
					warn_info = 'progress-bar-info'
				else if task.percent > 40
					warn_info = 'progress-bar-warning'
				else
					warn_info = 'progress-bar-danger'
				task_html += """
					<li>
						<a href="#{task.url}">
							<div class="clearfix">
								<span class="pull-left">#{task.name}</span>
								<span class="pull-right">#{task.percent}%</span>
							</div>

							<div class="progress progress-mini ">
								<div style="width:#{task.percent}%" class="progress-bar #{warn_info}"></div>
							</div>
						</a>
					</li>				
				"""
			$('#task_list').html task_html
			###
			#处理notification
			###
			console.log "处理Notification"

			###
			#处理Message
			###
			console.log "处理Message"



	}
	#默认加载dashboard页面
	show_page('home','首页')
	return

