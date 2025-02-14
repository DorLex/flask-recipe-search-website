import {
  searchBar,
  dropDownListIngredientsUl,
  liveSearchIngredients,
  clearElement,
  setDisplay,
}
  from './live_search.js';



const searchButton = document.querySelector('.search-button');
const selectedIngredientsSpans = document.getElementsByClassName('selected-ingredient-span');


function searchBarHandler() {
  let inputText = this.value;

  if (inputText) {
    liveSearchIngredients(inputText);

  } else {
    setDisplay(dropDownListIngredientsUl, 'none');
    clearElement(dropDownListIngredientsUl);
  };
};

searchBar.addEventListener('input', searchBarHandler);


function recipeSearch() {
  let ingredientsList = [];

  if (selectedIngredientsSpans.length > 0) {
    for (let spanElement of selectedIngredientsSpans) {
      ingredientsList.push(spanElement.innerText);
    }

    let url = 'http://127.0.0.1:5000/search-recipes-by-ingredients' + `?ingredients=${ingredientsList}`;

    window.location.href = url;
  };
};

searchButton.addEventListener('click', recipeSearch);
