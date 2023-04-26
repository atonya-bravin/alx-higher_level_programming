#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Make a GET request to the Star Wars API with the movie ID
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
// Check for errors or non-200 status code
  if (error || response.statusCode !== 200) {
    console.error(`Error fetching movie data: ${error || response.statusCode}`);
    return;
  }
  // Parse the movie data from the response body
  const movie = JSON.parse(body);
  // Check if the episode number matches the given ID
  if (movie.episode_id === parseInt(movieId)) {
    console.log(`Title: ${movie.title}`);
  } else {
    console.log(`No movie found with ID ${movieId}`);
  }
});
