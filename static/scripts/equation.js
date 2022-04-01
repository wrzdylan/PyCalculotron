$( function() {
    $("#eq-button-exp").on("click", function() {
        $("#eq-input").val(function(_i, currentValue) {
            return currentValue + "**"
        })
    })

    $("#eq-button-rcarr").on("click", function() {
        $("#eq-input").val(function(_i, currentValue) {
            return currentValue + "sqrt()"
        })
    })
})