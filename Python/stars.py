# 			** Part I **
arrNum = [6, 3, 12, 15, 36]
def draw_stars(arr):
	strStar = ''
	for idx in arr:
		for num in range(0, idx):
			strStar += '*'
		print strStar
		strStar = ''
	return 'Goodnight star counter'
star = draw_stars(arrNum)
print star

#			** Part II **
arrMixy = [6, 'Skywalker', 3, 'Bane of the Sith', 12, 'dagestan', 5]
def starsLetter(arr):
	strStar = ''
	strLetter = ''
	for idx in arr:
		if isinstance(idx, int):			
			for item in range(0, idx):
				strStar += '*'
			print strStar
			strStar = ''
		elif isinstance(idx, str):
			firstChar = idx[0]			
			for item in range(0, len(idx)):
				strLetter += firstChar
			print strLetter.lower()
			strLetter = ''
	return 'Goodnight mixy counter'
mixy = starsLetter(arrMixy)
print mixy

