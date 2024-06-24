#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  let secondBiggest = Number.MIN_SAFE_INTEGER;
  let biggest = Number(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    const num = Number(argv[i]);
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num < biggest) {
      secondBiggest = num;
    }
  }
  console.log(secondBiggest);
}
