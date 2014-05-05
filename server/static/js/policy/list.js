// Generated by CoffeeScript 1.7.1
var root;

root = typeof exports !== "undefined" && exports !== null ? exports : this;

$(function() {
  $('#policy-list').dataTable({
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
    "url": "policies",
    "success": function(data) {
      var d, data_list, table_data, tmp, _i, _len;
      console.log(data);
      data_list = data['data'];
      table_data = [];
      for (_i = 0, _len = data_list.length; _i < _len; _i++) {
        d = data_list[_i];
        tmp = [];
        tmp.push(d['policy_id']);
        tmp.push(d['policy_name']);
        tmp.push(d['platform']);
        tmp.push(d['time']);
        tmp.push("<button type='button' class='btn btn-xs btn-success btn-confirm' data-toggle='modal' data-target='#policy-delete' onclick='policy_delete(\"" + d['policy_id'] + "\")'>删除</button><button type='button' class='btn btn-xs btn-success' data-toggle='modal' data-target='#policy-pull' onclick='policy_pull(\"" + d['policy_id'] + "\")'>推送</button><button type='button' class='btn btn-xs btn-success' data-toggle='modal' data-target='#policy-add' onclick='policy_edit(\"" + d['policy_id'] + "\")'>编辑</button>");
        table_data.push(tmp);
      }
      $("#policy-list").dataTable().fnAddData(table_data);
      $('[data-rel=tooltip]').tooltip({
        'html': true
      });
      $(".btn-confirm").confirm({
        text: "是否删除该策略",
        title: "删除策略",
        confirm: function(button) {
          $('#policy-delete').val(policy_id);
          $.ajax({
            "type": "delete",
            "contentType": "application/json",
            "url": "/policies/" + policy_id,
            "success": function(resp) {
              if (resp.status === 1) {
                return alert('删除成功');
              }
            }
          });
          return show_page('policy_list', '策略');
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

this.policy_pull = function() {
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

this.policy_add = function() {
  return $('#policy-add-form').ajaxSubmit(function(data) {
    if (data.status === 1) {
      alert('添加成功');
    }
    $('#policy-add').on('hidden.bs.modal', function() {
      return show_page('policy_list', '策略');
    });
    return $('#policy-add').modal('hide');
  });
};

this.policy_delete = function(policy_id) {
  return root.policy_id = policy_id;
};

this.policy_edit = function(policy_id) {
  return $.ajax({
    "type": "put",
    "url": "/policies/" + policy_id,
    "success": function(data) {
      var d;
      console.log(data);
      d = data['data'];
      document.getElementById("policy_name").value = d['policy_name'];
      document.getElementById("platform").value = d['platform'];
      document.getElementById("content").value = d['content'];
      document.getElementById("policy_id").value = d['policy_id'];
      $("#policy-add");
      $('[data-rel=tooltip]').tooltip({
        'html': true
      });
    }
  });
};

this.policy_modify = function() {
  return $('#policy-edit-form').ajaxSubmit(function(data) {
    if (data.status === 1) {
      alert('修改成功');
    }
    $('#policy-edit').on('hidden.bs.modal', function() {
      return show_page('policy_list', '策略');
    });
    return $('#policy-edit').modal('hide');
  });
};