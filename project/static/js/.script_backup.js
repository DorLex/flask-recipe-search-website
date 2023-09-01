const searchButton = document.querySelector('.search-button');
const searchBar = document.querySelector('.search-bar');

const dropDownListIngredientsUl = document.getElementById('dropdown-list-ingredients');

const selectedIngredientsBox = document.querySelector('.selected-ingredients-box');
const selectedIngredients = document.getElementsByClassName('selected-ingredient-span');






function liveSearchFetch(ingredient) {
  fetch('http://127.0.0.1:5000/live-search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json; charset=utf-8'
    },
    body: JSON.stringify(ingredient)
  })
    .then(response => {
      return response.json();
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
};




function searchBarHandler() {
  let inputText = this.value

  // мб убрать
  let ingredient = {
    ingredient: inputText,
  };


  if (inputText) {
    liveSearchFetch(ingredient)

  } else {
    dropDownListIngredientsUl.style.display = 'none';
    dropDownListIngredientsUl.innerHTML = ''
  };
};



searchBar.addEventListener('input', searchBarHandler);



function search() {
  let ingList = []
  console.log(selectedIngredients);

  if (selectedIngredients.length > 0) {
    for (let element of selectedIngredients) {
      ingList.push(element.innerText);
    }
    window.location.href = `http://127.0.0.1:5000/search-recipes/${ingList}`;
  };
};


searchButton.addEventListener('click', search);
