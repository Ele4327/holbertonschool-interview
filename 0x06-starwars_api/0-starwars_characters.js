#!/usr/bin/node

const URL = 'https://swapi-api.hbtn.io/api/';
const request = require('request');
const idMovie = process.argv[2];

async function getRequest (url) {
  return new Promise(function (resolve, reject) {
    request.get(url, function (err, resp, body) {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

(async () => {
  return getRequest(URL + 'films/' + idMovie);
})().then(async (movie) => {
  if (movie.detail !== 'Not found') {
    for (const ConstCharacter of movie.characters) {
      const Character = await getRequest(ConstCharacter);
      if (Character.detail === undefined) {
        console.log(Character.name);
      }
    }
  }
});
