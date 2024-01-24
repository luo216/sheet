function toggle_chart(value) {
  myData.chart_type = chart_type_arr[value][0];
  tmpData = {};
  Object.assign(tmpData, myData);
  tmpData.data = [];
  for (var i = 0; i < datarangestatus.length; i++) {
    if (datarangestatus[i]) {
      tmpData.data.push(myData.data[i])
    }
  }
  update(tmpData);
}

for (var i = 0; i < chart_type_arr.length; i++) {
  addRadioButtonToDiv('chartType-switch-box', 'chartType', i, chart_type_arr[i][0], toggle_chart)
}
