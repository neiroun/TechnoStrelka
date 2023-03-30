 window.onload = () => {   
    document.getElementById('table').hidden = true;
    document.getElementById('back').hidden = true;
    document.getElementById('list').style.display = 'none';
    document.getElementById('schedule').onclick = function(){
        document.getElementById('table').hidden = false;
        document.getElementById('list').style.display = 'block';
        document.getElementById('schedule').hidden = true;
    }
 }
 jQuery(($) => {
    $('.select').on('click', '.select__head', function () {
        if ($(this).hasClass('open')) {
            $(this).removeClass('open');
            $(this).next().fadeOut();
        } else {
            $('.select__head').removeClass('open');
            $('.select__list').fadeOut();
            $(this).addClass('open');
            $(this).next().fadeIn();
        }
    });

    $('.select').on('click', '.select__item', function () {
        $('.select__head').removeClass('open');
        $(this).parent().fadeOut();
        $(this).parent().prev().text($(this).text());
        $(this).parent().prev().prev().val($(this).text());
    });

    $(document).click(function (e) {
        if (!$(e.target).closest('.select').length) {
            $('.select__head').removeClass('open');
            $('.select__list').fadeOut();
        }
    });
});