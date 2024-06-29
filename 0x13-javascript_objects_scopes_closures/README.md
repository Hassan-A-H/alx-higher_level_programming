 [Class - ES6](https://alx-intranet.hbtn.io/rltoken/NEm-UViCThD5hfq_3Lj9Hg "Class - ES6")
 -   [super - ES6](https://alx-intranet.hbtn.io/rltoken/_cxdVKsdqPWbbp2cHtQSbQ "super - ES6")
 -   [extends - ES6](https://alx-intranet.hbtn.io/rltoken/6wdl6Bc5yjBplpiZKmr6Zw "extends - ES6")
 -   [Object prototypes](https://alx-intranet.hbtn.io/rltoken/NiBbDiOlfhfUf4eIigglIw "Object prototypes")
 -   [Inheritance in JavaScript](https://alx-intranet.hbtn.io/rltoken/qqgqdyHPzUZkKQ5UMnw2MQ "Inheritance in JavaScript")
 -   [Closures](https://alx-intranet.hbtn.io/rltoken/CybTMKEDNdTdU99kx_OXgQ "Closures")
 -   [this/self](https://alx-intranet.hbtn.io/rltoken/XcOkisoKPud4faDDkLMABw "this/self")
 -   [Modern JS](https://alx-intranet.hbtn.io/rltoken/rU_q2J3qGWfvTYNllW8JnA "Modern JS")

Learning Objectives
-------------------

At the end of this project, you are expected to be able [explain to anyone](https://alx-intranet.hbtn.io/rltoken/Eo6JxX0bkDywq4IxT8wRew "explain to **without the help of Google**:

### General

-   Why JavaScript programming is amazing
-   How to create an object in JavaScript
- ` means
- ` means
-   Why the variable type and scope is important
-   What is a closure
-   What is a prototype
-   How to inherit an object from another

Requirements
------------

### General

-   Allowed ` ` `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
-   All your files should end with a new line
-   The first line of all your files should be `#!/usr/bin/node`
- `README. file, at the root of the folder of the project, is mandatory
-   Your code should ` [Rules of Standard](https://alx-intranet.hbtn.io/rltoken/CAKkGG6pUDtpu3T2rn4MXw "Rules [semicolons on top](https://alx-intranet.hbtn.io/rltoken/oc1-9XTUtCiIyZkdAFvoUQ "semicolons on top"). Also as [AirBnB style](https://alx-intranet.hbtn.io/rltoken/JvqqQQrEPtGjP-57CZSEaQ "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested `wc`
-   You are not allowed to `var`

More Info
---------

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://alx-intranet.hbtn.io/rltoken/oc1-9XTUtCiIyZkdAFvoUQ "Documentation")

```
$ sudo npm install semistandard --global

```

Quiz questions
--------------

Show

Tasks
-----

### 0\. Rectangle #0

mandatory

Write an empty ` that defines a rectangle:

-   You must use ` notation for defining your class

```
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Function: Rectangle]
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `0-rectangle. Check your Get a sandbox

### 1\. Rectangle #1

mandatory

Write a ` that defines a rectangle:

-   You must use ` notation for defining your class
-   The constructor must take 2 ` `h`
-   Initialize the instance ` with the value `w`
-   Initialize the instance ` with the value `h`

```
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `1-rectangle. Check your Get a sandbox

### 2\. Rectangle #2

mandatory

Write a ` that defines a rectangle:

-   You must use ` notation for defining your class
-   The constructor must take 2 ` `h`
-   Initialize the instance ` with the value `w`
-   Initialize the instance ` with the value `h`
- ` ` is equal to 0 or not a positive integer, create an empty object

```
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `2-rectangle. Check your Get a sandbox

### 3\. Rectangle #3

mandatory

Write a ` that defines a rectangle:

-   You must use ` notation for defining your class
-   The constructor must take 2 ` `h`
-   Initialize the instance ` with the value `w`
-   Initialize the instance ` with the value `h`
- ` ` is equal to 0 or not a positive integer, create an empty object
-   Create an instance method ` that prints the rectangle using the `X`

```
guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `3-rectangle. Check your Get a sandbox

### 4\. Rectangle #4

mandatory

Write a ` that defines a rectangle:

-   You must use ` notation for defining your class
-   The constructor must take 2 ` `h`
-   Initialize the instance ` with the value `w`
-   Initialize the instance ` with the value `h`
- ` ` is equal to 0 or not a positive integer, create an empty object
-   Create an instance method ` that prints the rectangle using the `X`
-   Create an instance method ` that exchanges ` and ` of the rectangle
-   Create an instance method ` that multiples ` and ` of the rectangle by 2

```
guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `4-rectangle. Check your Get a sandbox

### 5\. Square #0

mandatory

Write a ` that defines a square and inherits ` `4-rectangle.js`:

-   You must use ` notation for defining your class `extends`
-   The constructor must take 1 `size`
-   The constructor ` must be called (by `super()`)

```
guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `5-square. Check your Get a sandbox

### 6\. Square #1

mandatory

Write a ` that defines a square and inherits ` `5-square.js`:

-   You must use ` notation for defining your class `extends`
-   Create an instance method `charPrint( that prints the rectangle using the `c`
    - ` `undefined`, use the `X`

```
guillaume@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `6-square. Check your Get a sandbox

### 7\. Occurrences

mandatory

Write a function that returns the number of occurrences in a list:

- `exports.nbOccurences = function (list, searchElement)`

```
guillaume@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));

guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `7-occurrences. Check your code

### 8\. Esrever

mandatory

Write a function that returns the reversed version of a list:

- `exports.esrever = function (list)`
-   You are not allow to use the built-in `reverse`

```
guillaume@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["School", 89, { id: 12 }, "String"]));

guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `8-esrever. Check your Get a sandbox

### 9\. Log me

mandatory

Write a function that prints the number of arguments already printed and the new argument value. (see example below)

- `exports.logMe = function (item)`
-   Output `<number arguments already printed>: <current argument value>`

```
guillaume@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Best");
logMe("School");

guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Best
2: School
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `9-logme. Check your code

### 10\. Number conversion

mandatory

Write a function that converts a number from base 10 to another base passed as argument:

- `exports.converter = function (base)`
-   You are not allowed to import any file
-   You are not allowed to declare any new variable (` `let`, etc..)

```
guillaume@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x13-javascript_objects_scopes_closures`
- `10-converter.js`


