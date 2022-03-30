"use strict";

//CONSTANTES
const DISTANCE = "distance";
const ENERGIE = "energie";
const MASSE = "masse";
const STOCKAGE = "stockage";
const TEMPERATURE = "temperature";
const VITESSE = "vitesse";
const VOLUME = "volume";


function displayUnits(option) {
    $("#units-panel").css("visibility", "visible");
    $('.units-selector').children().remove().end();
    switch(option) {
        case TEMPERATURE :
            $('.units-selector').append('<option value="celsius">Celsius</option>');
            $('.units-selector').append('<option value="fahrenheit">Fahrenheit</option>');
            $('.units-selector').append('<option value="kelvin">Kelvin</option>');
            break;
        default:
    }
}

$( function() {
    $("#type-selector").on("change", function () {
        displayUnits($("#type-selector").val())    
    });
});