window.onload = () => {  
    document.getElementById('table').hidden = true;
    document.getElementById('back').style.display = 'none';
    document.getElementById('list').style.display = 'none';
    document.getElementById('delimiter').hidden = false;
    document.getElementById('reload').style.display = 'none';
    document.getElementById('roslov').style.display = 'none';
    document.getElementById('schedule').onclick = function(){
        document.getElementById('table').hidden = false;
        document.getElementById('list').style.display = 'block';
        document.getElementById('schedule').style.display = 'none';
        document.getElementById('back').style.display = 'block';
        document.getElementById('delimiter').hidden = true;
        document.getElementById('teacher').style.display = 'none';
        document.getElementById('reload').style.display = 'block';
        document.getElementById('roslov').style.display = 'none';
        document.getElementById('About_ass').style.display = 'none';
    }
    document.getElementById('back').onclick = () => {
        document.getElementById('table').hidden = true;
        document.getElementById('list').style.display = 'none';
        document.getElementById('schedule').style.display = 'block';
        document.getElementById('back').style.display = 'none';
        document.getElementById('delimiter').hidden = false;
        document.getElementById('teacher').style.display = 'block';
        document.getElementById('reload').style.display = 'none';
        document.getElementById('About_ass').style.display = 'block';
    }
    document.getElementById('About_ass').onclick = () => {
        document.getElementById('roslov').style.display = 'block';
    }
    document.getElementById('reload').onclick = () => {
        let req = new XMLHttpRequest();
        req.open('GET', '/result?stat=' + document.getElementById('group_selector').value, true);
        req.send();
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
