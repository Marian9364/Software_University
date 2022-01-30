function addItem() {
    let textEl = document.getElementById('newItemText');
    let valueEl = document.getElementById('newItemValue');
    let selectMenu = document.getElementById('menu');
    
    let option = document.createElement('option');
    option.textContent = textEl.value;
    option.value = valueEl.value;
    selectMenu.appendChild(option);

    textEl.value = '';
    valueEl.value = '';
    }
