n/UFSXQvb7c_45LRd6SdzFTg "explain to **without the help of Google**:

### General

-   Why JavaScript programming is amazing
-   How to run a JavaScript script
-   How to create variables and constants
-   What are differences ` ` `let`
-   What are all the data types available in JavaScript
-   How to use ` `if ... statements
-   How to use comments
-   How to affect values to variables
-   How to ` ` loops
-   How to ` ` statements
-   What is a function and how do you use functions
-   What does a function that does not use ` statement return
-   Scope of variables
-   What are the arithmetic operators and how to use them
-   How to manipulate dictionary
-   How to import a file

Requirements
------------

### General

-   Allowed ` ` `emacs`
-   All your files will be interpreted on Ubuntu 20.04 LTS ` (version 14.x)
-   All your files should end with a new line
-   The first line of all your files should be `#!/usr/bin/node`
- `README. file, at the root of the folder of the project, is mandatory
-   Your code should ` compliant (version 16.x. [Rules of Standard](https://alx-intranet.hbtn.io/rltoken/1T1yg1vOAChRN20Yyz8crw "Rules [semicolons on top](https://alx-intranet.hbtn.io/rltoken/35q5Pc6A6KWPyd3kGeRQFg "semicolons on top"). Also as [AirBnB style](https://alx-intranet.hbtn.io/rltoken/ilo9MmB3u0utJZjZat-W3Q "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested `wc`

More Info
---------

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://alx-intranet.hbtn.io/rltoken/35q5Pc6A6KWPyd3kGeRQFg "Documentation")

```
$ sudo npm install semistandard --global

```

Quiz questions
--------------

Show

Tasks
-----

### 0\. First constant, first print

mandatory

Write a script that prints "JavaScript is amazing":

-   You must create a constant variable ` with the value "JavaScript is amazing"
-   You must `console. to print all output
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
JavaScript is amazing
guillaume@ubuntu:~/0x12$
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `0-javascript_is_amazing. Check your Get a sandbox

### 1\. 3 languages

mandatory

Write a script that prints 3 lines:

-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must `console. to print all output
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `1-multi_languages. Check your Get a sandbox

### 2\. Arguments

mandatory

Write a script that prints a message depending of the number of arguments passed:

-   If no arguments are passed to the script, print "No argument"
-   If only one argument is passed to the script, print "Argument found"
-   Otherwise, print "Arguments found"
-   You must `console. to print all output
-   You are not allowed to `var`

 [process.argv](https://alx-intranet.hbtn.io/rltoken/5kTYi3rxb6KM1_pivm-tXg "process.argv")

```
guillaume@ubuntu:~/0x12$ ./2-arguments.js
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `2-arguments. Check your code

### 3\. Value of my argument

mandatory

Write a script that prints the first argument passed to it:

-   If no arguments are passed to the script, print "No argument"
-   You must `console. to print all output
-   You are not allowed to `var`
-   You are not allowed to `length`

```
guillaume@ubuntu:~/0x12$ ./3-value_argument.js
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `3-value_argument. Check your code

### 4\. Create a sentence

mandatory

Write a script that prints two arguments passed to it, in the following "

-   You must `console. to print all output
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `4-concat. Check your Get a sandbox

### 5\. An Integer

mandatory

Write a script that `My number: <first argument converted in if the first argument can be converted to an integer:

-   If the argument can't be converted to an integer, print "Not a number"
-   You must `console. to print all output
-   You are not allowed to `var`
-   You are not allowed to `try/catch`

```
guillaume@ubuntu:~/0x12$ ./5-to_integer.js
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `5-to_integer. Check your code

### 6\. Loop to languages

mandatory

Write a script that prints 3 lines: ( `1-multi_languages.js`) but by using an array of string and a loop

-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must `console. to print all output
-   You are not allowed to `var`
-   You are not allowed to use `if/ statement
-   You can use only `console.log`
-   You must use a loop (` `for`, etc.)

```
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `6-multi_languages_loop. Check your Get a sandbox

### 7\. I love C

mandatory

Write a script that ` times "C is fun"

- ` is the first argument of the script
-   If the first argument can't be converted to an integer, print "Missing number of occurrences"
-   You must `console. to print all output
-   You are not allowed to `var`
-   You can use only `console.log`
-   You must use a loop (` `for`, etc.)

```
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `7-multi_c. Check your Get a sandbox

### 8\. Square

mandatory

Write a script that prints a square

-   The first argument is the size of the square
-   If the first argument can't be converted to an integer, print "Missing size"
-   You must use the ` to print the square
-   You must `console. to print all output
-   You are not allowed to `var`
-   You must use a loop (` `for`, etc.)

```
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `8-square. Check your code

### 9\. Add

mandatory

Write a script that prints the addition of 2 integers

-   The first argument is the first integer
-   The second argument is the second integer
-   You have to define a function with this `function add(a, b)`
-   You must `console. to print all output
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ ./9-add.js
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `9-add. Check your Get a sandbox

### 10\. Factorial

mandatory

Write a script that computes and prints a factorial

-   The first argument is integer (argument can be cast as integer) used for computing the factorial
-   Factorial ` `1`
-   You must do it recursively
-   You must use a function
-   You must `console. to print all output
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ ./10-factorial.js
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `10-factorial. Check your Get a sandbox

### 11\. Second biggest!

mandatory

Write a script that searches the second biggest integer in the list of arguments.

-   You can assume all arguments can be converted to integer
-   If no argument passed, `0`
-   If the number of arguments is 1, `0`
-   You must `console. to print all output
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `11-second_biggest. Check your code

### 12\. Object

mandatory

Update this script to replace the ` `89`:

-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `12-object. Check your Get a sandbox

### 13\. Add file

mandatory

Write a function that returns the addition of 2 integers.

-   The function must be visible from outside
-   The name of the function must `add`
-   You are not allowed to `var`

[Tip](https://alx-intranet.hbtn.io/rltoken/1k6VPdLchwtGubOfPyGL1Q "Tip")

```
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `13-add. Done?

### 14\. Const or not const

#advanced

 0. (Checks completed: 0.00%)

Write a file that modifies the value ` `333`

```
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$

```

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4ae30fb44f708dbb3abc211b784db614e615ca21.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220301%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220301T121514Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a1f02cfa1a04eae1b926f44e9a5b754a0ebf8e706a6b5f5be7f2445959cc4c4f)

Do you get it? Tweet! Post! Talk about it!

Hint: Scope

**This exercise doesn't ` so don't worry about it.

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `100-let_me_const. Check your QA Review

### 15\. Call me Moby

#advanced

 0. (Checks completed: 0.00%)

Write a function that ` times a function.

-   The function must be visible from outside
- `function (x, theFunction)`
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `101-call_me_moby. Check your Get a QA Review

### 16\. Add me maybe

#advanced

 0. (Checks completed: 0.00%)

Write a function that increments and calls a function.

-   The function must be visible from outside
- `function (number, theFunction)`
-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `102-add_me_maybe. Check your Get a QA Review

### 17\. Increment object

#advanced

 0. (Checks completed: 0.00%)

Update this script by adding a new ` that increments the `value`.

-   You are not allowed to `var`

```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$

```

**Repo:**

-   GitHub `alx-higher_level_programming`
- `0x12-javascript-warm_up`
- `103-object_fct.js`
