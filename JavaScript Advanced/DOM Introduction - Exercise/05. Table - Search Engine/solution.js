function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      allTableElements = document.querySelectorAll('tbody tr');
      let searchedEl = document.getElementById('searchField').value;
      for (const el of allTableElements){
         if (el.textContent.includes(searchedEl)){
            //el.textContent.style.fontWeight = 'bold';
            //el.textContent.style.textDecoration = 'underline';
            el.classList.add('select');
         }

      }

   }
}