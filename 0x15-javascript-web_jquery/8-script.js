$('document').ready(
	function getCharacterName(){
		fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
			.then(response => response.json())
			.then(data =>{
				let movies = data.results;
				let titles = movies.map(movie => movie.title);
				titles.forEach(title => {
					let list_element = $('<li></li>').text(title);
					$('UL#list_movies').append(list_element);})})
			.catch(error => console.error(error));
	}
);
