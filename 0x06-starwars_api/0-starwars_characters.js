#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv.slice(2);

const getData = (list1, index) => {
  request.get(list1[index], (error, response, body) => {
    const ListSize = list1.length;

    if (error) throw error;
    const ReturnValue = JSON.parse(body);
    console.log(ReturnValue.name);

    if (index < (ListSize - 1)) {
      getData(list1, (index + 1));
    }
  });
};

request.get(url, (error, response) => {
  if (error) console.log(error);
  else {
    const list2 = JSON.parse(response.body);
    getData(list2.characters, 0);
  }
});
