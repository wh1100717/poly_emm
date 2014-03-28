login_submit = ->
	$('#login_form').ajaxSubmit (data) ->
		if data.status is 1
			window.location.href = "/"
		else
			alert(data.desc)

register_submit = ->
	$('#register_form').ajaxSubmit (data) ->
		if data.status is 1
			alert('注册成功')
			window.location.href = "/user/login"
		else
			alert(data.desc)
