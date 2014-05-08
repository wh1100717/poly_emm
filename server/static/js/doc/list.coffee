root = exports ? this
$ ->
	$('#doc-list').dataTable {
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
		"url": "docs",
		"success": (data) ->
			console.log data
			data_list = data['data']
			table_data = []
			for d in data_list
				tmp = []
				tmp.push d['doc_id']
				tmp.push d['doc_name']
				tmp.push d['time']
				tmp.push """<button type='button' class='btn btn-xs btn-success btn-confirm' data-toggle='modal' data-target='#doc-delete' onclick='doc_delete("#{d['doc_id']}")'>删除</button><button type='button' class='btn btn-xs btn-success' data-toggle='modal' data-target='#doc-pull' onclick='doc_pull("#{d['doc_id']}")'>推送</button>"""
				table_data.push tmp
			$("#doc-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			$(".btn-confirm").confirm {
				text: "确认删除该文档？"
				title: "删除文档"
				confirm: (button) ->
					
					$('#doc-delete').val(doc_id)

					$.ajax {
						"type":"delete"
						"contentType":"application/json"
						"url":"/docs/"+doc_id
						"success": (resp) ->
							if resp.status is 1
								alert('删除成功')
					}
					show_page('doc_list','文档列表')	
				cancel: (button) ->
					alert 'no'
				confirmButton: "确定"
				cancelButton: "取消"
			}
			return
	}

@doc_pull = ->
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

@doc_upload = ->
	$('#doc-upload-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('upload成功')
		$('#doc-upload').on 'hidden.bs.modal', -> show_page('html_doc','文档列表')			
		$('#doc-upload').modal('hide')

@doc_delete = (doc_id) ->
	root.doc_id = doc_id

