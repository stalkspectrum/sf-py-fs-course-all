// Написать метод jQuery.prototype.text(),
// который возвращает или изменяет текстовое содержимое выбранных элементов.
const $ = (e) => new jQuery(e);
//$('button').click(e => console.log(e.target));

//$('button').click($('h1') => $('h1').remove());

//$('.message').html('<b><u><i>Message line</i></u></b>');
console.log($('.message').html());
//$('.message').text('<b><u>Message line</u></b>');
