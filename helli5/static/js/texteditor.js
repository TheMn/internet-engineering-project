var wys = select('.edit-text');
var wyg = select('.text');
console.log(wyg);

wys.addEventListener('keyup', function(e){
  wyg.innerHTML = this.innerHTML;
});

var buttons = select('.formatter button');

buttons.forEach(function(button){
  button.addEventListener('click', function(){
    formatText(this.getAttribute('data-command'));
  })
});

function formatText(command){
  if(command === 'h1' || command === 'h2' || command === 'p'){
    document.execCommand('formatBlock', false, command);
    return;
  }else if(command === 'createlink'){
    var url = prompt('Enter the link here: ', 'http:\/\/');
    document.execCommand(command, false, url);
  }else{
    document.execCommand(command, false, null);
  }
  wys.dispatchEvent(new Event('keyup'));
}

function select(query){
  var elements = document.querySelectorAll(query);
  return ( elements.length > 1 ) ? elements : elements[0] ;
}