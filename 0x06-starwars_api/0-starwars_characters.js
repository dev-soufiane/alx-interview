#!/usr/bin/env node

const request = require('request');

// Retrieve movie ID from command line argument
const movieId = process.argv[2];

// Construct the URL for fetching movie data
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch and print character names
function printCharacterNames(movieId) {
    // Make a GET request to fetch movie data
    request(apiUrl, function(error, response, body) {
        if (!error && response.statusCode === 200) {
            // Parse movie data JSON
            const movieData = JSON.parse(body);
            // Extract characters array from movie data
            const characters = movieData.characters;

            // Recursive function to fetch and print character names
            function fetchAndPrint(index) {
                if (index >= characters.length) {
                    return; // Exit recursion if all characters are printed
                }

                const characterUrl = characters[index];
                // Make a GET request to fetch character data
                request(characterUrl, function(error, response, body) {
                    if (!error && response.statusCode === 200) {
                        // Parse character data JSON
                        const characterData = JSON.parse(body);
                        // Print the name of the character
                        console.log(characterData.name);
                        // Recursively fetch next character
                        fetchAndPrint(index + 1);
                    } else {
                        console.error(`Failed to fetch character data for ${characterUrl}`);
                    }
                });
            }

            // Start fetching characters from the first index
            fetchAndPrint(0);
        } else {
            console.error(`Failed to fetch movie data for Movie ID ${movieId}`);
        }
    });
}

// Check if Movie ID is provided
if (!movieId) {
    console.error('Please provide a valid Movie ID as a command line argument.');
} else {
    // Call function to print character names for the provided Movie ID
    printCharacterNames(movieId);
}
