//RESTART GAME BUTTON
var restart = document.querySelector("#restart");

var squares = document.querySelectorAll('td');

//Clear all the squares
function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = ''
  }
}

restart.addEventListener('click',clearBoard);

// var cellOne = document.querySelector("#one"); -> We can repeat this for 9 times for all cells but that isn't suggested A/DRY principles
// cellOne.addEventListener('click',function(){
//   if(cellOne.textContent === ''){
//     cellOne.textContent = 'X';
//   }else if(cellOne.textContent === 'X'){
//     cellOne.textContent = 'O';
//   }else{
//     cellOne.textContent = '';
//   }
// })
// horizontalComplete = ((squares[0].textContent !== '') && (squares[0].textContent===squares[1].textContent===squares[2].textContent))||
//                       ((squares[3].textContent !== '') && (squares[3].textContent===squares[4].textContent===squares[5].textContent)) ||
//                       ((squares[6].textContent !== '') && (squares[6].textContent===squares[7].textContent===squares[8].textContent))
//
// verticalComplete = ((squares[0].textContent !== '') && (squares[0].textContent===squares[3].textContent===squares[6].textContent))||
//                       ((squares[1].textContent !== '') && (squares[1].textContent===squares[4].textContent===squares[7].textContent)) ||
//                       ((squares[2].textContent !== '') && (squares[2].textContent===squares[5].textContent===squares[8].textContent))
//
// diagonalComplete = ((squares[0].textContent !== '') && (squares[0].textContent===squares[4].textContent===squares[8].textContent))||
//                       ((squares[2].textContent !== '') && (squares[2].textContent===squares[4].textContent===squares[6].textContent))
//
//
// function boardComplete(){
//   if (horizontalComplete || verticalComplete || diagonalComplete){
//     alert(this.textContent + "  WINS :)")
//     clearBoard();
//   }
// }

function changeMarker(){
  if(this.textContent === ''){
    this.textContent = 'X';
  } else if(this.textContent === 'X'){
    this.textContent = 'O';
  } else {
    this.textContent = '';
  }

}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker);
  // boardComplete();
}
