window.onscroll = function(ev) {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        let origin = document.location.origin;
        let category_slug = $('.top__old a.active span').data('category-slug');
        let offset = $('.news__item').length;
        let query_url = `${origin}/more_news_ajax/${category_slug}/${offset}`;

        $.ajax({
            url: query_url,
            success: function(responce){
                console.log(1111)
                $('.news__content').append(responce)
            }
        });
    }
};

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

    let items_length = $itemBlock.length;

    let origin = document.location.origin;
    let category_id = $newsBlock.data('category-id');
    let date = $dateBlock.attr('date');
    let limit = items_length+10;

    let query_url = `${origin}/news_ajax/${category_id}/${date}/${limit}`;

    $.ajax({
        url: query_url,
        success: function(responce){
            $newsBlock.find('.items__box').html(responce);

            if ($newsBlock.find('.news__one').length != limit){
                $newsBlock.find('.bottom-field').hide()
            };
        }
    });
});

// TODO: remove copy-paste
$('.news__item .news__all').click(function(event) {
    let $btn = $(this)

    let $newsBlock = $(this).closest('.news__item');
    let $dateBlock = $newsBlock.find('.date__text');
    let $itemBlock = $newsBlock.find('.news__one');

    let items_length = $itemBlock.length;

    let origin = document.location.origin;
    let category_id = $newsBlock.data('category-id');
    let date = $dateBlock.attr('date');
    let limit = $(this).data('total-news-per-day')

    let query_url = `${origin}/news_ajax/${category_id}/${date}/${limit}`;

    $.ajax({
        url: query_url,
        beforeSend: function(){
            $btn.find('span').hide();
            $btn.find('img').show();
        },
        success: function(responce){
            $newsBlock.find('.items__box').html(responce);
            $newsBlock.find('.bottom-field').hide()
            $btn.hide(500)
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