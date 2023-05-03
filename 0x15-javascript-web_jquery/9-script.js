$('document').ready(
	function getCharacterName(){
		let hello_value;
		fetch('https://fourtonfish.com/hellosalut/?lang=fr')
		.then(response => response.json())
		.then(data => hello_value = data.hello)
		.catch(error => console.error(error));
		$('#hello').text(hello_value);
	}
);
