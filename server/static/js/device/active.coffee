root = exports ? this
$('#device_active_list').dataTable {
	"aoColumns": [
		{ "sWidth": "10%", "sClass": "center", "bSortable": false }
		{ "sWidth": "8%",  "sClass": "center", "bSortable": false }
		{ "sWidth": "12%", "sClass": "center", "bSortable": false }
		{ "sWidth": "10%", "sClass": "center", "bSortable": false }
		{ "sWidth": "10%", "sClass": "center", "bSortable": false }
		{ "sWidth": "12%", "sClass": "center", "bSortable": false }
		{ "sWidth": "8%", "sClass": "center", "bSortable": false }
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
			"url": "#{sSource}?page_size=#{aoData[4].value}&page_start=#{aoData[3].value}"
			"dataType": "json"
			"success": (resp) ->
				result1 = {}
				result1['iTotalDisplayRecords'] = resp.total
				result1['iTotalRecords'] = resp.max
				data_list = []
				for d in resp.data
					tmp = []
					tmp.push d['uid']
					tmp.push d['owner']
					tmp.push d['tanent_id']
					tmp.push d['active_code']
					tmp.push d['time']
					tmp.push d['active']
					tmp.push """
						<button type='button' class='btn btn-xs btn-info' data-toggle='modal' data-target='#device-detail' onclick='show_detail("#{d['uid']}")'>more</button>
					"""
					data_list.push tmp
				result1['aaData'] = data_list
				console.log result1
				fnCallback result1
				return
		}
		return
}
@show_detail = (uid) ->
	$.ajax {
		"type":"get"
		"contentType":"application/json"
		"url":"/device/detail?uid=" + uid
		"success": (resp) ->
			root.uid = uid
			data = resp.data
			$('#loc_interval').html data['loc_interval']
			$('#loc_mode').html data['loc_mode']
			$('#did').html data['did']
			$('#cid').html data['cid']
			$('#imei').html data['imei']
	}

$ ->
	$('a[data-toggle="tab"]').on 'shown.bs.tab', (e)->
		if e.target.outerText is 'Location'
			$.ajax {
				"type": "get"
				"contentType":"application/json"
				"url":"/loc/latest?did=123"
				"success": (resp) ->
					console.log resp
					map = new BMap.Map("allmap")
					point = new BMap.Point(resp.long, resp.lat)
					map.centerAndZoom point, 15
					marker = new BMap.Marker(point)
					map.addOverlay marker 
					marker.setAnimation BMAP_ANIMATION_BOUNCE 
			}






