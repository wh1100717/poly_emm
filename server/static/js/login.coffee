login_submit = ->
	$('#login_form').ajaxSubmit (data) ->
		if data is 'success'
			location.href = "/"
		else
			alert(data)

register_submit = ->
	$('#register_form').ajaxSubmit (data) ->
		if data is 'success'
			alert('注册成功')
			window.location.href = "/user/login"
		else
			alert(data)
