$('#device_register_list').dataTable {
	"aoColumns": [
		{ "bSortable": false },
		null, null,null, null, null,
		{ "bSortable": false }
	] ,
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
			tmp.push "<a href='' class='orange' data-toggle='modal' data-target='#update_user_modal' onclick='update_user(#{d['id']})'>#{d['username']}</a>"
			tmp.push d['loginName']
			tmp.push d['passcode']
			tmp.push d['snNumber']
			dd = new Date d['registionTime']
			tmp.push [dd.getFullYear(), dd.getMonth()+1, dd.getDate()].join('-')+ ' ' + [dd.getHours(), dd.getMinutes(), dd.getSeconds()].join(':')
			if d['enrollment_status'] is '1'
				tmp.push '<span class="label label-sm label-warning">已激活</span>'
			else
				tmp.push '<span class="label label-sm label-success">未激活</span>'
			tmp.push """
					<td>
						<div class="visible-md visible-lg hidden-sm hidden-xs action-buttons">
							<a class="blue" href="#">
								<i class="icon-zoom-in bigger-130"></i>
							</a>

							<a class="green" href="#">
								<i class="icon-pencil bigger-130"></i>
							</a>

							<a class="red" href="#">
								<i class="icon-trash bigger-130"></i>
							</a>
						</div>

						<div class="visible-xs visible-sm hidden-md hidden-lg">
							<div class="inline position-relative">
								<button class="btn btn-minier btn-yellow dropdown-toggle" data-toggle="dropdown">
									<i class="icon-caret-down icon-only bigger-120"></i>
								</button>

								<ul class="dropdown-menu dropdown-only-icon dropdown-yellow pull-right dropdown-caret dropdown-close">
									<li>
										<a href="#" class="tooltip-info" data-rel="tooltip" title="View">
											<span class="blue">
												<i class="icon-zoom-in bigger-120"></i>
											</span>
										</a>
									</li>

									<li>
										<a href="#" class="tooltip-success" data-rel="tooltip" title="Edit">
											<span class="green">
												<i class="icon-edit bigger-120"></i>
											</span>
										</a>
									</li>

									<li>
										<a href="#" class="tooltip-error" data-rel="tooltip" title="Delete">
											<span class="red">
												<i class="icon-trash bigger-120"></i>
											</span>
										</a>
									</li>
								</ul>
							</div>
						</div>
					</td>
				"""
			tmp.push "123"
			table_data.push tmp
		console.log table_data
		$("#device_register_list").dataTable().fnAddData table_data
}

@update_user = (uid)->
	$.ajax {
		"type":"get",
		"url":"/user/user_info?uid=" + uid,
		"success": (data) ->
			console.log data
	}
