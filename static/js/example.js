function chart_pie(data){
  var option = {
    series: [
      {
        type: 'pie',
        data: []
      }
    ]
  }
  for (var i = 0; i < data.length; i++) {
    option.series[0].data.push({
      name: data[i][0],
      value: data[i][1]
    })
  }
 
  return option
} 

function chart_bar(data) {
  var option = {
      xAxis: {
        type: 'category',
        data: []
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: [],
          type: 'bar'
        }
      ]
  }

  for (var i = 0; i < data.length; i++) {
    option.xAxis.data.push(data[i][0])
    option.series[0].data.push(data[i][1])
  }

  return option
}

function get_option(data) {
  if (data.chart_type=='pie'){
    return chart_pie(data.data)
  }
  if (data.chart_type=='bar'){
    return chart_bar(data.data)
  }

  return {}
}
