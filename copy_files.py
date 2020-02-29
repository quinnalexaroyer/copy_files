import os
from os import path
import shutil
import time

def copyDir(sourceDir,destDir,since=None,deep=False):
	since2 = None
	if since is not None:
		since2 = timestamp(since)
	if sourceDir[-1] != "\\":
		sourceDir += "\\"
	if destDir[-1] != "\\":
		destDir += "\\"
	dirList = []
	if not os.path.isdir(destDir):
		os.mkdir(destDir)
	for i in os.listdir(path=sourceDir):
		if deep and os.path.isdir(sourceDir+i):
			dirList.append(i)
		else:
			if not os.path.isdir(sourceDir+i) and (since2 is None or os.path.getmtime(sourceDir+i) >= since2):
				try:
					shutil.copy2(sourceDir+i,destDir+i)
				except PermissionError:
					pass
	if deep:
		for i in dirList:
			if len(os.listdir(path=sourceDir+i)) > 0:
				os.mkdir(destDir+i)
				copyDir(sourceDir+i+"\\",destDir+i,since=since,deep=deep)

def timestamp(s):
	st = [0]*9
	st[0] = int(s[:4])
	st[1] = int(s[4:6])
	st[2] = int(s[6:8])
	if len(s) >= 11:
		st[3] = int(s[9:11])
	if len(s) >= 13:
		st[4] = int(s[11:13])
	if len(s) >= 15:
		st[5] = int(s[13:15])
	st[8] = -1
	return time.mktime(tuple(st))
