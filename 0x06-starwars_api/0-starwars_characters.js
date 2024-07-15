#!/usr/bin/env node

const request = require('request');

// Retrieve movie ID from command line argument
const movieId = process.argv[2];

// URL for fetching movie data
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch and print character names
function printCharacterNames(movieId) {
    // Make a GET request to fetch movie data
    request(apiUrl, function(error, response, body) {
        if (!error && response.statusCode === 200) {
            const movieData = JSON.parse(body);
            const characters = movieData.characters;

            // Recursive function to print character names
            function fetchAndPrint(index) {
                if (index >= characters.length) {
                    return; // Exit if all characters are printed
                }

                const characterUrl = characters[index];
                // Make a GET request to fetch character data
                request(characterUrl, function(error, response, body) {
                    if (!error && response.statusCode === 200) {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                        fetchAndPrint(index + 1); // Recursively fetch next character
                    } else {
                        console.error(`Failed to fetch character data for ${characterUrl}`);
                    }
                });
            }

            fetchAndPrint(0); // Start fetching from the first character
        } else {
            console.error(`Failed to fetch movie data for Movie ID ${movieId}`);
        }
    });
}

// Check if Movie ID is provided
if (!movieId) {
    console.error('Please provide a valid Movie ID as a command line argument.');
} else {
    printCharacterNames(movieId);
}
