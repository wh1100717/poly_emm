$ ->
	seriesOptions = []
	$.getJSON '/device/register_history', (data) ->
		xiaomi_crawled_data = []
		xiaomi_new_data = []
		$.each data, (date, item) ->
			date = date.split('-')
			date = Date.UTC(parseInt(date[0]), parseInt(date[1])-1, parseInt(date[2]))
			item = eval('(' + item + ')')
			console.log item
			xiaomi_crawled_data.push [date, parseInt item.crawled] if item.crawled
			xiaomi_new_data.push [date, parseInt item.new] if item.new
			console.log  xiaomi_crawled_data
			console.log  xiaomi_new_data
			return
		seriesOptions[0] = {name: 'xiaomi_crawled_data', data: xiaomi_crawled_data.sort (x,y) -> x[0]-y[0]}
		seriesOptions[1] = {name: 'xiaomi_new_data', data: xiaomi_new_data.sort (x,y) -> x[0]-y[0]}
		$('#container-status-list').highcharts 'StockChart',{
			chart: {},
			rangeSelector: {selected:1},
			title: {text:'爬虫数据分析'},
			legend: {enabled:true},
			tooltip:{
				pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b><br/>',
				valueDecimals: 2
			}
			series: seriesOptions
		}
		status_list_chart = $('#container-status-list').highcharts()
		# status_list_chart.series[1].hide() #可以默认隐藏
		return
	return
