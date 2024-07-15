#!/usr/bin/env node

const request = require('request');

// Retrieve movie ID from command line argument
const movieId = process.argv[2];

// Define the API URL for fetching movie data
const apiUrl = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + movieId,
  method: 'GET'
};

// Make a GET request to retrieve the movie data
request(apiUrl, function (error, response, body) {
  if (!error) {
    // Parse the response body to extract character URLs
    const characterUrls = JSON.parse(body).characters;
    // Start printing character names
    printCharacterNames(characterUrls, 0);
  }
});

// Recursive function to print the characters' names
function printCharacterNames(urls, index) {
  // Make a GET request for each character URL
  const characterUrl = urls[index];
  request(characterUrl, function (error, response, body) {
    if (!error) {
      // Parse character data JSON to extract character's name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      // Check if there are more character URLs to fetch and print
      if (index + 1 < urls.length) {
        // Recursively print names of subsequent characters
        printCharacterNames(urls, index + 1);
      }
    }
  });
}
