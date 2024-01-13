// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('chart'));

// 指定图表的配置项和数据
var option = {}
// 使用 fetch 函数获取数据
fetch('/data')
    .then(response => response.json())
    .then(data => {
        // 将获取的数据设置为 option 的数据
        option = data
        console.log(option);
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);

    })
    .catch(error => {
        console.error('Error:', error);
    });

    setTimeout(() => {
        fetch('/data1')
            .then(response => response.json())
            .then(data => {
                myChart.clear();
                // 将获取的数据设置为 option 的数据
                option = data;
                console.log(option);
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }, 3000);

