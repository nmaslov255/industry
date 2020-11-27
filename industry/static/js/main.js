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

function changePriceTicker($el, newPrice){
    var lastPrice = parseFloat($el.text());

    if (newPrice > lastPrice){
        $el.css('color','rgb(2, 192, 118)');
    } else if (newPrice < lastPrice) {
        $el.css('color','rgb(248, 73, 96)');
    } else {
        $el.css('color', 'black');
    }

    $el.text(newPrice)
}

function loadTicker(){
    $.ajax({
        url: 'https://api.coingecko.com/api/v3/simple/price',
        data: {'ids': 'etoro-euro,tether,bitcoin,ethereum', 
               'vs_currencies': 'rub'},
        success: function(responce){
            $('#usdt-currency').slideUp(600, callback=() => {
                var $el = $('#usdt-currency');
                changePriceTicker($el, responce['tether']['rub']);
            }).slideDown(600)

            $('#etoro-euro-currency').slideUp(600, callback=() => {
                var $el = $('#etoro-euro-currency');
                changePriceTicker($el, responce['etoro-euro']['rub']);
            }).slideDown(600)

            $('#bitcoin-currency').slideUp(600, callback=() => {
                var $el = $('#bitcoin-currency');
                changePriceTicker($el, responce['bitcoin']['rub']);
            }).slideDown(600)

            $('#ethereum-currency').slideUp(600, callback=() => {
                var $el = $('#ethereum-currency');
                changePriceTicker($el, responce['ethereum']['rub']);
            }).slideDown(600)
        }
    })
}
loadTicker()
setInterval(loadTicker, 1000*60)