var input_is_service;

$(function () {
    input_is_service = $('input[name="is_service"]');

    $('.select2').select2({
        language: 'es',
        theme: 'bootstrap4'
    }); 

    

    $('input[name="precio"]')
        .TouchSpin({
            min: 0.01,
            max: 1000000,
            step: 0.01,
            decimals: 2,
            boostat: 5,
            maxboostedstep: 10,
            prefix: '$'
        })
        .on('change touchspin.on.min touchspin.on.max', function () {
            $('input[name="pvp"]').trigger("touchspin.updatesettings", {min: parseFloat($(this).val())});
        })
        .on('keypress', function (e) {
            return validate_text_box({'event': e, 'type': 'decimals'});
        });

    input_is_service.on('change', function () {
        var container = $(this).closest('.container-fluid').find('input[name="price"], input[name="stock"]').closest('.form-input');
        $(container).show();
        if (this.checked) {
            $(container).hide();
        }
    });

    input_is_service.trigger('change');

    
});