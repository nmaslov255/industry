$('.menuu .button').click(function(event) {
    $(this).toggleClass('active');
    $('.burger').toggleClass('active');
    return false;
});

$('.bottom-field .news__read.bttn').click(function(event) {
    let $btn = $(this)

    let $newsBlock = $(this).closest('.news__item');
    let $dateBlock = $newsBlock.find('.date__text');
    let $itemBlock = $newsBlock.find('.news__one');

    let date = $dateBlock.attr('date');
    let items_length = $itemBlock.length;

    let limit = items_length+10;

    $.ajax({
        url: 'satoshi_ajax/'+date+'/'+limit,
        success: function(responce){
            $newsBlock.find('.items__box').html(responce);

            if ($newsBlock.find('.news__one').length != limit){
                $btn.closest('.bottom-field').hide()
            };
        }
    });
});

$.ajax({
    url: 'https://api.coingecko.com/api/v3/simple/price',
    data: {'ids': 'etoro-euro,tether,bitcoin,ethereum', 
           'vs_currencies': 'rub'},
    success: function(responce){
        $('#usdt-currency').text(responce['tether']['rub'])
        $('#etoro-euro-currency').text(responce['etoro-euro']['rub'])
        $('#bitcoin-currency').text(responce['bitcoin']['rub'])
        $('#ethereum-currency').text(responce['ethereum']['rub'])
    }
})