#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  let secondBiggest = 0;
  let biggest = argv[2];
  for (let i = 3; i < argv.length; i++) {
    if (argv[i] > biggest) {
      secondBiggest = biggest;
      biggest = argv[i];
    }
  }
  console.log(secondBiggest);
}
