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


function addSelectedIngredient(dropSearchElementLi) {
  let selectIngredientSpan = createElement('span', 'selected-ingredient-span', { content: dropSearchElementLi.innerHTML });
  let closeButtonSelectIngredient = createElement('button', 'search-element-btn', { type: 'button' });

  closeButtonSelectIngredient.addEventListener('click', () => selectIngredientSpan.remove());

  selectIngredientSpan.appendChild(closeButtonSelectIngredient);

  selectedIngredientsBox.appendChild(selectIngredientSpan);
};


function dropSearchElementHandler(dropSearchElementLi) {
  clearElement(dropDownListIngredientsUl);
  setDisplay(dropDownListIngredientsUl, 'none');
  searchBar.value = '';

  addSelectedIngredient(dropSearchElementLi);
};


function createContentForDropDownList(foundIngredientsList) {
  clearElement(dropDownListIngredientsUl);
  switchDisplayElementIfContent(dropDownListIngredientsUl, foundIngredientsList);

  if (foundIngredientsList.length > 0) {
    foundIngredientsList.forEach(
      foundIngredient => {
        let dropSearchElementLi = createElement('li', 'search-element', { content: foundIngredient });
        dropSearchElementLi.addEventListener('click', () => dropSearchElementHandler(dropSearchElementLi));
        dropDownListIngredientsUl.appendChild(dropSearchElementLi);
      }
    );
  };
};


export function liveSearchIngredients(inputText) {
  let url = 'http://127.0.0.1:5000/ingredient-live-search' + `?title_fragment=${inputText}`;

  fetch(url)
    .then(responseObj => {
      return responseObj.json();
    })
    .then(foundIngredientsList => {
      createContentForDropDownList(foundIngredientsList);
    });
}
