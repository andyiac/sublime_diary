
## install path 

```
~/Library/Application Support/Sublime Text/Packages [18:36:53] 
$ ls
sublime_diary User
```

# Sublime Text 4 plugin for my daily logs

This is a Sublime Text 4 plugin (compatible with ST3) which adds some new commands to the Tools menu that help create and update the markdown/yaml files I use for daily logging, and keep track of different projects I'm working on.

## Installation

Copy the plugin folder into the Sublime Text Packages folder (Preferences -> Browse Packages).

## Settings

The 'Go to DIARY' context menu can resolve "volumes", that is root folders where different projects are kept. I have the same folder structures on the machines I work with, but they may be in a different path (e.g. between Window and macOS, etc)

Add to Preferences -> settings.

```
	"diary_volumes": {
		"Work": "D:\\Work\\",
		"Projects": "D:\\Projects\\",
		"Dropbox": "~/Dropbox/",
		"UNI": "~/Dropbox/_UNI/"
	}
```

Paths between backticks are opened, and resolved using the volumes set in Preferences. E.g. `Work:Tests/MyCoolProject` would resolve to `D:\Work\Tests\MyCoolProject` using the above settings.

I have `.md` files associated with Sublime Text, so opening them just opens a new tab for me. If the path is a folder it gets opened in Explorer/Finder/etc.

## Dev notes

### Ref Links

- https://www.sublimetext.com/docs/plugin-examples
- https://www.sublimetext.com/docs/api_reference.html
- https://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685
- https://stackoverflow.com/questions/21954127/open-a-file-in-sublime-and-show-that-it-needs-saving
- https://github.com/kek/sublime-expand-selection-to-quotes

### Python Commands

```py
view.run_command('diary')
view.run_command('project_log')
view.run_command('food_log')
view.run_command('go_to_diary')
```
