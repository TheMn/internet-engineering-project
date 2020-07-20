$(document).ready(function () {
    console.log('salam');
    $('#div-1-next').click(function () {
        $("#form-part-1").css("display", "none");
        $("#form-part-2").css("display", "flex");
        scroll("#form-part-2");
    });
    $('#div-2-next').click(function () {
        $("#form-part-2").css("display", "none");
        $("#form-part-3").css("display", "flex");
        scroll("#form-part-3");
    });
    $('#div-2-prev').click(function () {
        $("#form-part-2").css("display", "none");
        $("#form-part-1").css("display", "flex");
        scroll("#form-part-1");
    });
    $('#div-3-next').click(function () {
        $("#form-part-3").css("display", "none");
        $("#form-part-4").css("display", "flex");
        scroll("#form-part-4");
    });
    $('#div-3-prev').click(function () {
        $("#form-part-3").css("display", "none");
        $("#form-part-2").css("display", "flex");
        scroll("#form-part-2");
    });
    $('#div-4-next').click(function () {
        $("#form-part-4").css("display", "none");
        $("#form-part-5").css("display", "flex");
        scroll("#form-part-5");
    });
    $('#div-4-prev').click(function () {
        $("#form-part-4").css("display", "none");
        $("#form-part-3").css("display", "flex");
        scroll("#form-part-3");
    });
    $('#div-5-prev').click(function () {
        $("#form-part-5").css("display", "none");
        $("#form-part-4").css("display", "flex");
        scroll("#form-part-4");
    });

    function scroll(id) {
        $('html, body').animate({
            scrollTop: $(id).offset().top - 100
        });
    }
});