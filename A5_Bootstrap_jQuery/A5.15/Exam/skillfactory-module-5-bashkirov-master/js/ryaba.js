const dataURL = "https://api.myjson.com/bins/jcmhn";
const fields = [
	"var1",
	"var2",
	"var3",
	"var4",
	"var5",
	"var6",
	"speach"
]

function getFormValues() {
	let obj = {};

	fields.forEach(function(field) {
		obj[field] = $("input[name=" + field + "]")[0].value
	});

	return obj;
}

function handleButton(event) {
	$.getJSON(dataURL, handleData);
	$("form").hide();

	event.preventDefault();
}

function handleData(data) {
	let message = "";

	let values = getFormValues();

	data["text"].forEach(function(line) {
		for (key in values) {
			line = line.replace("{" + key + "}", values[key]);
			// line = line.replace(`{${key}}`, values[key]);
		}

		message = message + line + "<BR>";
	});

    $("div#result").html(message);
}

function init() {
	$("#button-fetch").click(handleButton);
}

$(document).ready(init);