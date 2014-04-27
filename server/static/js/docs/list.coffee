root = exports ? this
$ ->
	$('#docs-list').dataTable {
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
			$("#docs-list").dataTable().fnAddData table_data
			$('[data-rel=tooltip]').tooltip({'html':true})
			$(".btn-confirm").confirm {
				text: "是否删除该doc"
				title: "删除doc"
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
					show_page('doc_list','推送消息')	
				cancel: (button) ->
					alert 'no'
				confirmButton: "确定"
				cancelButton: "取消"
			}
			return
	}
@docs_upload = ->
	$('#doc-upload-form').ajaxSubmit (data) ->
		if data.status is 1
			alert('upload成功')
		$('#docs-upload').on 'hidden.bs.modal', -> show_page('html_doc','推送doc')			
		$('#docs-upload').modal('hide')

@doc_delete = (doc_id) ->
	root.doc_id = doc_id

