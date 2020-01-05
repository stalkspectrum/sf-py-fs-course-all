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

// Задание 2
// Написать метод jQuery.prototype.text(),
// который возвращает или изменяет текстовое содержимое выбранных элементов.

jQuery.prototype.text = function(newText) {
    if (newText) {
        this.each(element => element.innerText = newText);
        return this;
    }
    else {
        console.log(this.elements[0].innerText);
    }
}

const $ = (e) => new jQuery(e);

/*  Теперь можно заменять текст внутри тега, заданного или именем самого
    тэга ('tag'), или именем атрибута id ('#id'), или именем класса ('.class'):

    $('sel').text('New text inside selected tag')

    Если метод без аргументов:
    $('sel').text()
    то в консоль выводится текстовое содержимое внутренностей тэга. */
