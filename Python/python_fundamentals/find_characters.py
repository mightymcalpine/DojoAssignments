yodaSays = ['Size', 'matters', 'not', 'Look', 'at', 'me', 'Judge', 'me', 'by', 'my', 'size', 'do', 'you', 'Hmm', 'Hmm', 'And', 'well', 'you', 'should', 'not', 'For', 'my', 'ally', 'is', 'the', 'Force', 'and', 'a', 'powerful', 'ally', 'it', 'is']
char = 'm'

newList = []

for idx in yodaSays:	
	if idx.count(char):
		newList.append(idx)
	else:
		continue
print newList