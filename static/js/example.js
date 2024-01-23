function chart_pie(data){
  var option = {
    series: [
      {
        type: 'pie',
        data: []
      }
    ]
  }
  for (var i = 0; i < data.data.length; i++) {
    option.series[0].data.push({
      name: data.data[i][0],
      value: data.data[i][1]
    })
  }
 
  return option
} 

function get_option(data) {
  if (data.chart_type=='pie'){
    return chart_pie(data)
  }

  return {}
}
