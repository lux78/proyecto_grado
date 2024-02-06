var input_fecha_nacimiento;

$(function () {
    input_fecha_nacimiento = $('input[name="fecha_nacimiento"]');

    input_fecha_nacimiento.datetimepicker({
        useCurrent: false,
        format: 'YYYY-MM-DD',
        locale: 'es',
        keepOpen: false,
        maxDate: new Date()
    });

    $('.select2').select2({
        language: 'es',
        theme: 'bootstrap4'
    });

    $('input[name="nombres"]')
        .on('keypress', function (e) {
            return validate_text_box({ 'event': e, 'type': 'letters' });
        });

    $('input[name="ci"]')
        .on('keypress', function (e) {
            return validate_text_box({ 'event': e, 'type': 'numbers' });
        });

    $('input[name="celular"]')
        .on('keypress', function (e) {
            return validate_text_box({ 'event': e, 'type': 'numbers' });
        });
});