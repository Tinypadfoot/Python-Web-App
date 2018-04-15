// console.log('connected');
//Restart Game button

var restart = document.querySelector("#b");


//Grabs all the Squares

var squares = document.querySelectorAll('td');

//Clears all the Squares

function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = ' ';
  }
}

restart.addEventListener('click',clearBoard);

//Check the square square marker

function changeMarker() {
  if (this.textContent === ' ') {
    this.textContent = 'X';
  }else if (this.textContent === 'X') {
    this.textContent = 'O';
  }else {
    this.textContent = ' ';
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker)
}


//Check the square changeMarker

//For loop to add EL to all the squares
