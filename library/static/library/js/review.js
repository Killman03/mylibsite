console.log('working')

const month_name = ['Янв', "Февр", "Мар", "Апр", "Июнь", "Июль",
 "Авг", "Сент", "Окт", "Нояб", "Дек"];

$('#comment_form').submit(function(e){
    e.preventDefault();

    let dt = new Date()
    let time = dt.getDay() + ' ' + month_name[dt.getUTCMonth()] + ', ' + dt.getFullYear();

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr('action'),

        dataType: 'json',

        success: function(response){
            if(response.bool) {
                console.log('Отзыв успешно сохранен');
                console.log('Средний рейтинг ' + response.avg_reviews.rating);
                let _html = `<div class="card my-3" style="width: 90%;">
                            <div class="card-body">
                            <div class="thumb d-flex justify-content-between">
                            <p class="pe-3">${response.context.user}</p>
                            <span>${time}</span>
                            <div class="product_rating">`

                            for(let i = 1; i <= response.context.rating; i++ ){
                                _html += '<i class="bi bi-star-fill" style="color: gold;"></i>'
                            };

                            _html += `</div>
                            </div>
                            <div class="desc">
                            <div>
                            <div class="product_rating" style="width: 100%"></div>
                            </div>
                            <p class="card-text">${response.context.review}</p>
                            </div>
                            </div>
                            </div>`;
                $('.comment-list').prepend(_html);
                }
            else{
                console.log("Произошла ошибка при сохранение отзыва");
            }
        }
    })
})