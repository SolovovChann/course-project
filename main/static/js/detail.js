$(document).ready(function(){
    $(".review").slick({
        arrows : true,
        infinite: true,
        slidesToScroll: 1,
        slidesToShow : 3,
        swipeToSlide: true,
        responsive: [{
            breakpoint: 756,
            settings: {
                adaptiveHeight: true,
                arrows: false,
                slidesToShow: 1,
                slidesToScroll: 1,
        }}]});
})

$(document).ready(setTimeout(function(){
    $(".message").slideUp();
}, 5000))

$("h2 .open_spoiler").click(function(){
    $(this).toggleClass("active");
    $(".commentForm").slideToggle();
}); 