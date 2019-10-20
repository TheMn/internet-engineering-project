/**
 * Created by Cloner on 10/21/2019.
 */
$(document).ready(function () {
    console.log("yo");
    var up, logo;
    console.log($(".nav").height());
    up = $(".nav").offset().top;
    logo = $(".nav").offset().top - $(".logo").height();
    console.log(logo);
    if ($(window).scrollTop() > up) {
        $(".logo").hide();
        $(".nav").addClass("fix");
        $(".nav a").css("color", "#1A6844");
        $("#ie").css({
            "border-right": "1px solid black",
            "padding-right": "0.8em"
        });
    }
    $(window).scroll(function () {

        windowHeight = $(window).height();

        if ($(window).scrollTop() > logo) {
            $(".logo").fadeOut();
        }
        else {
            $(".logo").fadeIn();
        }

        if ($(window).scrollTop() > up) {

            $(".nav").addClass("fix");
            $(".nav a").css("color", "#1A6844");
            $("#ie").css({
                "border-right": "1px solid black",
                "padding-right": "0.8em"
            });
            $(".nav ul a:last").attr("href", "#home");
            console.log("here");
            $(".nav ul i").removeClass("fa-chevron-down");
            $(".nav ul i").addClass("fa-chevron-up");
        }
        else {
            $(".nav").removeClass("fix");
            $(".nav a").css("color", "white");
            $("#ie").css({
                "border-right": "1px solid white",
                "padding-right": "0.8em"
            });
            $(".nav ul a:last").attr("href", "#about");
            $(".nav ul i").removeClass("fa-chevron-up");
            $(".nav ul i").addClass("fa-chevron-down");
        }

    });

    // Smooth Scrolling //
    $(function () {
        $('a[href*="#"]:not([href="#"])').click(function () {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html, body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });
    // End of smooth scroll //

});