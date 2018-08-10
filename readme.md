
# Sublime Text 3 plugin for my daily logs

This is a little ST3 plugin which adds some new commands to the Tools menu that help create and update the markdown/yaml files I use for daily logging.

## Installation

Copy the Diary folder into the Sublime Text Packages folder (Preferences -> Browse Packages).

## Dev notes

### Ref Links

- https://www.sublimetext.com/docs/plugin-examples
- https://www.sublimetext.com/docs/3/api_reference.html
- https://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685
- https://stackoverflow.com/questions/21954127/open-a-file-in-sublime-and-show-that-it-needs-saving

### Python Commands

```py
view.run_command('diary')
view.run_command('food_log')
```
