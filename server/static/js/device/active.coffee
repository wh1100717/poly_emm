$('#device_active_list').dataTable {
	"aoColumns": [
		{ "sWidth": "10%", "sClass": "center", "bSortable": false }
		{ "sWidth": "8%",  "sClass": "center", "bSortable": false }
		{ "sWidth": "12%", "sClass": "center", "bSortable": false }
		{ "sWidth": "10%", "sClass": "center", "bSortable": false }
		{ "sWidth": "10%", "sClass": "center", "bSortable": false }
		{ "sWidth": "12%", "sClass": "center", "bSortable": false }
		{ "sWidth": "12%", "sClass": "center", "bSortable": false }
		{ "sWidth": "15%", "sClass": "center", "bSortable": false }
	]
	"oLanguage": {
		"sLengthMenu": "每页显示 _MENU_ 条记录"
		"sZeroRecords": "抱歉， 没有找到"
		"sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据"
		"sInfoFiltered": "(从 _MAX_ 条数据中检索)"
		"sInfoEmpty": "没有数据"
		"oPaginate": {
			"sFirst": "首页"
			"sPrevious": "前一页"
			"sNext": "后一页"
			"sLast": "尾页"
		},
		"sSearch": "搜索: "
		"sZeroRecords": "没有检索到数据"
		"sProcessing": "<img src='./loading.gif' />"
	},
	"bSort": false
	"bFilter": false
	"bServerSide": true
	"sAjaxSource": "/device/active/list"
	"fnServerData": (sSource, aoData, fnCallback) ->
		$.ajax {
			"type": "get"
			"contentType": "application/json"
			"url": "#{sSource}?page_size=#{aoData[4].value}&page_index=#{aoData[3].value/aoData[4].value}"
			"dataType": "json"
			"success": (resp) ->
				result1 = {}
				result1['iTotalDisplayRecords'] = resp.total
				result1['iTotalRecords'] = resp.max
				data_list = []
				for t in resp.data
					data = []
					data.push t.device_name
					data.push t.owner_name
					data.push t.sn_number
					data.push t.device_type
					data.push t.platform
					d = new Date(t.registion_time)
					data.push [d.getFullYear(), d.getMonth()+1, d.getDate()].join('-')+ ' ' + [d.getHours(), d.getMinutes(), d.getSeconds()].join(':')
					d = new Date(t.last_update_time)
					data.push [d.getFullYear(), d.getMonth()+1, d.getDate()].join('-')+ ' ' + [d.getHours(), d.getMinutes(), d.getSeconds()].join(':')
					data.push """
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
					data_list.push data
				result1['aaData'] = data_list
				console.log result1
				fnCallback result1
				return
		}
		return
}
