root = exports ? this
$ ->
	$('#msg-list').dataTable {
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
		"type": "get",
		"url": "msgs",
		"success": (data) ->
			console.log data
			data_list = data['data']
			table_data = []
			for d in data_list
				tmp = []
				tmp.push d['msg_id']
				tmp.push d['title']
				tmp.push d['content']
				tmp.push d['time']
				tmp.push """<button type='button' class='btn btn-xs btn-info' data-toggle='modal' data-target='#msg-pull' onclick='msg_pull("#{d['msg_id']}")'>推送</button><button type='button' class='btn btn-xs btn-danger btn-confirm' data-toggle='modal' data-target='#msg-delete' onclick='msg_delete("#{d['msg_id']}")'>删除</button>"""
				table_data.push tmp
			$("#msg-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			$(".btn-confirm").confirm {
				text: "确认删除该消息？"
				title: "删除消息"
				confirm: (button) ->
					
					$('#msg-delete').val(msg_id)

					$.ajax {
						"type":"delete"
						"contentType":"application/json"
						"url":"/msgs/"+msg_id
						"success": (resp) ->
							if resp.status is 1
								alert('删除成功')
					}
					show_page('msg_list','推送消息')	
				cancel: (button) ->
					alert 'no'
				confirmButton: "确定"
				cancelButton: "取消"
			}
			return
	}


# $ ->
@msg_pull = (msg_id)->
	$('#push-list').dataTable {
		# "aoColumns": [
		# 	{ "bSortable": false },
		# 	null, null,null, null, null,
		# 	{ "bSortable": false }
		# ] ,
		"bRetrieve":true
		"bDestroy":true
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
	$("#push-list").dataTable().fnClearTable()
	$.ajax {
		"type": "get",
		"url": "push/devices",
		"success": (data) ->
			console.log data
			data_list = data['data']
			table_data = []
			for d in data_list
				tmp = []
				tmp.push '<input type="checkbox" name="check_list" value="'+d['did']+'">'
				tmp.push d['owner']
				tmp.push d['phone']
				table_data.push tmp
			$("#msg_id").val(msg_id)
			$("#push-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			return
	}
	

@msg_add = ->
	$('#msg-add-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('添加成功')
		$('#msg-add').on 'hidden.bs.modal', -> show_page('msg_list','推送消息')			
		$('#msg-add').modal('hide')

@msg_delete = (msg_id) ->
	root.msg_id = msg_id

@msg_push = ->
	$('#msg-push-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('推送成功')
		$('#push-list').on 'hidden.bl.modal', -> show_page('msg_list','推送消息')
		$('#push-list').modal('hide')