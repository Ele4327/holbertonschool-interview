#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const GetData = (list, index) => {
  request.get(list[index], (error, res, body) => {
    const ListSize = list.length;

    if (error) throw error;
    const ReturnValue = JSON.parse(body);
    console.log(ReturnValue.name);

    if (index < (ListSize - 1)) {
      GetData(list, (index + 1));
    }
  });
};

request.get(url, async (error, res) => {
  if (error) console.log(error);
  else {
    const list = JSON.parse(res.body);
    GetData(list.characters, 0);
  }
});
