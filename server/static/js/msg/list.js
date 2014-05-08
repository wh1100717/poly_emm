// Generated by CoffeeScript 1.7.1
var root;

root = typeof exports !== "undefined" && exports !== null ? exports : this;

$(function() {
  $('#msg-list').dataTable({
    "oLanguage": {
      "sLengthMenu": "每页显示 _MENU_ 条记录",
      "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
      "sInfoEmpty": "&nbsp;",
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
  return $.ajax({
    "type": "get",
    "url": "msgs",
    "success": function(data) {
      var d, data_list, table_data, tmp, _i, _len;
      console.log(data);
      data_list = data['data'];
      table_data = [];
      for (_i = 0, _len = data_list.length; _i < _len; _i++) {
        d = data_list[_i];
        tmp = [];
        tmp.push(d['msg_id']);
        tmp.push(d['title']);
        tmp.push(d['content']);
        tmp.push(d['time']);
        tmp.push("<button type='button' class='btn btn-xs btn-success btn-confirm' data-toggle='modal' data-target='#msg-delete' onclick='msg_delete(\"" + d['msg_id'] + "\")'>删除</button><button type='button' class='btn btn-xs btn-success' data-toggle='modal' data-target='#msg-pull' onclick='msg_pull(\"" + d['msg_id'] + "\")'>推送</button>");
        table_data.push(tmp);
      }
      $("#msg-list").dataTable().fnAddData(table_data);
      $('[data-rel=tooltip]').tooltip({
        'html': true
      });
      $(".btn-confirm").confirm({
        text: "确认删除该消息？",
        title: "删除消息",
        confirm: function(button) {
          $('#msg-delete').val(msg_id);
          $.ajax({
            "type": "delete",
            "contentType": "application/json",
            "url": "/msgs/" + msg_id,
            "success": function(resp) {
              if (resp.status === 1) {
                return alert('删除成功');
              }
            }
          });
          return show_page('msg_list', '推送消息');
        },
        cancel: function(button) {
          return alert('no');
        },
        confirmButton: "确定",
        cancelButton: "取消"
      });
    }
  });
});

this.msg_pull = function() {
  $('#device-list').dataTable({
    "bRetrieve": true,
    "bDestroy": true,
    "oLanguage": {
      "sLengthMenu": "每页显示 _MENU_ 条记录",
      "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
      "sInfoEmpty": "&nbsp;",
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
  $("#device-list").dataTable().fnClearTable();
  return $.ajax({
    "type": "get",
    "url": "devices",
    "success": function(data) {
      var d, data_list, table_data, tmp, _i, _len;
      console.log(data);
      data_list = data['data'];
      table_data = [];
      for (_i = 0, _len = data_list.length; _i < _len; _i++) {
        d = data_list[_i];
        tmp = [];
        tmp.push("<input type=\"checkbox\" name=\"chek_list\" value=\"1\">");
        tmp.push(d['owner']);
        tmp.push(d['phone']);
        table_data.push(tmp);
      }
      $("#device-list").dataTable().fnAddData(table_data);
      $('[data-rel=tooltip]').tooltip({
        'html': true
      });
    }
  });
};

this.msg_add = function() {
  return $('#msg-add-form').ajaxSubmit(function(data) {
    if (data.status === 1) {
      alert('添加成功');
    }
    $('#msg-add').on('hidden.bs.modal', function() {
      return show_page('msg_list', '推送消息');
    });
    return $('#msg-add').modal('hide');
  });
};

this.msg_delete = function(msg_id) {
  return root.msg_id = msg_id;
};
