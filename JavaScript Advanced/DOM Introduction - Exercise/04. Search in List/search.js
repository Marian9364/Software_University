function search() {
   let towns = document.querySelectorAll('ul li');
   let arrTowns = Array.from(towns);
   let searchField = document.getElementById('searchText');
   let matches = 0;
   let resultField = document.getElementById('result');
   let searchedEl = '';
   let currentTown = '';
   for (let town of arrTowns){
      searchedEl = searchField.value;
      currentTown = town.textContent;
      
      if (currentTown.includes(searchedEl)){
         matches++;
         town.style.textDecoration = 'underline';
         town.style.fontWeight = 'bold';
      }
   }
   resultField.textContent = `${matches} matches found`;
}
