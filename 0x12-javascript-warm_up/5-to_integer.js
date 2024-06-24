#!/usr/bin/node

const { argv } = require('node:process');

const x = Number(argv[2]);
if (Number.isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + x);
}
