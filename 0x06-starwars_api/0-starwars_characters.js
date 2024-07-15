#!/usr/bin/node
// Script to print all characters of a Star Wars movie

const request = require('request');
const filmId = process.argv[2]; // Retrieve movie ID from command line argument

const apiUrl = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + filmId,
  method: 'GET'
};

// Make a GET request to fetch the movie data
request(apiUrl, function (error, response, body) {
  if (!error) {
    // Extract characters from the movie data
    const characters = JSON.parse(body).characters;
    printCharacterNames(characters, 0); // Initiate printing of character names
  }
});

// Recursive function to print characters' names
function printCharacterNames(characters, index) {
  // Make a GET request for each character URL
  const characterUrl = characters[index];
  request(characterUrl, function (error, response, body) {
    if (!error) {
      // Extract character's name from the response data
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      // Check if there are more characters to print
      if (index + 1 < characters.length) {
        // Recursively print with the next character index
        printCharacterNames(characters, index + 1);
      }
    }
  });
}
