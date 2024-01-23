const index = 1; // 要发送的参数值
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('chart'));
var myData = {};
var tmpData = {};

function update(data) {
  var option = get_option(data);
  Object.assign(option,data.other)
  myChart.clear();
  myChart.setOption(option);
}

function draw_chart(index) {
  fetch(`/data/${index}`)
    .then(response => response.json())
    .then(data => {
      // 在这里处理返回的JSON数据
      myData = data;
      tmpData = data;
      update(tmpData);
      function test(value) {
        console.log(value);
      }
      removeAllChildElements('Check-Box')
      for (var i = 0; i < tmpData.data.length; i++) {
        addCheckBoxToDiv('Check-Box', 'dataRange', i, tmpData.data[i][0], test)
      }
    })
    .catch(error => {
      // 在这里处理请求错误
      console.error(error);
    });
}

function handleClick(index) {
  draw_chart(index);
}


draw_chart(0)
