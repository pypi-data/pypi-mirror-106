# -*- coding: utf-8 -*-
from os import getenv, remove, listdir
from os.path import join as pjoin, isdir, exists, sep
from zipfile import ZipFile
from getpass import getuser
from requests import get

CD = pjoin(getenv("systemDrive"), sep)
USERNAME = getuser()
CHROME = pjoin(CD, 'Users', USERNAME, 'AppData', 'Local', 'Google', 'Chrome')
YANDEX = pjoin(CD, 'Users', USERNAME, 'AppData', 'Local', 'Yandex', 'YandexBrowser')
FIREFOX = pjoin(CD, 'Users', USERNAME, 'AppData', 'Local', 'Mozilla', 'Firefox')
OPERA = pjoin(CD, 'Users', USERNAME, 'AppData', 'Roaming', 'Opera Software')

def getChromeDriver():
	r = get('https://chromedriver.storage.googleapis.com/')
	cv = getChromeVersion()
	cdv = cv + r.text.split('<Key>' + cv)[1].split('/')[0]
	bytes = get('https://chromedriver.storage.googleapis.com/' + cdv + '/chromedriver_win32.zip').content
	with open('chromedriver.zip', 'wb') as f:
		f.write(bytes)
	with ZipFile('chromedriver.zip', 'r') as z:
		z.extractall(CHROME)
	remove('chromedriver.zip')
	return pjoin(CHROME, 'chromedriver')

def getChromeVersion():
	paths = [pjoin(CD, 'Program Files', 'Google', 'Chrome', 'Application'), pjoin(CD, 'Program Files (x86)', 'Google', 'Chrome', 'Application'), pjoin(CHROME, 'Application')]
	for i in range(len(paths)):
		try:
			dir = paths[i]
			files = listdir(dir)
			break
		except:
			pass
	for file in files:
		if isdir(pjoin(dir, file)) and file.__contains__('.'):
			return file.split('.')[0]
	return None

def getOperaDriver():
	ov = getOperaVersion()
	tags = get('https://api.github.com/repos/operasoftware/operachromiumdriver/tags').json()
	for i in range(len(tags)):
		tag = tags[i]['name']
		release = get('https://api.github.com/repos/operasoftware/operachromiumdriver/releases/tags/' + tag).json()['body']
		name = release.split(']')[0].split('[')[1]
		try:
			if name.__contains__('Stable'):
				odv = name.split('Stable ')[1]
			else:
				odv = name.split('Opera ')[1]
			if ov == odv:
				bytes = get('https://github.com/operasoftware/operachromiumdriver/releases/download/' + tag + '/operadriver_win32.zip').content
				with open('operadriver.zip', 'wb') as f:
					f.write(bytes)
				with ZipFile('operadriver.zip', 'r') as z:					
					opera = pjoin(CD, 'Users', USERNAME, 'AppData', 'Local', 'Opera Software')
					z.extractall(opera)
				remove('operadriver.zip')
				return
		except:
			return
	return pjoin(opera, 'operadriver_win32', 'operadriver')

def getOperaVersion():
	paths = [pjoin(CD, 'Users', USERNAME, 'AppData', 'Local', 'Programs', 'Opera'), pjoin(CD, 'Program Files', 'Opera'), pjoin(CD, 'Program, Files (x86)', 'Opera')]
	for i in range(len(paths)):
		try:
			dir = paths[i]
			files = listdir(dir)
			break
		except:
			pass
	for file in files:
		if isdir(pjoin(OPERA, file)):
			if exists(pjoin(OPERA, file, 'opera.exe')):
				return file.split('.')[0]
	return None

def getYandexDriver():
	yav = getYandexVersion()
	yv = yav.replace('.' + yav.split('.')[3], '').replace('.', '')
	tags = get('https://api.github.com/repos/yandex/YandexDriver/tags').json()
	ydvs = []
	for i in range(len(tags)):
		tag = tags[i]['name']
		ydvs.append(tag + '\n' + tag.replace('v', '').replace('-stable', '').replace('.', ''))
	for i in range(len(ydvs)):
		if yv == ydvs[i].split('\n')[1]:
			tag = ydvs[i].split('\n')[0]
			break
		if yv[0:3] == ydvs[i].split('\n')[1][0:3]:
			tag = ydvs[i].split('\n')[0]
			break
	assets = get('https://api.github.com/repos/yandex/YandexDriver/releases/tags/' + tag).json()['assets']
	for i in range(len(assets)):
		if assets[i]['name'].__contains__('win'):
			url = assets[i]['browser_download_url']
			break
	bytes = get(url).content
	with open('yandexdriver.zip', 'wb') as f:
		f.write(bytes)
	with ZipFile('yandexdriver.zip', 'r') as z:
		z.extractall(YANDEX)
	remove('yandexdriver.zip')
	return pjoin(YANDEX, 'yandexdriver')

def getYandexVersion():	
	paths = [pjoin(CD, 'Program Files (x86)', 'Yandex', 'YandexBrowser'), pjoin(CD, 'Program Files', 'Yandex', 'YandexBrowser'), pjoin(YANDEX, 'Application')]
	for i in range(len(paths)):
		try:
			dir = paths[i]
			files = listdir(dir)
			break
		except:
			pass
	for file in files:
		if isdir(pjoin(dir, file)) and file.__contains__('.'):
			return file
	return None

def getFirefoxDriver():
	assets = get('https://api.github.com/repos/mozilla/geckodriver/releases/latest').json()['assets']
	for i in range(len(assets)):
		if assets[i]['name'].__contains__('win32'):
			url = assets[i]['browser_download_url']
			break
	bytes = get(url).content
	with open('firefoxdriver.zip', 'wb') as f:
		f.write(bytes)
	with ZipFile('firefoxdriver.zip', 'r') as z:
		z.extractall(FIREFOX)
	remove('firefoxdriver.zip')
	return pjoin(FIREFOX, 'geckodriver')