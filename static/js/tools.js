function addRadioButtonToDiv(divId, name, value, label, clickFunc) {
  var div = document.getElementById(divId);

  var radio = document.createElement('input');
  radio.type = 'radio';
  radio.name = name;
  radio.value = value;
  radio.onclick = function() {
    clickFunc(value);
  };

  var radioLabel = document.createElement('label');
  radioLabel.appendChild(radio);
  radioLabel.appendChild(document.createTextNode(label));

  div.appendChild(radioLabel);
}
