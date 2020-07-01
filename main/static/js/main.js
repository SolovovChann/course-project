// Open mobile side menu on click
$(".mob-menu").click(function(){
    $("nav").toggleClass("active");
    $(this).toggleClass("active");
})
$("#search-trigger").click(function(){
    $("#search-form").fadeToggle();
})

let input = document.querySelector(".amount input[name=quantity]"),
    form = document.querySelector(".buyPanel form");

function addOne(){
    if ( +input.value < +input.max ){
        +input.value++;
    }
}
function minusOne(){
    if ( +input.value > +input.min ){
        +input.value--;
    }
}