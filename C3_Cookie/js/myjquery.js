// Функция-конструктор и необходимые методы,
// как локальный заменитель jQuery

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
    return this
}

jQuery.prototype.hide = function() {
    this.each(element => element.style.display = 'none');
    return this;
}

jQuery.prototype.show = function() {
    this.each(element => element.style.display = '');
    return this;
}

jQuery.prototype.html = function(newHtml) {
    if (newHtml) {
        this.each(element => element.outerHTML = newHtml);
        return this;
    }
    return this.elements[0].outerHTML;
}

jQuery.prototype.text = function(newText) {
    if (newText) {
        this.each(element => element.innerText = newText);
        return this;
    }
    return this.elements[0].innerText;
}

jQuery.prototype.class = function(cName) {
    this.each(element => element.className = cName);
    return this;
}

jQuery.prototype.getattrib = function(aName) {
    this.each(element => element.getAttribute(aName));
    return this;
}

jQuery.prototype.setattrib = function(aName, aValue) {
    this.each(element => element.setAttribute(aName, aValue));
    return this;
}

jQuery.prototype.remattrib = function(aName) {
    this.each(element => element.removeAttribute(aName));
    return this;
}

const $ = (e) => new jQuery(e);
