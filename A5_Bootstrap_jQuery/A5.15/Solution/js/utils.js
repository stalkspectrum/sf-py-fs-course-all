function getFormValues() {
	let formValues = $("form").serializeArray();
	let obj = {};
	for (let i = 0; i < formValues.length; i++) {
		obj[formValues[i]["name"]] = formValues[i]["value"];
	}
	return obj;
}
