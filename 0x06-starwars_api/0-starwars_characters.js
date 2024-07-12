#!/usr/bin/node

const request = require('request');

const movieNum = process.argv[2] + '/';
const movieURL = 'https://swapi-api.hbtn.io/api/films/';

request(movieURL + movieNum, async function (err, res, body) {
  if (err) return console.error(err);

  const charURLList = JSON.parse(body).characters;

  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
