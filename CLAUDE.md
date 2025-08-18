# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Sublime Text 4 plugin (compatible with ST3) that provides daily logging functionality for personal diary, project logs, and food logs. The plugin adds commands to Sublime Text's Tools menu and context menu to create and manage markdown/YAML files in a structured folder hierarchy.

## Architecture

### Core Components

- `Diary.py` - Main plugin file containing all command classes and utility functions
- `Main.sublime-menu` - Adds commands to the Tools menu
- `Context.sublime-menu` - Adds "Go to DIARY" command to context menu

### Key Functions

- `DiaryCommand` - Creates daily diary entries in `~/Dropbox/Braindump/Diary/YYYY-MM-DD.md`
- `ProjectLogCommand` - Creates project log entries in `~/Dropbox/Braindump/ProjectLog/pYYYY-MM-DD.md`
- `FoodLogCommand` - Creates monthly food logs in `~/Dropbox/Braindump/FoodLog/YYYY-MM.yml`
- `GoToDiaryCommand` - Opens files/folders based on backtick-enclosed paths with volume resolution

### File Structure

The plugin expects a `~/Dropbox/Braindump` directory structure:
```
Braindump/
├── Diary/           # Daily markdown entries
├── ProjectLog/      # Project-specific logs
├── FoodLog/         # Monthly YAML food logs
└── Notes/           # General notes
```

### Path Resolution System

The plugin uses a volume system for cross-platform path resolution:
- Volumes are defined in Sublime Text preferences under `diary_volumes`
- Paths in backticks like `Work:Tests/Project` resolve using volume mappings
- Falls back to searching within Braindump folder structure for relative paths

## Development Commands

### Testing Commands

To test the plugin commands manually in Sublime Text console:
```python
view.run_command('diary')
view.run_command('project_log')
view.run_command('food_log')
view.run_command('go_to_diary')
```

### Plugin Installation

The plugin is installed by copying the entire folder to Sublime Text's Packages directory (accessible via Preferences -> Browse Packages).

### ST4 Compatibility

- Uses Python 3.8 runtime (specified in `.python-version` file)
- Cross-platform file opening replaces Windows-only `os.startfile()`
- Maintains backward compatibility with ST3

## Configuration

Users configure volume mappings in Sublime Text preferences:
```json
"diary_volumes": {
    "Work": "D:\\Work\\",
    "Projects": "D:\\Projects\\",
    "Dropbox": "~/Dropbox/",
    "UNI": "~/Dropbox/_UNI/"
}
```

## File Templates

### Diary Template
```markdown
---
created_at: YYYY-MM-DD HH:MM:SS +ZZZZ
location: 
---

# Diary for YYYY-MM-DD, Day

## HH:MM - 
```

### Project Log Template
```markdown
---
created_at: YYYY-MM-DD HH:MM:SS +ZZZZ
location: 
---

# ProjectLog for YYYY-MM-DD, Day

## HH:MM - 
```

### Food Log Template
```yaml
---
title: Food Log for YYYY-Mon
created: YYYY-MM-DD HH:MM:SS
---
data:

- 
  date: YYYY-MM-DD HH:MM:SS
  food: 
  feeling: 
  supplements: 
```
