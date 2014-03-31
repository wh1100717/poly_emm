root = exports ? this

@update_user = (uid)->
	$.ajax {
		"type":"get",
		"url":"/user/user_info?uid=" + uid,
		"success": (data) ->
			console.log data
	}

@device_add = ->
	$('#device-add-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('添加成功')
		$('#device-add').on 'hidden.bs.modal', -> show_page('device_list','设备')			
		$('#device-add').modal('hide')

@device_enroll = ->
	$('#device-enroll-form').ajaxSubmit (data) ->
		alert(data['status'])
		$('#device-enroll').on 'hidden.bs.modal', -> show_page('device_list','设备')			
		$('#device-enroll').modal('hide')

@device_initial = ->
	$('#device-initial-form').ajaxSubmit (data) ->
		alert(data['status'])
		$('#device-initial').on 'hidden.bs.modal', -> show_page('device_list','设备')			
		$('#device-initial').modal('hide')

@msg_push = ->
	$('#msg-push-form').ajaxSubmit (data) ->
		alert(data)


@show_detail = (did) ->
	root.did = did
	$('#msg_push_did').val(did)
	$.ajax {
		"type":"get"
		"contentType":"application/json"
		"url":"/device/detail?did=" + did
		"success": (resp) ->
			data = resp.data
			$('#loc_interval').html data['loc_interval']
			$('#loc_mode').html data['loc_mode']
			$('#did').html data['did']
			$('#cid').html data['cid']
			$('#imei').html data['imei']
	}

$ ->
	$('#device-list').dataTable {
		# "aoColumns": [
		# 	{ "bSortable": false },
		# 	null, null,null, null, null,
		# 	{ "bSortable": false }
		# ] ,
		"oLanguage": {
			"sLengthMenu": "每页显示 _MENU_ 条记录",
			"sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
			"sInfoEmpty": "&nbsp;",
			"sInfoFiltered": "(从 _MAX_ 条数据中检索)",
			"oPaginate": {
				"sFirst": "首页",
				"sPrevious": "前一页",
				"sNext": "后一页",
				"sLast": "尾页",
			},
			"sSearch": "搜索: ",
			"sZeroRecords": "没有检索到数据",
			"sProcessing": "<img src='./loading.gif' />"
		} 	
	}
	$.ajax {
		"type": "post",
		"url": "device/list",
		"success": (data) ->
			console.log data
			data_list = data['data']
			table_data = []
			for d in data_list
				tmp = []
				tmp.push d['owner']
				tmp.push d['phone']
				tmp.push d['time']
				if d.active is false
					tmp.push """
						<span class="btn btn-warning btn-xs tooltip-warning" data-rel="tooltip" data-placement="left" data-original-title="tid:#{d.tid}<br>激活码:#{d.active_code}<br>手机号:#{d.phone}" style="width: 64px;">未激活</span>
					"""
				else if d.did?
					tmp.push """
						<button type='button' class='btn btn-xs btn-success' data-toggle='modal' data-target='#device-detail' onclick='show_detail("#{d['did']}")'>设备详情</button>
					"""
				else
					tmp.push """
						<span class="btn btn-info btn-xs" style="width: 64px;">正在激活</span>
					"""
				table_data.push tmp
			$("#device-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			return
	}
	$('a[data-toggle="tab"]').on 'shown.bs.tab', (e)->
		if e.target.outerText is 'Location'
			$.ajax {
				"type": "get"
				"contentType":"application/json"
				"url":"/loc/latest?did=" + root.did
				"success": (resp) ->
					console.log resp
					map = new BMap.Map("allmap")
					point = new BMap.Point(resp.long, resp.lat)
					map.centerAndZoom point, 15
					marker = new BMap.Marker(point)
					map.addOverlay marker 
					marker.setAnimation BMAP_ANIMATION_BOUNCE 
			}
	$('a[data-toggle="tab"]').on 'shown.bs.tab', (e)->
		if e.target.outerText is 'App'
			$.ajax {
				"type": "get"
				"contentType":"application/json"
				"url":"/app/list?did="+ root.did
				"success": (resp) ->
					console.log resp
					app_list = resp['data']
					table_data = []
					for d in app_list
						tmp = []
						tmp.push d['appName']
						tmp.push d['appId']
						tmp.push d['version']
						table_data.push tmp
					$("#device_app_list").dataTable().fnAddData table_data
			}
	$('#device_app_list').dataTable {
		# "aoColumns": [
		# 	{ "sWidth": "30%", "sClass": "center", "bSortable": false }
		# 	{ "sWidth": "30%", "sClass": "center", "bSortable": false }
		# 	{ "sWidth": "40%", "sClass": "center", "bSortable": false }
		# ] ,
		"oLanguage": {
			"sLengthMenu": "每页显示 _MENU_ 条记录",
			"sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
			"sInfoEmpty": "&nbsp;",
			"sInfoFiltered": "(从 _MAX_ 条数据中检索)",
			"oPaginate": {
				"sFirst": "首页",
				"sPrevious": "前一页",
				"sNext": "后一页",
				"sLast": "尾页",
			},
			"sSearch": "搜索: ",
			"sZeroRecords": "没有检索到数据",
			"sProcessing": "<img src='./loading.gif' />"
		} 	
	}

