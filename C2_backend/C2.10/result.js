const header = new Headers({
    'Access-Control-Allow-Credentials': true,
    'Access-Control-Allow-Origin': '*'
});
const catsResult = document.querySelector('#cats-result-bar');
const dogsResult = document.querySelector('#dogs-result-bar');
const parrotsResult = document.querySelector('#parrots-result-bar');
const urlResult = new URL('https://sf-pyw.mosyag.in/sse/vote/stats');
const streamResult = new EventSource(urlResult, header);
streamResult.onopen = event => {
    console.log(event);
};
streamResult.onmessage = message => {
    let messageDict = JSON.parse(message.data)
    let maxResult = Math.max(messageDict.cats, messageDict.dogs, messageDict.parrots);
    /*let catsPcWidth = integer();*/
    catsResult.style.cssText = `width: ${messageDict.cats}px`;
    catsResult.textContent = `${messageDict.cats}`;
    dogsResult.style.cssText = `width: ${messageDict.dogs}px`;
    dogsResult.textContent = `${messageDict.dogs}`;
    parrotsResult.style.cssText = `width: ${messageDict.parrots}px`;
    parrotsResult.textContent = `${messageDict.parrots}`;
};
