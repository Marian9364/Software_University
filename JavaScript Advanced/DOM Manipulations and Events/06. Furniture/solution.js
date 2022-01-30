function solve() {
  let [inputArea, outputArea] = Array.from(document.querySelectorAll('textarea'));
  let [generateBtn, buyBtn] = Array.from(document.querySelectorAll('button'));
  let table = document.querySelector('table.table tbody');
  

  generateBtn.addEventListener('click', generate);
  buyBtn.addEventListener('click', buy);

  function generate(){
    let data = JSON.parse(inputArea.value);

    for (let item of data){
      let row = document.createElement('tr');
      let imgCell = document.createElement('td');
      let nameCell = document.createElement('td');
      let priceCell = document.createElement('td');
      let decFactorCell = document.createElement('td');
      let checkCell = document.createElement('td');

      let img = document.createElement('img');
      img.src = item.img;
      imgCell.appendChild(img);
      
      let nameP = document.createElement('p');
      nameP.textContent = item.name;
      nameCell.appendChild(nameP);

      let priceP = document.createElement('p');
      priceP.textContent = item.price;
      priceCell.appendChild(priceP);

      let decFactorP = document.createElement('p');
      decFactorP.textContent = item.decFactor;
      decFactorCell.appendChild(decFactorP);

      let check = document.createElement('input');
      check.type = 'checkbox';
      checkCell.appendChild(check);

      row.appendChild(imgCell);
      row.appendChild(nameCell);
      row.appendChild(priceCell);
      row.appendChild(decFactorCell);
      row.appendChild(checkCell);

      table.appendChild(row);

    }
   
  }
  function buy(){
    let allCheckBoxes = Array.from(document.querySelectorAll('input[type="checkbox"]'));
    let checkedBoxes = allCheckBoxes.filter(x => x.checked);
    let sum = 0;
    let result = "";
    let decFactorSum = 0
    let furnitureNames = [];
    
    
    for (let checkedBox of checkedBoxes){
      let nameOfCurrentCheckBox = checkedBox.parentElement.parentElement.children[1].textContent;
      let priceOfCurrentCheckBox = Number(checkedBox.parentElement.parentElement.children[2].textContent);
      let decFactorOfCurrentCheckBox = Number(checkedBox.parentElement.parentElement.children[3].textContent);
      furnitureNames.push(nameOfCurrentCheckBox);
      decFactorSum += decFactorOfCurrentCheckBox;
      sum += priceOfCurrentCheckBox;

    }
    avgDecFactor = decFactorSum / checkedBoxes.length;
    result = `Bought furniture: ${furnitureNames.join(", ")}` + '\n';
    result += `Total price: ${sum.toFixed(2)}` + '\n';
    result += `Average decoration factor: ${avgDecFactor}`;

    outputArea.value = result;
  }
  


}


/* json data for parsing and adding to our generator
[
    {
        "img":"https://www.ikea.com/PIAimages/0447583_PE597395_S5.JPG",
        "name": "Sofa",
        "price": "259",
        "decFactor":"0.4"

    },
    {
        "img":"https://www.stylespafurniture.com/wp-content/uploads/2020/03/Cove_3_Door_Wardrobe_1.jpg",
        "name": "Wardrobe",
        "price": "120",
        "decFactor":"1.2"
    }
]
*/