function chart_pie(data){
  var option = {
    tooltip: {},
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
        data: [],
        axisLabel: { interval: 0, rotate: 20 }
      },
      yAxis: {
        type: 'value'
      },
      tooltip: {},
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

// 创建一个二维数组存储图表类型和对应的函数
var chart_type_arr = [
  ['pie', chart_pie],
  ['bar', chart_bar]
]

function get_option(data) {
  for (var i = 0; i < chart_type_arr.length; i++) {
    if (chart_type_arr[i][0] == data.chart_type) {
      return chart_type_arr[i][1](data.data)
    }
  }

  return {}
}
