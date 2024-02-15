#!/usr/bin/node
/**
 * Starwars Characters
 */

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (error, res, body) => {
   if (error) console.log(err);
   const index = 0;
   const characters = JSON.parse(body).characters;
   printMovieCharacter(characters, index);
});

const printMovieCharacter = (url, i) => {
    request(url[i], (err, res, body) => {
        if (err) console.log(err);
        console.log(JSON.parse(body).name);
        if (++i < url.length) {
          printMovieCharacter(url, i++);
        }
      });
}
