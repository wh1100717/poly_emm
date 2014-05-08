root = exports ? this
$ ->
	$('#app-list').dataTable {
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
		"url": "apps",
		"success": (data) ->
			console.log data
			data_list = data['data']
			table_data = []
			for d in data_list
				tmp = []
				tmp.push d['app_id']
				tmp.push d['app_name']
				tmp.push d['time']
				tmp.push """<button type='button' class='btn btn-xs btn-info' data-toggle='modal' data-target='#app-pull' onclick='app_pull("#{d['app_id']}")'>推送</button><button type='button' class='btn btn-xs btn-danger btn-confirm' data-toggle='modal' data-target='#app-delete' onclick='app_delete("#{d['app_id']}")'>删除</button>"""
				table_data.push tmp
			$("#app-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			$(".btn-confirm").confirm {
				text: "确认删除该应用？"
				title: "删除应用"
				confirm: (button) ->
					
					$('#app-delete').val(app_id)

					$.ajax {
						"type":"delete"
						"contentType":"application/json"
						"url":"/apps/"+app_id
						"success": (resp) ->
							if resp.status is 1
								alert('删除成功')
					}
					show_page('app_list','推送应用')	
				cancel: (button) ->
					alert 'no'
				confirmButton: "确定"
				cancelButton: "取消"
			}
			return
	}

@app_pull = ->
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

@app_upload = ->
	$('#app-upload-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('upload成功')
		$('#app-upload').on 'hidden.bs.modal', -> show_page('html_app','推送应用')			
		$('#app-upload').modal('hide')

@app_delete = (app_id) ->
	root.app_id = app_id

