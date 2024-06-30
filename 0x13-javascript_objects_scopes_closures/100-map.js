#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((el, index) => el * index);

console.log(list);
console.log(newList);
