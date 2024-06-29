#!/usr/bin/node

const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (chr) {
    if (chr === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rec = '';
        for (let j = 0; j < this.width; j++) {
          rec += chr;
        }
        console.log(rec);
      }
    }
  }
};
