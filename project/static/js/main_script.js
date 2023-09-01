import { searchBar, dropDownListIngredientsUl, liveSearchIngredients, } from './live_search.js';



const searchButton = document.querySelector('.search-button')
const selectedIngredientsSnans = document.getElementsByClassName('selected-ingredient-span')



function searchBarHandler() {

  let inputText = this.value

  if (inputText) {
    liveSearchIngredients(inputText)

  } else {
    dropDownListIngredientsUl.style.display = 'none';
    dropDownListIngredientsUl.innerHTML = ''
  };
};

searchBar.addEventListener('input', searchBarHandler);





function recipeSearch() {

  let ingredientsList = [];

  if (selectedIngredientsSnans.length > 0) {
    for (let spanElement of selectedIngredientsSnans) {
      ingredientsList.push(spanElement.innerText);
    }

    let url = 'http://127.0.0.1:5000/search-recipes-by-ingredients' + `?ingredients=${ingredientsList}`;

    window.location.href = url;

  };
};

searchButton.addEventListener('click', recipeSearch);
