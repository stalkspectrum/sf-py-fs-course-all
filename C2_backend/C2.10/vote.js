const postURL = new URL('https://sf-pyw.mosyag.in/sse/vote/');
let postVoteForPets = new XMLHttpRequest();

function postVoteFor(petName) {
    postVoteForPets.open('POST', postURL + petName, true);
    postVoteForPets.send('');
};

$('#vote-cats').click(function() { postVoteFor('cats') });
$('#vote-dogs').click(function() { postVoteFor('dogs') });
$('#vote-parrots').click(function() { postVoteFor('parrots') });
