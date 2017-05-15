import re

def find_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
	matches = []
	for word in words:
		if re.search(regex, word):
			matches.append(word)
	return matches

token1 = re.compile(r'[v]\w+')
token2 = re.compile(r'[s]{2}')
token3 = re.compile(r'[e]\b')
token4 = re.compile(r'[b]\w+[b]')
token5 = re.compile(r'[b].[b]')
token6 = re.compile(r'[b]{2}|\w+[b]')
token7 = re.compile(r'a[^iou]*e[^aiou]*i[^aeou]*o[^aeiu]*u')
token8 = re.compile(r'\b[regularexpression]+\b')
token9 = re.compile(r'(.)\1{1,}')

print find_matching_words(token8)