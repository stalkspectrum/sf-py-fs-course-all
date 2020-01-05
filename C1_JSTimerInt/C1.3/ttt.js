const content = document.querySelector(".testcontent");

function getRandomDog (breed) {
    fetch(`https://dog.ceo/api/breed/${breed}/images/random`)
    .then(function(response) {
        return response.json();
    })
    .then(function(response) {
        content.innerHTML = `<img src="${response.message}" alt="dog">`;
    })
}

getRandomDog('briard')
