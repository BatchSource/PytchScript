# PytchScript
Pytch is a scripting language design to be for absolute begineers.

# [Download v2.2](https://www.dropbox.com/s/mseq9a6jpzefjeh/Pytch22.exe?dl=1)

#### [Getting started](https://github.com/BatchSource/PytchScript/blob/master/README.md#getting-started-1)

[`Installation`](https://github.com/BatchSource/PytchScript/blob/master/README.md#installation) [`Getting Started`](https://github.com/BatchSource/PytchScript/blob/master/README.md#getting-started-1) [`Console`](https://github.com/BatchSource/PytchScript/blob/master/README.md#console) [`Start.bat`](https://github.com/BatchSource/PytchScript/blob/master/README.md#Console)

#### [Variables, Input, and Output](https://github.com/BatchSource/PytchScript/blob/master/README.md#variables-input-and-output-1)

[`Variables`](https://github.com/BatchSource/PytchScript/blob/master/README.md#variables) [`Output`](https://github.com/BatchSource/PytchScript/blob/master/README.md#output) [`Wait`](https://github.com/BatchSource/PytchScript/blob/master/README.md#wait) [`Beep`](https://github.com/BatchSource/PytchScript/blob/master/README.md#beep) [`Pause`](https://github.com/BatchSource/PytchScript/blob/master/README.md#pause) [`Write`](https://github.com/BatchSource/PytchScript/blob/master/README.md#write) [`Writing\calling file`](https://github.com/BatchSource/PytchScript/blob/master/README.md#writingcalling-a-file) [`Title`](https://github.com/BatchSource/PytchScript/blob/master/README.md#title) [`Spacing`](https://github.com/BatchSource/PytchScript/blob/master/README.md#spacing) [`TTS`](https://github.com/BatchSource/PytchScript/blob/master/README.md#tts) [`Input`](https://github.com/BatchSource/PytchScript/blob/master/README.md#input)

#### [Logic, Comments, and Misc](https://github.com/BatchSource/PytchScript/blob/master/README.md#logic-comments-and-misc-1)

[`Comments`](https://github.com/BatchSource/PytchScript/blob/master/README.md#comments) [`Goto`](https://github.com/BatchSource/PytchScript/blob/master/README.md#goto) [`If statements`](https://github.com/BatchSource/PytchScript/blob/master/README.md#if-statements) [`If statements (multiple lines)`](https://github.com/BatchSource/PytchScript/blob/master/README.md#if-statements-with-multiple-lines) [`Input`](https://github.com/BatchSource/PytchScript/blob/master/README.md#input) [`If, and, else, or`](https://github.com/BatchSource/PytchScript/blob/master/README.md#if-and-else-or) [`Set command functions`](https://github.com/BatchSource/PytchScript/blob/master/README.md#set-command-functions) [`Random`](https://github.com/BatchSource/PytchScript/blob/master/README.md#random) [`Integer Operatons`](https://github.com/BatchSource/PytchScript/blob/master/README.md#integer-operations) [`Float Operations`](https://github.com/BatchSource/PytchScript/blob/master/README.md#float-operations) [`For loops`](https://github.com/BatchSource/PytchScript/blob/master/README.md#for-loops)

#### [Simulate Keyboard and Mouse Inputs](https://github.com/BatchSource/PytchScript/blob/master/README.md#simulate-keyboard-and-mouse-inputs-1)

[`Keyboard Presses`](https://github.com/BatchSource/PytchScript/blob/master/README.md#keyboard-presses) [`Keyboard Typing`](https://github.com/BatchSource/PytchScript/blob/master/README.md#keyboard-typing) [`Cursor Clicks`](https://github.com/BatchSource/PytchScript/blob/master/README.md#cursor-clicks) [`Cursor Movements`](https://github.com/BatchSource/PytchScript/blob/master/README.md#cursor-movements)

#### [GUIs and Special Variables](https://github.com/BatchSource/PytchScript/blob/master/README.md#guis-and-special-variables-1)

[`Types of GUIs`](https://github.com/BatchSource/PytchScript/blob/master/README.md#types-of-guis) [`Msgbox`](https://github.com/BatchSource/PytchScript/blob/master/README.md#msgbox) [`Textbox`](https://github.com/BatchSource/PytchScript/blob/master/README.md#textbox) [`Buttonbox/Choicebox`](https://github.com/BatchSource/PytchScript/blob/master/README.md#buttonbox-choicebox) [`Special Variables`](https://github.com/BatchSource/PytchScript/blob/master/README.md#special-variables)

----------------------

## Installation

Clone the repository and unzip it somewhere in your desktop. That folder will contain all the necessary files to run and compile a Pytch file. You do not need to install any development software.

If you want to execute a pytch command in a batch file, you can either add pytch to the `%path%` variable or move `Pytch.exe` to the same directory as the batch file.
You can execute commands like this:
```
pytch22 -c say Hello World
```

## Getting Started
So now you have Pytch in your desktop, but now what? We don't have any code written for it so lets write something simple, a hello world program!

Go ahead and open your favorite text editor. Go ahead and type in the following:
```
say Hello, World!
```
Now save it as a .pytch file.

To run the file go ahead and open up Command Prompt and cd into the directory where Pytch.py is located, in this case we extracted it into our desktop, so lets cd into the directory.
```
cd C:\Users\PytchScript\Desktop\PytchScript-master\
```
Now to run it. Go ahead and type in the following:
```
pytch22 -r "<path to the pytch file>"
```
Replace <path to the pytch file> with the path of the file. So if we have the Pytch file in our desktop, then it would be:
```
pytch22 -r "C:\Users\PytchScript\Desktop\file.pytch"
```
As soon as you press enter, you should see the following:
```
Hello, World!
```
Great, you created your first Pytch program! The next sections will teach you more about the commands and syntax, and different build options for Pytch.

### Console
You can activate the console by doing:
```
pytch22 --console
```
However, you cannot use goto in the the Pytch console.

### Start.bat
If you don't want to activate the terminal every time you want to run a file, you can click and drag the `.pytch` file over `start.bat` in explorer.
You can open the console just by normally double-clicking `start.bat` in explorer.
You can download start.bat [here](https://raw.githubusercontent.com/BatchSource/PytchScript/master/start.bat).

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
// OR
print <text>
// OR
echo <text>
```

#### Output: String

Replace text with whatever you want, or leave it like that, nothing is stopping you.
```
say This is the say command in Pytch!
```
That outputs:
```
This is the say command in Pytch!
```

#### Output: Variable

To output a variable:
```
set myVar = 10
say The value of myVar is [myVar]!
```
Which outputs:
```
The value of myVar is 10!
```

##### Output: Empty line

You can use `say.` to easity
A simple way to create a blank line is:
```
say 1234
say.
say 1234
```
Outputs:
```
1234

1234
```

##### Output: Clear

Cls/clear can be used like this:
```
clear
// OR
cls
```

### Wait
Wait for a specific amount of miliseconds.
For example,
```
wait 1000
```
This will wait for 1000 miliseconds, or one whole second.
You could also use `wait 1000 ms` and `wait 1000 milliseconds` for milliseconds.

You can also run:
```
wait 1 sec
// OR
wait 1 second
```
To wait 1 second.

### Beep
You can use the `beep` or the `play` command to play frequencies inside the terminal.
For example, you can write:
```
beep 250 freq 1000
```
This will play a frequency of 1000 for 250 ms.
You can also use the note command to play piano notes.
```
beep 250 note e5 d#5 e5 d#5 b#4 d5 c5 a4
// You can run multiple notes in order like this without having to create a new line for each one.
```

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

### TTS

You can use `speak` or `tts` to for text to speech.
```
speak Hello World!
// OR
tts Hello World!
```

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

You could also use `if defined` to check to see if something is defined.
For example:
```
if defined var1     say Hello
if not defined var1 say Goodbye
```
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
### Set command functions
In the set command, there are different multiple cuntions.

The first feature is to grab specific characters from a string.
For example, you can use:
```
set var =.char 1 3 Hello World
```
...to grab the first to 3 characters of the string "Hello World".
This would set var to `Hel`, because it is the first 3 character of "Hello World".

The next feature is to use "`.len`". This can be used to calculate the legnth of a string.
For example:
```
set var =.len Hello World
```
This will set `var` to be "`10`" because the legnth of "Hello World" is 10 characters long.

Next we have the `.upper` and `.lower` to convert the case to either be uppercase or lowercase.
For example:
```
set var1 =.upper Hello World
set var2 =.lower Hello World
```
This will set `var1` to `HELLO WORLD` and `var2` to `hello world`.

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

You also can use the in-line loop feature to loop Hello 100 times.
For example:
```
100 say Hello
```
This will also say Hello 100 times.
You can also use a variable with this feature to create dynamic forloops.

## Simulate Keyboard and Mouse Inputs

Keyboard and mouse movements can be used with the `wait` command to create algorithms to automate boring work.

### Keyboard Presses
You can use the `key` command to simulate keyboard and mouse inputs.
You can use `key press` to to use any of the function keys, arrow keys, backspace, enter, shift, space, tab, escape, delete, copy, and paste.

You can also use the commands in order like this:
```
key press tab esc right
```

### Keyboard Typing
You can use the `key type` command to type words.
For example, you can type `Hello World` by doing:
```
key type Hello World
```

Remember, you have to use `&` to simulate multiple spaces.
For example:
```
key type Hello&&&&World
```
This will create 4 spaces.

### Cursor Clicks
You can simulate cursor events with the `key cursor` command.
To use clicks, you have to use `key cursor click`.

For example:
```
key cursor click left
```

This will simulate a left click.
Like the key presses, you can make multiple clicks in one line of code.

For example:
```
key cursor click left right middle left left
```

You could also create a super auto clicker in one line of code by using the single-line forloop with the cursor click feature.
You could do `-1 key cursor click left` to indefinetly left lick, however it does lag up your system due to the 10k-500k clicks per second.

### Cursor Movements
You can move the cursor with the `key cursor move` command.

You need the XY value of the screen pixel to set the cursor position to.

For example:
```
key cursor move 10 20
```

This will move the cursor pointer to the screen pixel X:10 and Y:20.

## GUIs and Special Variables

### Types of GUIs
There are 3 types of GUIs in pytch.
`msgbox`, `textbox`, and `buttonbox`.

### Msgbox
The `msgbox`/`messagebox` GUI is for create alerts for the user.
The syntax for this command is:
```
gui varName msgbox --title: Your title here --text: Your text here.
// OR
gui varName msgbox -title Your title here -text Your text here.
```
You can use the `--text:` or `--title:` instead of `-text` and `-title` to be more organized.
This will create a simple message box gui. When the user clicks `OK`, it will set `varName` to be `OK`.

It also pauses the script until the user click "X" or "OK". If you do not want to pause the script, you can use `cmd msg * Your message here`.

### Textbox
The next type of GUI is the textbox. This can be used to get a user input from the user in a GUI application.
The command is:
```
gui varName textbox --title: Your title here --text: Your question/text here --prompt: Optional prompt here.
// OR
gui varName textbox -title Your title here -text Your question/text here -prompt Optional prompt here.
```
The `prompt` command is optional, and is used to automatically put text in the textbox before the user types anything.

This command will set the contents of the textbox to `varName`.

### Buttonbox/Choicebox
The final type of GUI is the Buttonbox. This is used to give the user a list of buttons to choose from.
You could also use "`choicebox`" for a different interface.

The command is:
```
// FOR BUTTONBOX:
gui varName buttonbox --title: Your title here --text: Your question/text here --buttons: Button1 Button2 Button3 Button4
gui varName buttonbox -title Your title here -text Your question/text here -buttons Button1 Button2 Button3 Button4

// FOR CHOICEBOX:
gui varName choicebox --title: Your title here --text: Your question/text here --buttons: Button1 Button2 Button3 Button4
gui varName choicebox -title Your title here -text Your question/text here -choices Choice1 Choice2 Choice3 Choice4

```
This will give users a list of buttons to choose from.
This command will set the name of the button pressed to `varName`.

### Special Variables
These variables use {} instead of []. They are variables built into the language.
(Note: These variables don't update when the in-line forloop command is on. For example, `-1 say {time}` will not update the variable value and just repeat the value it was at when the loop started.)

Here is a list of all the special variables and their functions:
```
{space}           // creates a space. does the exact same thing as &
{amp}             // creates an ampersand (normal ampersands turn into spaces)
{home}            // the %userprofile% directory
{file}            // the current file name the script is running of off.
{time}            // HH:MM:SS, similar to %time% in batch
{time12}          // HH:MM:SS PM, 12h time, similar to the "time /t" command in batch
{date}            // YYYY-MM-DD, for example: 2020-09-15
{weekday}         // DAY, for example: Mon
{cursorpos}       // The current cursor position
{cursorposX}      // The cursor X position
{cursorposY}      // The cursor Y position
{cursorcolor}     // The pixel under the cursor's RGB value
{cursorcolorR}    // The pixel under the cursor's R (RGB) value
{cursorcolorG}    // The pixel under the cursor's G (RGB) value
{cursorcolorB}    // The pixel under the cursor's B (RGB) value
{cursorcolorHex}  // The pixel under the cursor's Hex value
{cursorcolorName} // The pixel under the cursor's closest CSS color name
```
