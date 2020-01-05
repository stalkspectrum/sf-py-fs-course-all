// Написать метод jQuery.prototype.html(),
// который возвращает или изменяет html-содержимое выбранных элементов.

function jQuery (selector, context = document) {
    this.elements = Array.from(context.querySelectorAll(selector));
    return this;
}

jQuery.prototype.each = function(fn) {
    this.elements.forEach((element, index) => fn.call(element, element, index));
    return this;
}

jQuery.prototype.click = function(fn) {
    this.each(element => element.addEventListener('click', fn));
    return this;
}

jQuery.prototype.remove = function() {
    this.each(element => element.remove());
    return this;
}

jQuery.prototype.html = function(newHtml) {
    if (newHtml) {
        this.each(element => element.innerHTML = newHtml);
        return this;
    }
    else return this.elements[0].innerHTML;
}

jQuery.prototype.text = function(newText) {
    if (newText) {
        this.each(element => element.innerText = newText);
        return this;
    }
    else return this.elements[0].innerText;
}
