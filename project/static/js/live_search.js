export const searchBar = document.querySelector('.search-bar')
export const dropDownListIngredientsUl = document.getElementById('dropdown-list-ingredients')
export const selectedIngredientsBox = document.querySelector('.selected-ingredients-box')



export function clearElement(element) {
  element.innerHTML = ''
}


export function setDisplay(element, display) {
  element.style.display = display;
}


function switchDisplayElementIfContent(element, foundIngredientsList) {
  if (foundIngredientsList.length > 0) {
    setDisplay(element, 'block');
  } else {
    setDisplay(element, 'none');
  }
};


function createDropSerchElementLi(foundIngredient) {
  let dropSerchElementLi = document.createElement('li');
  dropSerchElementLi.innerHTML = foundIngredient;
  dropSerchElementLi.className = 'search-element';

  return dropSerchElementLi;
};


function dropSerchElementHandler(dropSerchElementLi) {
  dropDownListIngredientsUl.innerHTML = ''
  dropDownListIngredientsUl.style.display = 'none';
  searchBar.value = ''

  let span = document.createElement('span');
  span.innerHTML = dropSerchElementLi.innerHTML;
  span.className = 'selected-ingredient-span';

  let btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'search-element-btn';

  btn.addEventListener('click', function () {
    span.remove();
  })

  span.appendChild(btn);

  selectedIngredientsBox.appendChild(span);
};



function createContentForDropDownList(foundIngredientsList) {
  clearElement(dropDownListIngredientsUl);
  switchDisplayElementIfContent(dropDownListIngredientsUl, foundIngredientsList);

  if (foundIngredientsList.length > 0) {

    foundIngredientsList.forEach(foundIngredient => {
      let dropSerchElementLi = createDropSerchElementLi(foundIngredient)
      dropSerchElementLi.addEventListener('click', () => dropSerchElementHandler(dropSerchElementLi));
      dropDownListIngredientsUl.appendChild(dropSerchElementLi);
    });
  };
};






export function liveSearchIngredients(inputText) {
  let url = 'http://127.0.0.1:5000/live-search' + `?ingredient=${inputText}`;
  fetch(url)
    .then(responseObj => {
      return responseObj.json();
    })
    .then(foundIngredientsList => {
      createContentForDropDownList(foundIngredientsList);
    });
}