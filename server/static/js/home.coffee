$ ->
	$.ajax {
		'type': 'get'
		'url' : '/device/statistics'
		'success': (data) ->
			data = eval(data)
			$('#last7_lost_controll_devices').html data.last7_lost_controll_devices
			$('#root_devices').html data.root_devices
			$('#last7_noncompliance_devices').html data.last7_noncompliance_devices
			$('#last7_new_devices').html data.last7_new_devices
			$('#china_unicom_devices').html data.china_unicom_devices
			$('#china_mobile_devices').html data.china_mobile_devices
			$('#china_telecom_devices').html data.china_telecom_devices
			$('#device_amount').html data.device_amount
			$('#user_amount').html data.user_amount
			$('#app_amount').html data.app_amount			
	}