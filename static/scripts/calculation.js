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
});



