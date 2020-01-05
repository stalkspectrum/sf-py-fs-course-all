const minS = document.querySelector(".minutes");
const secS = document.querySelector(".seconds");

let countMinS = 0;
let countSecS = 0;

const updateText = () => {
    minS.innerHTML = (0 + String(countMinS)).slice(-2);
    secS.innerHTML = (0 + String(countSecS)).slice(-2);
}

updateText();
