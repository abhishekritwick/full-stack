$('h1').click(function(){
  $(this).text('I was changed');
})


//KEYPRESS
// $('input').eq(0).keypress(function(){
//   $('h3').toggleClass('turnBlue')
// })

$('input').eq(0).keypress(function(event){
  // console.log(event);
  if(event.which === 13){
    $('h3').toggleClass('turnBlue');
  }
})

$('h1').on('mouseenter',function(){
  $(this).toggleClass('turnBlue');
})

$('input').eq(1).on('click',function(){
  $('.container').fadeOut(3000);
  //$('.container').slideUp(3000);
})
