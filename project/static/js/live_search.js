export const searchBar = document.querySelector('.search-bar')
export const dropDownListIngredientsUl = document.getElementById('dropdown-list-ingredients')
export const selectedIngredientsBox = document.querySelector('.selected-ingredients-box')



export function liveSearchIngredients(ingredient) {
  fetch(
    'http://127.0.0.1:5000/live-search',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(ingredient)
    }
  )

    .then(responseObj => {
      return responseObj.json();
    })

    .then(foundIngredients => {

      dropDownListIngredientsUl.innerHTML = ''
      if (foundIngredients.length > 0) {
        dropDownListIngredientsUl.style.display = 'block';
      } else {
        dropDownListIngredientsUl.style.display = 'none';
      }

      foundIngredients.forEach(foundIngredient => {
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