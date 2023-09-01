import {
  searchBar,
  dropDownListIngredientsUl,
  liveSearchIngredients,
} from './live_search.js';



const searchButton = document.querySelector('.search-button')
const selectedIngredients = document.getElementsByClassName('selected-ingredient-span')



function searchBarHandler() {
  let inputText = this.value

  // мб убрать
  let ingredient = {
    ingredient: inputText,
  };


  if (inputText) {
    liveSearchIngredients(ingredient)

  } else {
    dropDownListIngredientsUl.style.display = 'none';
    dropDownListIngredientsUl.innerHTML = ''
  };
};



searchBar.addEventListener('input', searchBarHandler);



function recipeSearch() {
  let ingList = []

  if (selectedIngredients.length > 0) {
    for (let element of selectedIngredients) {
      ingList.push(element.innerText);
    }
    window.location.href = `http://127.0.0.1:5000/search-recipes/${ingList}`;
  };
};


searchButton.addEventListener('click', recipeSearch);
