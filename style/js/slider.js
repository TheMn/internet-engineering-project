var sliderIndex = 0;
showSlider(sliderIndex);
function showSlider(index){
    var slider = document.querySelectorAll('.slider');
    var dots   = document.querySelectorAll('.dot-navigation');
    if(index >= slider.length) sliderIndex = 0;
    if(index < 0) sliderIndex = slider.length - 1;
    for(var i = 0 ; i < slider.length ; i++ ){
        slider[i].style.display = "none";
        dots[i].classList.remove('active-dot');
    }
    slider[sliderIndex].style.display = "block";
    dots[sliderIndex].classList.add('active-dot');
}
document.querySelector('#arrow-prev').addEventListener('click',function(){
    showSlider(--sliderIndex);
});
document.querySelector('#arrow-next').addEventListener('click',function(){
    showSlider(++sliderIndex);
});

document.querySelectorAll('.dot-navigation').forEach(function(element){
    element.addEventListener('click',function(){
        var dots = Array.prototype.slice.call(this.parentElement.children);
        var dotIndex = dots.indexOf(element);
        showSlider(sliderIndex = dotIndex);
    });
});
setInterval(function(){
    showSlider(--sliderIndex);
},4000);