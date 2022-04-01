"use strict";


function displayInput(id) {
    $('.form-control').each( 
        function() {
            if($(this).hasClass(id)) {
                $(this).css("display", "block");
            } else {
                $(this).css("display", "none");
            }
        }
    )
}


$( function() {
    $('#operators :input').on('change', function () {
        $(this).each(function() {
            if($(this).is(':checked')) { 
                displayInput($(this).attr('id'))
            }
        })
    })

    $('.numbers-input').on('keydown', function() {
        if($(this).val().length >= 0) {
            $('.btn-calculotron').css("visibility", "visible")
        } else {
            $('.btn-calculotron').css("visibility", "hidden")
        }
    })
});



