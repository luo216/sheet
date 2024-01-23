function toggle_chart(value) {
  tmpData = myData;
  tmpData.chart_type = chart_type_arr[value][0];
  update(tmpData);
}

for (var i = 0; i < chart_type_arr.length; i++) {
  addRadioButtonToDiv('chartType-switch-box', 'chartType', i, chart_type_arr[i][0], toggle_chart)
}
