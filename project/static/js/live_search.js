export const searchBar = document.querySelector('.search-bar')
export const dropDownListIngredientsUl = document.getElementById('dropdown-list-ingredients')
export const selectedIngredientsBox = document.querySelector('.selected-ingredients-box')



export function liveSearchIngredients(inputText) {
  let url = 'http://127.0.0.1:5000/live-search' + `?ingredient=${inputText}`;

  fetch(url)

    .then(responseObj => {
      return responseObj.json();
    })

    .then(foundIngredientsList => {

      dropDownListIngredientsUl.innerHTML = ''
      if (foundIngredientsList.length > 0) {
        dropDownListIngredientsUl.style.display = 'block';
      } else {
        dropDownListIngredientsUl.style.display = 'none';
      }

      foundIngredientsList.forEach(foundIngredient => {

        let dropSerchElementLi = document.createElement('li');
        dropSerchElementLi.innerHTML = foundIngredient;
        dropSerchElementLi.className = 'search-element';
        dropSerchElementLi.addEventListener('click', function () {
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
        });

        dropDownListIngredientsUl.appendChild(dropSerchElementLi);

      });
    })
}