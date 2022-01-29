function create(words) {
   let arrInput = Array.from(words);
   let content = document.getElementById('content');

   for (let i = 0; i < arrInput.length; i++){
      let text = arrInput[i];
      let div = document.createElement('div');
      let p = document.createElement('p');
      
      p.textContent = text;
      div.appendChild(p);
      p.style.display = 'none';

      content.appendChild(div);

      div.addEventListener('click', function(e){
         p.style.display = 'inline-block';
      })
   }

}