// Generated by CoffeeScript 1.7.1

/*
base.js: 全局js，用来做一些页面初始化的配置工作
Date: 2013/03/03
Author: EricWang
 */
this.show_page = function(page, name) {
  var page_url;
  page_url = page.replace(/_/g, '/');
  $.ajax({
    'type': 'get',
    'url': '/' + page_url,
    'success': function(data) {
      var n, _i, _len;
      $("#sidebar_list li").removeClass("active");
      $("#" + page).addClass("active");
      $("#main").html(data);
      name = name.split(',');
      console.log(name);
      $('.breadcrumb').html("<li>\n	<i class=\"icon-home home-icon\"></i>\n	<a href=\"javascript:void(0)\" onclick=\"show_page('home', '首页')\">首页</a>\n</li>\n");
      if (name[0] !== '首页') {
        for (_i = 0, _len = name.length; _i < _len; _i++) {
          n = name[_i];
          $('.breadcrumb').append("<li><a href=\"javascript:void(0)\">" + n + "</a></li>");
        }
      }
    },
    'error': function(data) {
      return $("#main").html(data.responseText);
    }
  });
};

$(function() {
  $.ajax({
    'type': 'get',
    'url': '/base/config',
    'success': function(data) {
      var menu, menu_html, menulist, sub_m, submenu, _i, _j, _len, _len1;
      data = eval(data);
      $('#back_image').attr('src', data['back_image']);
      $("#back_title").html(data['back_title']);
      $("#back_username").html(data['back_username']);
      $("#back_userrole").html(data['back_userrole']);
      menulist = data['back_menulist'];
      menu_html = "";
      for (_i = 0, _len = menulist.length; _i < _len; _i++) {
        menu = menulist[_i];
        submenu = menu['submenu'];
        if (submenu === "" || submenu === void 0) {
          menu_html += "<li id=\"" + menu['id'] + "\">\n	<a href = \"javascript:void(0)\" onclick=\"show_page('" + menu['id'] + "','" + menu['name'] + "')\">\n		<i class=\"" + menu['icon'] + "\"></i>\n		<span class=\"menu-text\"> " + menu['name'] + " </span>\n	</a>\n</li>";
        } else {
          menu_html += "<li id=\"" + menu['id'] + "\">\n	<a href=\"javascript:void(0)\" class=\"dropdown-toggle\">\n		<i class=\"" + menu['icon'] + "\"></i>\n		<span class=\"menu-text\"> " + menu['name'] + " </span>\n                                <b class=\"arrow icon-angle-down\"></b>\n	</a>\n	<ul class=\"submenu\">";
          for (_j = 0, _len1 = submenu.length; _j < _len1; _j++) {
            sub_m = submenu[_j];
            menu_html += "<li>\n	<a href=\"javascript:void(0)\" onclick=\"show_page('" + sub_m['id'] + "','" + menu['name'] + "," + sub_m['name'] + "')\">\n		<i class=\"icon-double-angle-right\"></i>\n		" + sub_m['name'] + "\n	</a>\n</li>";
          }
          menu_html += '</ul></li>';
        }
      }
      $('#sidebar_list').append(menu_html);
    }
  });
  $.ajax({
    'type': 'get',
    'url': '/base/status_check',
    'success': function(data) {
      var task, task_html, tasks, warn_info, _i, _len;
      data = eval(data);

      /*
      			 *处理task
       */
      console.log("处理task");
      tasks = data.task;
      task_html = "<li class=\"dropdown-header\">\n	<i class=\"icon-ok\"></i>\n	" + tasks.length + " Tasks to complete\n</li>				";
      for (_i = 0, _len = tasks.length; _i < _len; _i++) {
        task = tasks[_i];
        warn_info = '';
        if (task.percent > 80) {
          warn_info = 'progress-bar-success';
        } else if (task.percent > 60) {
          warn_info = 'progress-bar-info';
        } else if (task.percent > 40) {
          warn_info = 'progress-bar-warning';
        } else {
          warn_info = 'progress-bar-danger';
        }
        task_html += "<li>\n	<a href=\"" + task.url + "\">\n		<div class=\"clearfix\">\n			<span class=\"pull-left\">" + task.name + "</span>\n			<span class=\"pull-right\">" + task.percent + "%</span>\n		</div>\n\n		<div class=\"progress progress-mini \">\n			<div style=\"width:" + task.percent + "%\" class=\"progress-bar " + warn_info + "\"></div>\n		</div>\n	</a>\n</li>				";
      }
      $('#task_list').html(task_html);

      /*
      			 *处理notification
       */
      console.log("处理Notification");

      /*
      			 *处理Message
       */
      return console.log("处理Message");
    }
  });
  show_page('home', '首页');
});
