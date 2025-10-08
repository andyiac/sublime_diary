import sublime, sublime_plugin
import datetime
import subprocess
import os

# sublime.log_commands(True)

def getSettings():
    user = sublime.load_settings("Preferences.sublime-settings")

    volumes = {}

    if user.has("diary_volumes"):
        for key,value in user.get("diary_volumes").items():
            volumes[key] = value

    settings = {"volumes": volumes}
    return settings

def moveToEofWhenLoaded(view):
    if not view.is_loading():
        view.run_command("move_to", {"to": "eof"})
    else:
        sublime.set_timeout(lambda: moveToEofWhenLoaded(view), 10)

def getBraindumpRoot():
    settings = getSettings()
    doc_root = settings["volumes"].get("DocRoot")
    if doc_root:
        return os.path.expanduser(doc_root)
    return os.path.expanduser('~') + '/Documents/Braindump'


def getDiaryPath(path):
    # remove prefixes if exist (to enable searching for yearly stashed entries)
    if path.startswith('Diary/'): path = path.replace('Diary/', '')
    if path.startswith('ProjectLog/'): path = path.replace('ProjectLog/', '')

    # file found, easy
    realpath = getBraindumpRoot() + '/' + path
    if os.path.isfile(realpath):
        return realpath

    # maybe it's a project log
    if path.startswith('p'):
        realpath = getBraindumpRoot() + '/ProjectLog/' + path
        if os.path.isfile(realpath):
            return realpath

        # maybe it's an old one
        realpath = getBraindumpRoot() + '/ProjectLog/' + path[1:5] + '/' + path
        if os.path.isfile(realpath):
            return realpath

    # maybe it _is_ in the Diary folder
    realpath = getBraindumpRoot() + '/Diary/' + path
    if os.path.isfile(realpath):
        return realpath

    # maybe it's buried in a yearly folder
    realpath = getBraindumpRoot() + '/Diary/' + path[0:4] + '/' + path
    if os.path.isfile(realpath):
        return realpath

    # maybe it is in the Notes folder
    realpath = getBraindumpRoot() + '/Notes/' + path
    if os.path.isfile(realpath):
        return realpath

    # maybe it's an absolute path, or dunno
    return path

def getRealPath(path, volumes):
    col = path.find(':')
    if (col == -1 or path.startswith('Diary:')):
        # path is not a volume, assume it's within Braindump
        diaryPath = path.replace('Diary:', '')
        return getDiaryPath(diaryPath)

    volname = path[0:col]
    if volname in volumes:
        realpath = volumes[volname].replace('~', os.path.expanduser('~'))
        return path.replace(volname+':', realpath)

    # perhaps absolute path...
    return path

class DiaryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        now = datetime.datetime.now()
        diary_file = getBraindumpRoot() + '/Diary/'+now.strftime('%Y-%m-%d')+'.md'

        isnew = not os.path.isfile(diary_file)

        with open(diary_file, 'a') as outfile:
            if isnew:
                txt = '\n'.join(('---',
                    'created_at: '+now.strftime('%Y-%m-%d %H:%M:%S %z'),
                    'location: ',
                    '---',
                    '',
                    '# Diary for '+now.strftime('%Y-%m-%d, %A')))

                outfile.write(txt)

            outfile.write('\n\n## '+now.strftime('%H:%M')+' - ')

        opened_view = self.view.window().open_file(diary_file)
        moveToEofWhenLoaded(opened_view)

class ProjectLogCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        now = datetime.datetime.now()
        diary_file = getBraindumpRoot() + '/ProjectLog/p'+now.strftime('%Y-%m-%d')+'.md'

        isnew = not os.path.isfile(diary_file)

        with open(diary_file, 'a') as outfile:
            if isnew:
                txt = '\n'.join(('---',
                    'created_at: '+now.strftime('%Y-%m-%d %H:%M:%S %z'),
                    'location: ',
                    '---',
                    '',
                    '# ProjectLog for '+now.strftime('%Y-%m-%d, %A')))

                outfile.write(txt)

            outfile.write('\n\n## '+now.strftime('%H:%M')+' - ')

        opened_view = self.view.window().open_file(diary_file)
        moveToEofWhenLoaded(opened_view)

class FoodLogCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        now = datetime.datetime.now()
        log_file = getBraindumpRoot() + '/FoodLog/'+now.strftime('%Y-%m')+'.yml'

        isnew = not os.path.isfile(log_file)

        with open(log_file, 'a') as outfile:
            if isnew:
                txt = '\n'.join(('---',
                    'title: Food Log for '+now.strftime('%Y-%b'),
                    'created: '+now.strftime('%Y-%m-%d %H:%M:%S'),
                    '---',
                    'data:'))

                outfile.write(txt)

            txt = '\n'.join(('\n-',
                '  date: '+now.strftime('%Y-%m-%d %H:%M:%S'),
                '  food: ',
                '  feeling: ',
                '  supplements: '))

            outfile.write(txt)

        opened_view = self.view.window().open_file(log_file)
        moveToEofWhenLoaded(opened_view)

class GoToDiaryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        backticks = list(map(lambda x: x.begin(), self.view.find_all('`')))
        caret = self.view.sel()[-1].b

        size, before, after = False, False, False
        all_before = list(filter(lambda x: x < caret, backticks))
        all_after = list(filter(lambda x: x >= caret, backticks))

        if all_before: before = all_before[-1]
        if all_after: after = all_after[0]

        if all_before and all_after:
            settings = getSettings()
            path = self.view.substr(sublime.Region(before+1, after))
            realPath = os.path.realpath(getRealPath(path, settings["volumes"]))
            print(path, "=>", realPath)
            # Cross-platform file opening for ST4 compatibility
            import platform
            system = platform.system()
            if system == 'Windows':
                os.startfile(realPath)
            elif system == 'Darwin':  # macOS
                subprocess.run(['open', realPath])
            else:  # Linux and others
                subprocess.run(['xdg-open', realPath])
