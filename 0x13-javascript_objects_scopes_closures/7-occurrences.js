#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let repeat = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      repeat += 1;
    }
  }
  return repeat;
};
