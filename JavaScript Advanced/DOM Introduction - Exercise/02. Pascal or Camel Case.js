function solve() {
  let input = document.getElementById('text').value;
  let currentCase = document.getElementById('naming-convention').value;
  let resultField = document.getElementById('result');

  let inputWordsLowerCase = input.toLowerCase();
  
  let arrayOfWords = inputWordsLowerCase.split(" ");
  let resultStr = '';
  
  
  for (let i = 0; i < arrayOfWords.length; i ++){
    if (currentCase == "Camel Case"){
      if (i > 0){
        resultStr += arrayOfWords[i][0].toUpperCase() + arrayOfWords[i].slice(1);
      } else{resultStr += arrayOfWords[i];

      }
    } else if (currentCase == "Pascal Case"){
        resultStr += arrayOfWords[i][0].toUpperCase() + arrayOfWords[i].slice(1);
      } else {
        resultStr = "Error!"
      }
  }

  resultField.textContent = resultStr;

}
