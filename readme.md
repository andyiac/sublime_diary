
# Sublime Text 3 plugin for my daily diary

This is a little plugin which adds a new command to the Tools menu, which creates a new file for the day if it doesn't exist and adds a new heading for the new entry. Quite possibly only useful for me.

## Installation

Copy the Diary folder into the Sublime Text Packages folder (Preferences -> Browse Packages).

## Dev notes

https://www.sublimetext.com/docs/plugin-examples
https://www.sublimetext.com/docs/3/api_reference.html
https://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685

```py
view.run_command('diary')
```
