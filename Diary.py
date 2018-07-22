import sublime, sublime_plugin
import os.path
import datetime

class DiaryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		diary_file = expanduser('~') + '/Dropbox/Braindump/Diary/'+str(datetime.date.today())+'.md'
		now = datetime.datetime.now()

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

		newview = self.view.window().open_file(diary_file)
