// Generated by CoffeeScript 1.7.1
$('#device_register_list').dataTable({
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
      "sLast": "尾页"
    },
    "sSearch": "搜索: ",
    "sZeroRecords": "没有检索到数据",
    "sProcessing": "<img src='./loading.gif' />"
  }
});

$.ajax({
  "type": "get",
  "url": "device/register/list",
  "success": function(data) {
    var d, data_list, table_data, tmp, _i, _len;
    console.log(data);
    data_list = data['data'];
    table_data = [];
    for (_i = 0, _len = data_list.length; _i < _len; _i++) {
      d = data_list[_i];
      tmp = [];
      tmp.push(d['tid']);
      tmp.push(d['active_code']);
      tmp.push(d['uid']);
      tmp.push(d['owner']);
      tmp.push(d['time']);
      tmp.push(d['active']);
      table_data.push(tmp);
    }
    return $("#device_register_list").dataTable().fnAddData(table_data);
  }
});

this.update_user = function(uid) {
  return $.ajax({
    "type": "get",
    "url": "/user/user_info?uid=" + uid,
    "success": function(data) {
      return console.log(data);
    }
  });
};

this.device_add = function() {
  return $('#device-add-form').ajaxSubmit(function(data) {
    alert(data);
    $('#device-add').on('hidden.bs.modal', function() {
      return show_page('device_register', '设备,注册列表');
    });
    return $('#device-add').modal('hide');
  });
};

this.device_enroll = function() {
  return $('#device-enroll-form').ajaxSubmit(function(data) {
    alert(data['status']);
    $('#device-enroll').on('hidden.bs.modal', function() {
      return show_page('device_register', '设备,注册列表');
    });
    return $('#device-enroll').modal('hide');
  });
};
