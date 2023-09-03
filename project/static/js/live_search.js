export const searchBar = document.querySelector('.search-bar')
export const dropDownListIngredientsUl = document.getElementById('dropdown-list-ingredients')
export const selectedIngredientsBox = document.querySelector('.selected-ingredients-box')



export function clearElement(element) {
  element.innerHTML = '';
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



function createElement(tagName, className, { content = null, type = null }) {
  let element = document.createElement(tagName);
  element.className = className;

  if (content) {
    element.innerHTML = content;
  }
  if (type) {
    element.type = type
  }

  return element;
};


function addSelectedIngredient(dropSerchElementLi) {
  let selectIngredientSpan = createElement('span', 'selected-ingredient-span', { content: dropSerchElementLi.innerHTML });
  let closeButtonSelectIngredient = createElement('button', 'search-element-btn', { type: 'button' });

  closeButtonSelectIngredient.addEventListener('click', () => selectIngredientSpan.remove());

  selectIngredientSpan.appendChild(closeButtonSelectIngredient);

  selectedIngredientsBox.appendChild(selectIngredientSpan);
};



function dropSerchElementHandler(dropSerchElementLi) {
  clearElement(dropDownListIngredientsUl);
  setDisplay(dropDownListIngredientsUl, 'none');
  searchBar.value = ''

  addSelectedIngredient(dropSerchElementLi);
};



function createContentForDropDownList(foundIngredientsList) {
  clearElement(dropDownListIngredientsUl);
  switchDisplayElementIfContent(dropDownListIngredientsUl, foundIngredientsList);

  if (foundIngredientsList.length > 0) {
    foundIngredientsList.forEach(foundIngredient => {

      let dropSerchElementLi = createElement('li', 'search-element', { content: foundIngredient })
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