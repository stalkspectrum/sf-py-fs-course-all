function getCookie(name) {
    let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options = {}) {
    options = {
        'path': '/',
        'max-age': 3600,
        'secure': false,
        'expires': 'Wed, 29 Jan 2020 21:00:00 GMT'
        //uname: 'newcookie',
        //...options
    };

    if (options.expires.toUTCString) {
        options.expires = options.expires.toUTCString();
    }
    let updatedCookie = encodeURIComponent(name) + '=' + encodeURIComponent(value);
    for (let optionKey in options) {
        updatedCookie += '; ' + optionKey;
        let optionValue = options[optionKey];
        if (optionValue !== true) {
            updatedCookie += '=' + optionValue;
        }
    }
    document.cookie = updatedCookie;
}

function deleteCookie(name) {
    setCookie(name, '', {'max-age': -1})
}
