$(document).ready(function () {
    // Выбрать все элементы ввода с типом "tel"
    $("input[type='phone']").inputmask({
        "mask": "+7 (999) 999-99-99"
    });
});