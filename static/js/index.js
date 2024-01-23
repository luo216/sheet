const index = 1; // 要发送的参数值
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('chart'));
var option = {}

function draw_chart(index) {
  fetch(`/data/${index}`)
    .then(response => response.json())
    .then(data => {
      // 在这里处理返回的JSON数据
      console.log(data);
      myChart.clear();
      myChart.setOption(option);
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
