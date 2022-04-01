"use strict";
//#region CONSTANTES
const DISTANCE = "distance";
const ENERGIE = "energie";
const MASSE = "masse";
const STOCKAGE = "stockage";
const TEMPERATURE = "temperature";
const VITESSE = "vitesse";
const VOLUME = "volume";

// DISTANCE
const KILOMETRE = "kilometre";
const METRE = "metre";
const DECIMETRE = "decimetre";
const CENTIMETRE = "centimetre";
const MILIMETRE = "millimetre";
const MILLE = "mile";
const INCH = "pouce";
const PIED = "pied";
const YARD = "yard";
const MILLE_MARIN = "mille_marin";

// ENERGIE
const JOULE = "J"
const KJ = "kJ"
const CAL = "cal"
const KCAL = "kcal"
const WH = "W*h"
const KWH = "kW*h"

// MASSE
const TONNE = "t";
const KG = "kg";
const GRAMME = "g";
const MG = "mg";
const OZ = "oz";
const LB = "lb";

// STOCKAGE
const BIT = "bit"
const OCTET = "o"
const KO = "ko"
const MO = "mo"
const GO = "go"
const TO = "to"

// TEMPERATURE
const CELSIUS = "celsius";
const FAHRENHEIT = "fahrenheit";
const KELVIN = "kelvin";

// VITESSE
const KMPH = "kmh"
const MPS = "mps"
const MPH = "mph"
const KNOT = "noeud"
// VOLUME
const LITRE = "litre"
const BBL = "baril"
const M3  = "m_cube"
const C3 = "cm_cube"
const GALUS = "gallon"

//#endregion

function displayUnits(option) {
    $("#units-panel").css("visibility", "visible");
    $('.units-selector').children().remove().end();
    $('.units-value').val('');
    switch(option) {
        case DISTANCE :
            // $('.units-selector').append('<option value='+KILOMETRE+'>Kilomètre</option>');
            $('.units-selector').append('<option value='+METRE+'>Mètre</option>');
            // $('.units-selector').append('<option value='+DECIMETRE+'>Décimètre</option>');
            // $('.units-selector').append('<option value='+CENTIMETRE+'>Centimètre</option>');
            // $('.units-selector').append('<option value='+MILIMETRE+'>Millimètre</option>');
            $('.units-selector').append('<option value='+MILLE+'>Mille</option>');
            $('.units-selector').append('<option value='+INCH+'>Inch</option>');
            $('.units-selector').append('<option value='+PIED+'>Pied</option>');
            $('.units-selector').append('<option value='+YARD+'>Yard</option>');
            // $('.units-selector').append('<option value='+MILLE_MARIN+'>Mille Marin</option>');
            break;
        case MASSE :
            $('.units-selector').append('<option value='+TONNE+'>Tonne</option>');
            $('.units-selector').append('<option value='+KG+'>Kilogramme</option>');
            // $('.units-selector').append('<option value='+HG+'>Hectogramme</option>');
            $('.units-selector').append('<option value='+GRAMME+'>Gramme</option>');
            // $('.units-selector').append('<option value='+DG+'>Decigramme</option>');
            // $('.units-selector').append('<option value='+CG+'>Centigramme</option>');
            $('.units-selector').append('<option value='+MG+'>Milligramme</option>');
            // $('.units-selector').append('<option value='+MMG+'>Microgramme</option>');
            // $('.units-selector').append('<option value='+CARAT+'>Carat</option>');
            // $('.units-selector').append('<option value='+GRAIN+'>Grain</option>');
            $('.units-selector').append('<option value='+OZ+'>Ounce</option>');
            $('.units-selector').append('<option value='+LB+'>Pound</option>');
            // $('.units-selector').append('<option value='+QL+'>Quintal Long</option>');
            // $('.units-selector').append('<option value='+QC+'>Quintal Court</option>');
            // $('.units-selector').append('<option value='+TL+'>Tonne Longue</option>');
            // $('.units-selector').append('<option value='+TC+'>Tonne Courte</option>');
            // $('.units-selector').append('<option value='+STONE+'>Stone</option>');
            break;
        case ENERGIE :
            $('.units-selector').append('<option value='+JOULE+'>Joule</option>');
            $('.units-selector').append('<option value='+KJ+'>Kilojoule</option>');
            $('.units-selector').append('<option value='+CAL+'>Calorie</option>');
            $('.units-selector').append('<option value='+KCAL+'>Kilocalorie</option>');
            $('.units-selector').append('<option value='+WH+'>Watt-heure</option>');
            $('.units-selector').append('<option value='+KWH+'>Kilowatt-heure</option>');
            // $('.units-selector').append('<option value='+BTU+'>British thermal uni</option>');
            // $('.units-selector').append('<option value='+THM+'>Therm américain</option>');
            // $('.units-selector').append('<option value='+FT_LB+'>Pied-livre</option>');
            // $('.units-selector').append('<option value='+EV+'>Electronvolt</option>');
            break;
        case STOCKAGE :
            $('.units-selector').append('<option value='+BIT+'>Bit</option>');
            $('.units-selector').append('<option value='+OCTET+'>Octect</option>');
            $('.units-selector').append('<option value='+KO+'>Kilooctet</option>');
            $('.units-selector').append('<option value='+MO+'>Megaoctet</option>');
            $('.units-selector').append('<option value='+GO+'>Gigaoctet</option>');
            $('.units-selector').append('<option value='+TO+'>Teraoctet</option>');
            $('.units-selector').append('<option value='+MIB+'>Mébioctet</option>');
            break;
        case TEMPERATURE :
            $('.units-selector').append('<option value='+CELSIUS+'>Celsius</option>');
            $('.units-selector').append('<option value='+FAHRENHEIT+'>Fahrenheit</option>');
            $('.units-selector').append('<option value='+KELVIN+'>Kelvin</option>');
            break;
        case VITESSE :
            $('.units-selector').append('<option value='+KMPH+'>Kilomètre par heure</option>');
            $('.units-selector').append('<option value='+MPS+'>Mètre par seconde</option>');
            $('.units-selector').append('<option value='+MPH+'>Mille par heure</option>');
            $('.units-selector').append('<option value='+KNOT+'>Knot</option>');
            break;
        case VOLUME :
            $('.units-selector').append('<option value='+LITRE+'>Litre</option>');
            $('.units-selector').append('<option value='+BBL+'>Baril de pétrole</option>');
            $('.units-selector').append('<option value='+M3+'>Mètre cube</option>');
            $('.units-selector').append('<option value='+C3+'>Centimètre cube</option>');
            $('.units-selector').append('<option value='+GALUS+'>Gallon (US)</option>');
            break;
        default:
            // $('.units-selector').append('<option value='++'></option>');
    }
}

function convert(origin, target, quantity) {
    // select-type = $("#type-selector").val()
    const myData = JSON.stringify({
                'select-type' : $("#type-selector").val(),
                'units-input': quantity,
                'type-in' : origin,
                'type-out' : target
            })
    $.ajax({
        type : "POST",
        url : '/conversion',
        dataType: "json",
        data: myData,
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            console.log(data)
            $("#units-res").val(data);
        }
    });
}

$( function() {
    $("#type-selector").on("change", function () {
        displayUnits($("#type-selector").val())    
    });

    $(".numbers-input").on("keyup", function(e) {
        this.value = this.value.replace(/[^0-9\.]/g,'');
    });

    $("#units-input").on("keyup", function(e) {
        if($('#base-unit').val() == $('#target-unit').val()) {
            $('#units-res').val(this.value);
        }
        else {
            $('#units-res').val(convert($('#base-unit').val(), $('#target-unit').val(), parseFloat(this.value)));
        }
    });

    $("#base-unit").on("change", function () {
        $('#units-res').val(convert($('#base-unit').val(), $('#target-unit').val(), parseFloat($("#units-input").val())));
    });

    $("#target-unit").on("change", function () {
        $('#units-res').val(convert($('#base-unit').val(), $('#target-unit').val(), parseFloat($("#units-input").val())));
    });

});
