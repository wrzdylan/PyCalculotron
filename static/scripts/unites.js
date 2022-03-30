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
const MILLE = "mille";
const INCH = "inch";
const PIED = "pied";
const YARD = "yard";
const MILLE_MARIN = "mille_marin";

// ENERGIE
const JOULE = "joule"
const KJ = "kilojoule"
const CAL = "calorie"
const KCAL = "kilocalorie"
const WH = "watt_heure"
const KWH = "kilowatt_heure"
const BTU = "british_thermal_unit"
const THM = "therm_americain"
const FT_LB = "pied_livre"
const EV = "electronvolt"

// MASSE
const TONNE = "tonne";
const KG = "kilogramme";
const HG = "hectogramme";
const GRAMME = "gramme";
const DG = "decigramme";
const CG = "centigramme";
const MG = "milligramme";
const MMG = "microgramme";
const CARAT = "carat";
const GRAIN = "grain";
const OZ = "ounce";
const LB = "pound";
const QL = "quintal_long";
const QC = "quintal_court";
const TL = "tonne_longue";
const TC = "tonne_courte";
const STONE = "stone";

// STOCKAGE

// TEMPERATURE
const CELSIUS = "celsius";
const FAHRENHEIT = "fahrenheit";
const KELVIN = "kelvin";

// VITESSE

// VOLUME

//#endregion

function displayUnits(option) {
    $("#units-panel").css("visibility", "visible");
    $('.units-selector').children().remove().end();
    $('.units-value').val('');
    switch(option) {
        case DISTANCE :
            $('.units-selector').append('<option value='+KILOMETRE+'>Kilomètre</option>');
            $('.units-selector').append('<option value='+METRE+'>Mètre</option>');
            $('.units-selector').append('<option value='+DECIMETRE+'>Décimètre</option>');
            $('.units-selector').append('<option value='+CENTIMETRE+'>Centimètre</option>');
            $('.units-selector').append('<option value='+MILIMETRE+'>Millimètre</option>');
            $('.units-selector').append('<option value='+MILLE+'>Mille</option>');
            $('.units-selector').append('<option value='+INCH+'>Inch</option>');
            $('.units-selector').append('<option value='+PIED+'>Pied</option>');
            $('.units-selector').append('<option value='+YARD+'>Yard</option>');
            $('.units-selector').append('<option value='+MILLE_MARIN+'>Mille Marin</option>');
            break;
        case MASSE :
            $('.units-selector').append('<option value='+TONNE+'>Tonne</option>');
            $('.units-selector').append('<option value='+KG+'>Kilogramme</option>');
            $('.units-selector').append('<option value='+HG+'>Hectogramme</option>');
            $('.units-selector').append('<option value='+GRAMME+'>Gramme</option>');
            $('.units-selector').append('<option value='+DG+'>Decigramme</option>');
            $('.units-selector').append('<option value='+CG+'>Centigramme</option>');
            $('.units-selector').append('<option value='+MG+'>Milligramme</option>');
            $('.units-selector').append('<option value='+MMG+'>Microgramme</option>');
            $('.units-selector').append('<option value='+CARAT+'>Carat</option>');
            $('.units-selector').append('<option value='+GRAIN+'>Grain</option>');
            $('.units-selector').append('<option value='+OZ+'>Ounce</option>');
            $('.units-selector').append('<option value='+LB+'>Pound</option>');
            $('.units-selector').append('<option value='+QL+'>Quintal Long</option>');
            $('.units-selector').append('<option value='+QC+'>Quintal Court</option>');
            $('.units-selector').append('<option value='+TL+'>Tonne Longue</option>');
            $('.units-selector').append('<option value='+TC+'>Tonne Courte</option>');
            $('.units-selector').append('<option value='+STONE+'>Stone</option>');
            break;
        case ENERGIE :
            $('.units-selector').append('<option value='+JOULE+'>Joule</option>');
            $('.units-selector').append('<option value='+KJ+'>Kilojoule</option>');
            $('.units-selector').append('<option value='+CAL+'>Calorie</option>');
            $('.units-selector').append('<option value='+KCAL+'>Kilocalorie</option>');
            $('.units-selector').append('<option value='+WH+'>Watt-heure</option>');
            $('.units-selector').append('<option value='+KWH+'>Kilowatt-heure</option>');
            $('.units-selector').append('<option value='+BTU+'>British thermal uni</option>');
            $('.units-selector').append('<option value='+THM+'>Therm américain</option>');
            $('.units-selector').append('<option value='+FT_LB+'>Pied-livre</option>');
            $('.units-selector').append('<option value='+EV+'>Electronvolt</option>');
            break;
        case TEMPERATURE :
            $('.units-selector').append('<option value='+CELSIUS+'>Celsius</option>');
            $('.units-selector').append('<option value='+FAHRENHEIT+'>Fahrenheit</option>');
            $('.units-selector').append('<option value='+KELVIN+'>Kelvin</option>');
            break;
        default:
    }
}

function convert(origin, target, quantity) {
    console.log("Convertir " + quantity + " " + origin + " vers " + target + ".");
}

$( function() {
    $("#type-selector").on("change", function () {
        displayUnits($("#type-selector").val())    
    });

    $("#units-input").on("keyup", function(e) {
        this.value = this.value.replace(/[^0-9\.]/g,'');
        if($('#base-unit').val() == $('#target-unit').val()) {
            $('#units-res').val(this.value);
        }
        else {
            $('#units-res').val(convert($('#base-unit').val(), $('#target-unit').val(), this.value));
        }
    });

    $("#base-unit").on("change", function () {
        $('#units-res').val(convert($('#base-unit').val(), $('#target-unit').val(), $("#units-input").val()));
    });

    $("#target-unit").on("change", function () {
        $('#units-res').val(convert($('#base-unit').val(), $('#target-unit').val(), $("#units-input").val()));
    });

});