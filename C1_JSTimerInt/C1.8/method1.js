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

jQuery.prototype.html = function(newText) {
    if (newText) {
        this.each(element => element.innerHTML = newText);
        return this;
    }
    else {
        //console.log(this.elements[0].innerHTML);
        console.log(this.elements[0].innerHTML);
    }
}

jQuery.prototype.text = function(newText) {
    if (newText) {
        this.each(element => element.innerText = newText);
        return this;
    }
    else {
        //const strr = this.elements[0].innerHTML;
        console.log(this.elements[0].innerText);
    }
}

/*
const but = document.querySelector('button');

function main(selector) {
    this.element = document.querySelector(selector);
    return this
}

main.prototype.click = function(fn) {
    this.element.addEventListener('click', fn);
    return this
}

main.prototype.disable = function() {
    this.element.disabled = true;
    return this
}

const $ = (e) => new jQuery(e);
$('button').click(e => console.log(e.target));
*/
