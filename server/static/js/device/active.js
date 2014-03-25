// Generated by CoffeeScript 1.7.1
var root;

root = typeof exports !== "undefined" && exports !== null ? exports : this;

$('#device_active_list').dataTable({
  "aoColumns": [
    {
      "sWidth": "10%",
      "sClass": "center",
      "bSortable": false
    }, {
      "sWidth": "8%",
      "sClass": "center",
      "bSortable": false
    }, {
      "sWidth": "12%",
      "sClass": "center",
      "bSortable": false
    }, {
      "sWidth": "10%",
      "sClass": "center",
      "bSortable": false
    }, {
      "sWidth": "10%",
      "sClass": "center",
      "bSortable": false
    }, {
      "sWidth": "12%",
      "sClass": "center",
      "bSortable": false
    }, {
      "sWidth": "8%",
      "sClass": "center",
      "bSortable": false
    }
  ],
  "oLanguage": {
    "sLengthMenu": "每页显示 _MENU_ 条记录",
    "sZeroRecords": "抱歉， 没有找到",
    "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
    "sInfoFiltered": "(从 _MAX_ 条数据中检索)",
    "sInfoEmpty": "没有数据",
    "oPaginate": {
      "sFirst": "首页",
      "sPrevious": "前一页",
      "sNext": "后一页",
      "sLast": "尾页"
    },
    "sSearch": "搜索: ",
    "sZeroRecords": "没有检索到数据",
    "sProcessing": "<img src='./loading.gif' />"
  },
  "bSort": false,
  "bFilter": false,
  "bServerSide": true,
  "sAjaxSource": "/device/active/list",
  "fnServerData": function(sSource, aoData, fnCallback) {
    $.ajax({
      "type": "get",
      "contentType": "application/json",
      "url": "" + sSource + "?page_size=" + aoData[4].value + "&page_start=" + aoData[3].value,
      "dataType": "json",
      "success": function(resp) {
        var d, data_list, result1, tmp, _i, _len, _ref;
        result1 = {};
        result1['iTotalDisplayRecords'] = resp.total;
        result1['iTotalRecords'] = resp.max;
        data_list = [];
        _ref = resp.data;
        for (_i = 0, _len = _ref.length; _i < _len; _i++) {
          d = _ref[_i];
          tmp = [];
          tmp.push(d['uid']);
          tmp.push(d['owner']);
          tmp.push(d['tanent_id']);
          tmp.push(d['active_code']);
          tmp.push(d['time']);
          tmp.push(d['active']);
          tmp.push("<button type='button' class='btn btn-xs btn-info' data-toggle='modal' data-target='#device-detail' onclick='show_detail(\"" + d['uid'] + "\")'>more</button>");
          data_list.push(tmp);
        }
        result1['aaData'] = data_list;
        console.log(result1);
        fnCallback(result1);
      }
    });
  }
});

this.show_detail = function(uid) {
  return $.ajax({
    "type": "get",
    "contentType": "application/json",
    "url": "/device/detail?uid=" + uid,
    "success": function(resp) {
      var data;
      root.uid = uid;
      data = resp.data;
      $('#loc_interval').html(data['loc_interval']);
      $('#loc_mode').html(data['loc_mode']);
      $('#did').html(data['did']);
      $('#cid').html(data['cid']);
      return $('#imei').html(data['imei']);
    }
  });
};

$(function() {
  return $('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
    if (e.target.outerText === 'Location') {
      return $.ajax({
        "type": "get",
        "contentType": "application/json",
        "url": "/loc/latest?did=123",
        "success": function(resp) {
          var map, marker, point;
          console.log(resp);
          map = new BMap.Map("allmap");
          point = new BMap.Point(resp.long, resp.lat);
          map.centerAndZoom(point, 15);
          marker = new BMap.Marker(point);
          map.addOverlay(marker);
          return marker.setAnimation(BMAP_ANIMATION_BOUNCE);
        }
      });
    }
  });
});
