#python file which will open the 
#files which I want to usually open when working on django project at the beginnign

import os
import subprocess

#change if you work with differnt project
folder_path = input('What is the folder name of the project app you are working with?  ')

py_files = ['models.py', 'urls.py', 'forms.py','views.py']
html_folder_path = f'templates/{folder_path}'
html_files = os.listdir(f'{folder_path}/{html_folder_path}')

#I don't want to open base.html
hmtl_files = html_files.remove('base.html')

def open_files(file_paths):
	'''opens files with sublime text of the django app of the project'''
	for file_path in file_paths:
		subprocess.run(['open', '-a', 'Sublime Text', file_path])

#list with all files I want to open
file_paths = []

#python files of app
for py_file in py_files:
	file_paths.append(f'{folder_path}/{py_file}')

#html files
for html_file in html_files:
	file_paths.append(f'{folder_path}/{html_folder_path}/{html_file}')

open_files(file_paths)





