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

function addCheckBoxToDiv(divId, name, value, label, clickFunc) {
  var div = document.getElementById(divId);

  var checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.name = name;
  checkbox.value = value;
  checkbox.checked = true;
  checkbox.onclick = function() {
    clickFunc(value);
  };

  var checkboxLabel = document.createElement('label');
  checkboxLabel.appendChild(checkbox);
  checkboxLabel.appendChild(document.createTextNode(label));

  div.appendChild(checkboxLabel);
}

function removeAllChildElements(parentId) {
  var parent = document.getElementById(parentId);
  if (parent) {
    parent.innerHTML = '';
  }
}
