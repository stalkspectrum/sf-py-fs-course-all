/*  Здесь сначала определены основная функция и метод,
    без которых работать не будет */
function jQuery (selector, context = document) {
    this.elements = Array.from(context.querySelectorAll(selector));
    return this;
}
jQuery.prototype.each = function(fn) {
    this.elements.forEach((element, index) => fn.call(element, element, index));
    return this;
}

// Задание 1
// Написать метод jQuery.prototype.html(),
// который возвращает или изменяет html-содержимое выбранных элементов.

jQuery.prototype.html = function(newHtml) {
    if (newHtml) {
        this.each(element => element.innerHTML = newHtml);
        return this;
    }
    return this.elements[0].innerHTML;
}

const $ = (e) => new jQuery(e);

/*  Теперь можно заменять HTML-код внутри тега, заданного или именем самого
    тэга ('tag'), или именем атрибута id ('#id'), или именем класса ('.class'):

    $('sel').html('<b><u>New HTML code inside selected tag</u></b>')

    Метод без аргументов возвращает текущее содержимое, например:

    console.log($('sel').html())
    выводит в консоль HTML-содержимое внутренностей тэга.

    На крайний случай, если в задании подразумевалось возвращать или изменять
    не только внутренности тэга, а весь тэг целиком, тогда в методе надо
    заменить 'innerHTML' на 'outerHTML'. */
