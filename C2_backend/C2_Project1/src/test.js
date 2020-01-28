const header = new Headers({
    'Access-Control-Allow-Credentials': true,
    'Access-Control-Allow-Origin': '*'
});
const progress = document.querySelector('.progress-bar');
const url = new URL('https://sf-pyw.mosyag.in/sse/stream-randoms');
const ES = new EventSource(url, header);
/*ES.onopen = event => {
    console.log(event);
};*/
ES.onerror = error => {
    ES.readyState
    ? progress.textContent = 'Strange Error'
    : null;
};
ES.onmessage = message => {
    progress.style.cssText = `width: ${message.data}%`;
    progress.textContent =`${message.data}%`
};
