var btn1 = document.getElementById('bt1');
var btn2 = document.getElementById('bt2');
console.log(btn1);
console.log(btn2);
console.log(this);

btn1.addEventListener('click', function() {
  console.log("hsddghjfjs")
    if (btn2.classList.contains('green')) {
      btn2.classList.remove('green');
    } 
  else
  btn2.classList.add('green')

});

btn2.addEventListener('click', function() {
  
    if (btn1.classList.contains('green')) {
      btn1.classList.remove('green');
    } 
  else
  btn1.classList.add('green')
  
});

