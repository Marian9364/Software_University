function solve() {
  let text = Array.from(document.getElementById('input').value.trimEnd().split('.'));
  let result = '';
  
  while(text.length > 0){
    let currentPar = '<p>';
    for (let i = 0; i < 3; i++) {
      let currentSent = text.shift().replace('.', '');
      currentPar += currentSent.trimEnd();
      if(currentSent.length > 0){
        currentPar += '.'
      }
      if(text.length == 0){
        break;
      }
    }
    currentPar += '</p>'
    if(currentPar != '<p></p>'){
      result += currentPar;
    }
  }
  document.getElementById('output').innerHTML = result.trimEnd();
}