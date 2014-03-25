$('#device_register_list').dataTable {
	# "aoColumns": [
	# 	{ "bSortable": false },
	# 	null, null,null, null, null,
	# 	{ "bSortable": false }
	# ] ,
	"oLanguage": {
		"sLengthMenu": "每页显示 _MENU_ 条记录",
		"sZeroRecords": "抱歉， 没有找到",
		"sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
		"sInfoEmpty": "没有数据",
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
	"type": "get",
	"url": "device/register/list",
	"success": (data) ->
		console.log data
		data_list = data['data']
		table_data = []
		for d in data_list
			tmp = []
			tmp.push d['tanent_id']
			tmp.push d['active_code']
			tmp.push d['uid']
			tmp.push d['owner']
			tmp.push d['time']
			tmp.push d['active']
			table_data.push tmp
		$("#device_register_list").dataTable().fnAddData table_data
}

@update_user = (uid)->
	$.ajax {
		"type":"get",
		"url":"/user/user_info?uid=" + uid,
		"success": (data) ->
			console.log data
	}

@device_add = ->
	$('#device-add-form').ajaxSubmit (data) ->
		alert(data)
		$('#device-add').on 'hidden.bs.modal', -> show_page('device_register','设备,注册列表')			
		$('#device-add').modal('hide')

@device_enroll = ->
	$('#device-enroll-form').ajaxSubmit (data) ->
		alert(data['status'])
		$('#device-enroll').on 'hidden.bs.modal', -> show_page('device_register','设备,注册列表')			
		$('#device-enroll').modal('hide')
		# if data is 'success'
		# 	show_page 'device_register','设备,注册列表'


		