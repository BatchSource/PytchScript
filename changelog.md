# Changelog

### [`2.5`](https://www.dropbox.com/s/6xchhm4a8k0kkwi/Pytch25.exe?dl=1)
- Added lists. They will split a variable into seperate elements. Each element in a list is a seperated by a space. Lists use `()` instead of `[]`.
    - Example of a list being used:
        ```
        set buttons = red green blue orange
        gui varname buttonbox --buttons: (buttons) --text: What is your fav color?

      // In this example, we are using a list for the buttons.
        ```
- New/changed syntax for types of variables. Here is a list of the possible commands for the `set` function:

    ```
    set <varname> input <prompt>               // Get user input
    set <varname> char <start> <end> <string>  // Grab range of characters
    set <varname> len <string>                 // Get the legnth of a string
    set <varname> listlen <list>               // Get the legnth of a list
    set <varname> upper <string>               // Convert to uppercase
    set <varname> lower <string>               // Convert to lowercase
    set <varname> reverse <string>             // Reverse a string
    set <varname> listreverse <list>           // Reverse a list
    set <varname> remove                       // Undefine a variable
    set <varname> cmd <command>    // Get the output of a terminal command
    set <varname> ord <list>       // Get a list of corresponding ASCII #s
    set <varname> chr <list>       // Get a string of corresponding ASCII chars
-  New commands added (similar to the new set commands, but print the output to the console instead of setting it to a variable/list).
    ```
    char <start> <end> <string>
    len <string>
    listlen <list>
    upper <string>
    lower <string>
    reverse <string>
    listreverse <list>
    ord <list>
    chr <list>
    ```
- New console write command to change the color of the output.
  Possible commands include `csay`/`cecho`/`cprint` or `say.color`/`echo.color`/`print.color`.

  The syntax to this command is "`csay <color> <string>`". Here are the possible colors you could use:
  ```
  csay grey    <string>
  csay red     <string>
  csay green   <string>
  csay yellow  <string>
  csay blue    <string>
  csay magenta <string>
  csay cyan    <string>
  csay white   <string>
  ```
 - Removed the "`Starting Pytch console...`" text when starting the program without any arguments.

---

### [`2.4`](https://www.dropbox.com/s/hemaehfpjzablu0/Pytch24.exe?dl=1)
- Optimimized/organized the way variables are set.
- Added `cmd`/`terminal` option to the `set` command to set the output of a cmd command to a variable. Syntax: `set var cmd dir`.
- Added a `to.reverse`/`=.reverse` option to the `set` command.
- You can now use `terminal` instead of `cmd` if you want.
- Syntax errors now say, "Invalid syntax ''. Type 'help' to view documentation.", instead of crashing immediately. Useful for debugging.
- Fixed error output when running '`exit`' command.
- `+=`,`-=`,`*=`,`/=` isn't as buggy anymore.
- Added `enterbox` and `passwordbox`/`passbox` types of GUIs.
- GUI parameters are no longer case sensitive.

---

### [`2.3`](https://www.dropbox.com/s/3ic0bacnkul8vcl/Pytch23.exe?dl=1)
- Bug fixes
- You can now click and drag files to run in Pytch.
- Modified the help screen to show new options.
- Added `window`/`size` command to resize window, similar to '`mode`' in cmd.
- Opening the program without any arguments now opens the console. (Useful for debuging)

---

### Other versions are not avaiable.
