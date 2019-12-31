# PytchScript
Pytch is a scripting language made for people who like both batch and python.

#### [Getting started](https://github.com/BatchSource/Pytch/blob/master/README.md#getting-started-1)

[`Installation`](https://github.com/BatchSource/Pytch/blob/master/README.md#installation) [`Getting Started`](https://github.com/BatchSource/Pytch/blob/master/README.md#getting-started-1) [`Console`](https://github.com/BatchSource/Pytch/blob/master/README.md#console) [`Start.bat`](https://github.com/BatchSource/Pytch/blob/master/README.md#Console)

#### [Variables, Input, and Output](https://github.com/BatchSource/Pytch/blob/master/README.md#variables-input-and-output-1)

[`Variables`](https://github.com/BatchSource/Pytch/blob/master/README.md#variables) [`Output`](https://github.com/BatchSource/Pytch/blob/master/README.md#output) [`Wait`](https://github.com/BatchSource/Pytch/blob/master/README.md#wait) [`Pause`](https://github.com/BatchSource/Pytch/blob/master/README.md#pause) [`Write`](https://github.com/BatchSource/Pytch/blob/master/README.md#write) [`Writing\calling file`](https://github.com/BatchSource/Pytch/blob/master/README.md#writingcalling-a-file) [`Title`](https://github.com/BatchSource/Pytch/blob/master/README.md#title) [`Spacing`](https://github.com/BatchSource/Pytch/blob/master/README.md#spacing) [`Input`](https://github.com/BatchSource/Pytch/blob/master/README.md#input)

#### [Logic, Comments, and Misc](https://github.com/BatchSource/Pytch/blob/master/README.md#logic-comments-and-misc-1)

[`Comments`](https://github.com/BatchSource/Pytch/blob/master/README.md#comments) [`Goto`](https://github.com/BatchSource/Pytch/blob/master/README.md#goto) [`If statements`](https://github.com/BatchSource/Pytch/blob/master/README.md#if-statements) [`If statements (multiple lines)`](https://github.com/BatchSource/Pytch/blob/master/README.md#if-statements-with-multiple-lines) [`Input`](https://github.com/BatchSource/Pytch/blob/master/README.md#input) [`If, and, else, or`](https://github.com/BatchSource/Pytch/blob/master/README.md#if-and-else-or) [`Random`](https://github.com/BatchSource/Pytch/blob/master/README.md#random) [`Integer Operatons`](https://github.com/BatchSource/Pytch/blob/master/README.md#integer-operations) [`Float Operations`](https://github.com/BatchSource/Pytch/blob/master/README.md#float-operations) [`For loops`](https://github.com/BatchSource/Pytch/blob/master/README.md#for-loops)

----------------------

## Installation

Clone the repository and unzip it somewhere in your desktop. That folder will contain all the necessary files to run and compile a Pytch file.

## Getting Started
So now you have Pytch in your desktop, but now what? We don't have any code written for it so lets write something simple, a hello world program!

Go ahead and open your favorite text editor. Go ahead and type in the following:
```
say Hello, World!
```
Now save it as a .pytch file.

To run the file go ahead and open up Command Prompt and cd into the directory where Pytch.py is located, in this case we extracted it into our desktop, so lets cd into the directory.
```
cd C:\Users\Pytch\Desktop\PytchScript-master\
```
Now to run it. Go ahead and type in the following:
```
python Pytch.py -r "<path to the pytch file>"
```
Replace <path to the pytch file> with the path of the file. So if we have the Pytch file in our desktop, then it would be:
```
python Pytch.py -r "C:\Users\Pytch\Desktop\file.pytch"
```
As soon as you press enter, you should see the following:
```
Hello, World!
```
Great, you created your first Pytch program! The next sections will teach you more about the commands and syntax, and different build options for Pytch.

### Console
You can activate the console by doing:
```
python Pytch.py --console
```
However, you cannot use goto in the the Pytch console.

### Start.bat
If you don't want to activate the terminal every time you want to run a file, you can click and drag the `.pytch` file over `start.bat` in explorer.
You can open the console just by normally double-clicking `start.bat` in explorer.

## Variables, Input, and Output
### Variables
Variables can be declared like this:
```
set <variable name> = <value>
```
Go ahead and replace <variable name> to the name of the variable. And also <value> to a value. I'm gonna also add that the following will work the same way:

```
set myVar to 10
set myVar = 10
var myVar to 10
var myVar = 10
```
All those will create a variable called myVar and set their value to 10. To change a variables value that has already been declared, its the same syntax:
```
set myVar = 10
set myVar = 20
```
You can also undefine a variable by doing either of these:
```
set myVar undefine
set myvar remove
```

### Output
Now for output. To output, all you do is:
```
say <text>
```
Replace text with whatever you want, or leave it like that, nothing is stopping you.
```
say This is the say command in Pytch!
```
That outputs:
```
This is the say command in Pytch!
```
To output a variable:
```
set myVar = 10
say The value of myVar is [myVar]!
```
Which outputs:
```
The value of myVar is 10!
```
A simple way to create a blank line is:
```
say lol
say.
say lol
```
Outputs:
```
lol

lol
```

Cls/clear can be used like this:
```
clear
```
Or:
```
cls
```

### Wait
Wait for a specific amount of miliseconds.
For example,
```
wait 1000
```
This will wait for 1000 miliseconds, or one whole second.

### Pause
This will pause the script, similar to `pause` from batch.
```
pause
```
This will pause and say "Press any key to continue . . . "
If we add nul at the end,
```
pause nul
```
This will pause and not say anything, similar to pause >nul from batch.

### Write
Similar to say, this prints to the console. However, write will write in the same line.
```
write Hello,
write how are you?
```
The output will be
```
Hello, how are you?
```

### Writing/calling a file
We can also use write.file to append lines to a file.
Doing this, we can create saves.
Set a variable to the file location when there is a space in the file path so it is in the same element.
```
set fileLocation = C:\Test Files\Cache.pytch
write.file [fileLocation] set levelUnlocked = True
```
We can now call this file by doing:
```
call [fileLocation]
```
Don't forget, a goto command inside a file will not look for labels in any other files.

### Title
You can title a Pytch script by running:
```
title Hello
```
This will title the prompt Hello.

### Spacing
Pytch is designed be an "oops proof" language, meaning that it is not very picky about how you write. 
Some examples of this are
- Pytch doesn't care when there is extra elements at the end of a command. For example, `clear` and `clear abc123` does the exact same thing.
- There are many different  ways you can write commands. For example in if statements, `equ`, `equals`, `==`, `is`, and `=`, are all valid operators of if.
- Pytch is only cares about CAPS LOCK in variable names and labels. Everything else doesn't matter.
- Pytch doesn't care if there are multiple spaces in a command:

In Pytch, the spacing between words do not matter.
For example if we had:
```
var color input What is your favorite color?:
if [color] = red      cmd color 04
if [color] = green    cmd color 0a
if [color] = yellow   cmd color 0e
if [color] = blue     cmd color 0b
```
The if statements will work normally.


### Input
For input, all you have to do is this:
`set <varname> input <prompt>`
You can replace `<varname>` with the name of the variable you are trying to replace and `<prompt>` with a prompt you want to show.

For example:
```
set userInput input Input:
say The user typed in "[userInput]"!
```
Which outputs:
```
Input: input test
The user typed in "input test"!
```
I typed in "input test" and it outputted that.
## Logic, Comments, and Misc
### Comments
To comment code, all you do is this:
```
# This is a comment, it will not be ran.
```
Comments include `::`, `#`, and `//`.
You can also add comments to the end of lines and they will be ignored.
For example:
```
say This is a test. # This is a comment.
```

### Goto
If you are familiar with batch, then you are familiar with this:
```
:myLabel
echo Test
goto myLabel
```
All that does is output "Test" forever. Now to do goto in Pytch, all you do is:
```
label myLabel
say Test
goto myLabel
```
It outputs the exact same thing as what it is in batch:
```
Test
Test
Test
Test
Test
...
```
### If statements
If statements can be declared like this:
```
if <value1> <operator> <value2> <code to run>
```
Some examples of this are:
```
set var1 = 10
set var2 = 20
if 10 = 10 write 1
if 10 = 20 write 2
if 10 > 5 write 3
if 50 < 10 write 4
if 50 != 40 write 5
if 50 >= 50 write 6
if 10 >= 4 write 7
if [var1] = 10 write 8
if [var1] = [var2] write 9
```
Which outputs:
```
1 3 5 6 7 8
```
Valid operators are:
```
=, ==, EQU, is, equals
>, GTR
<, LSS
!=, NOT
>=, GEQ, =>
<=, LEQ, =<
```
We also can use '&' to simulate a space without creating extra elements.
For example:
```
set password input What is the secret code?:
if [password] = super&man&123 say Correct!
```
If the input for the "password" variable is "super man 123", the if statement be correct.
This doesn't work in file paths when calling and writing files, though.

You can also use `if.sensitive` or `if.cs` to make if statements picky on case sensitivity. For example:
```
if True = true say 123
```
This will output `123` because the case does not matter. However, if you do:
```
if.cs True = true say 123
```
It will not output anything because there is a caps difference in `True` and `true`.

To use compare integers with if statements, you can use `if.int` or `if.integer`.
For example:
```
if [int1] > [int2] say Hello
```
This will compare the variables `int1` and `int2`.

### If statements with multiple lines
We can create if statements with mutiple commands by doing:
```
if [var1] = [var2] (
  say [var1] is equal to [var2].
  say [var1] is var1 and [var2] is var2.
)
```
We can also created nested if statements by doing
```
if [var1] = [var2] if [var2] = [var3] say var1 is equal to var2 is equal to var3
```
OR
```
if [var1] = [var2] (
    if [var2] = [var3] (
        say var1 is equal to var2 is equal to var3
    )
)
```

### If and, else, or.
For AND, we can use nested if statements.
```
set var1 to hello
set var2 to cool

if [var1] = hello if [var2] = cool say CORRECT.
```
For OR, we we can use multiple if statements.
```
set var1 to hello
set var2 to cool

if [var1] = hello   say CORRECT
if [var2] = cool    say CORRECT.
```
For ELSE, we can use NOT.
```
set var1 to hello

if [var1] =   hello   say CORRECT
if [var1] NOT hello   say INCORRECT
```

### Random
This sets a random to be in a range from 1 to a number.

For example:
```
random myVar 50
```
This will set the variable "myVar" to be a random number between 1 and 50.

### Integer Operations
This is used to set an variable to do math.
Valid operators are:
```
*, /, -, +
```
And
```
*=, /=, -=, +=
```

For example:
```
int myVar = 10 + 10
```
This will set the variable "myVar" to be 20, the sum of 10 and 10.
You can also do:
```
int myVar += 1
```
To add 1 to the variable "myVar".

### Float Operations
You can also use floats to have decimals.
```
float myVar = 2 / 3
````
will set myVar to 0.666666...

```
float myVar += 0.0001
```
will add .0001 to myVar.

### For loops
For is not a function of this language, but for loops can be simulated like this:
```
set var = 0
label loop
int var += 1
// Code here

say Hello

// :::::::::
if [var] = 100 goto escloop
goto loop
label escloop
```
This will say Hello 100 times.
