root = exports ? this
$ ->
	$('#policy-list').dataTable {
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
		"url": "policies",
		"success": (data) ->
			console.log data
			data_list = data['data']
			table_data = []
			for d in data_list
				tmp = []
				tmp.push d['policy_id']
				tmp.push d['policy_name']
				tmp.push d['platform']
				tmp.push d['time']
				tmp.push """<button type='button' class='btn btn-xs btn-success' data-toggle='modal' data-target='#policy-add' onclick='policy_edit("#{d['policy_id']}")'>编辑</button><button type='button' class='btn btn-xs btn-info' data-toggle='modal' data-target='#policy-pull' onclick='policy_pull("#{d['policy_id']}")'>推送</button><button type='button' class='btn btn-xs btn-danger btn-confirm' data-toggle='modal' data-target='#policy-delete' onclick='policy_delete("#{d['policy_id']}")'>删除</button>"""
				table_data.push tmp
			$("#policy-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			$(".btn-confirm").confirm {
				text: "确认删除该策略？"
				title: "删除策略"
				confirm: (button) ->
					
					$('#policy-delete').val(policy_id)

					$.ajax {
						"type":"delete"
						"contentType":"application/json"
						"url":"/policies/"+policy_id
						"success": (resp) ->
							if resp.status is 1
								alert('删除成功')
					}
					show_page('policy_list','策略')	
				cancel: (button) ->
					alert 'no'
				confirmButton: "确定"
				cancelButton: "取消"
			}
			return
	}


# $ ->
@policy_pull = ->
	$('#device-list').dataTable {
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
	$("#device-list").dataTable().fnClearTable()
	$.ajax {
		"type": "get",
		"url": "devices",
		"success": (data) ->
			console.log data
			data_list = data['data']
			table_data = []
			for d in data_list
				tmp = []
				tmp.push """
					<input type="checkbox" name="chek_list" value="1">
				"""
				tmp.push d['owner']
				tmp.push d['phone']
				table_data.push tmp
			$("#device-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			return
	}


@policy_add = ->
	
	$('#policy-add-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('添加成功')
		
		$('#policy-add').on 'hidden.bs.modal', -> show_page('policy_list','策略')			
		$('#policy-add').modal('hide')

@policy_delete = (policy_id) ->
	root.policy_id = policy_id

@policy_edit = (policy_id)->
	# alert(policy_id)
	$.ajax {
		"type": "put",
		"url": "/policies/"+policy_id,
		"success": (data) ->
			console.log data
			d = data['data']
			document.getElementById("policy_name").value = d['policy_name']
			document.getElementById("platform").value = d['platform']
			document.getElementById("content").value = d['content']
			# $('#policy_name').html data['policy_name']
			# $('#platform').html data['platform']
			# $('#content').html data['content']

			document.getElementById("policy_id").value = d['policy_id']
			# alert(data_list)
			# table_data = []
			
			# tmp = []
			# tmp.push d['policy_name']
			# tmp.push d['platform']
			# tmp.push d['content']
			# table_data.push tmp
			$("#policy-add")
			$('[data-rel=tooltip]').tooltip({'html':true})
			return
	}

@policy_modify = ->
	$('#policy-edit-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('修改成功')
		$('#policy-edit').on 'hidden.bs.modal', -> show_page('policy_list','策略')			
		$('#policy-edit').modal('hide')



	# $('#policy-edit-form').ajaxSubmit (data) ->
	# 	if data.status is 1
	# 		alert('修改成功')
	# 	$('#policy-edit').on 'hidden.bs.modal', -> show_page('policy_list','策略')			
	# 	$('#policy-edit').modal('hide')

