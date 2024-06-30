#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newObj = {};
for (const key in dict) {
  if (newObj[dict[key]] === undefined) {
    newObj[dict[key]] = [key];
  } else {
    newObj[dict[key]].push(key);
  }
}
console.log(newObj);

