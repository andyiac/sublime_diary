import sublime, sublime_plugin
import os.path
import datetime

class DiaryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		now = datetime.datetime.now()
		diary_file = expanduser('~') + '/Dropbox/Braindump/Diary/'+now.strftime('%Y-%m-%d')+'.md'

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

		self.view.window().open_file(diary_file)

class FoodLogCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		now = datetime.datetime.now()
		log_file = expanduser('~') + '/Dropbox/Braindump/FoodLog/'+now.strftime('%Y-%m')+'.yml'

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

		self.view.window().open_file(log_file)