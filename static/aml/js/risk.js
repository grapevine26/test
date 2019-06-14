window.onload = function () {
    $('.final_triangle').fadeIn(500);
    $('.table_div1').fadeIn(2000).css("display", "inline-block");
    setTimeout(function () {
        $('.one').css({
            background: "#f06292"
        }).fadeIn();
        $('.two').css({
            top: "160px",
            background: "#9575cd"
        }).fadeIn();
        $('.three').css({
            top: "320px",
            background: "#64b5f6"
        }).fadeIn();
        $('.four').css({
            top: "480px",
            background: "#4dd0e1"
        }).fadeIn();
    }, 750);
    setTimeout(function () {

    }, 1400);
};
