import pickle
import random
wfile = open('words.b','rb')
mfile = open('m.b','rb')
words = pickle.load(wfile)
meanings = pickle.load(mfile)

print 'SAT Vocab Flash Cards'
asked = []

while True:
	try:	
		word = random.choice(words)
		if word not in asked:
			print ' '*25 + word.upper()
			know = raw_input('Do you know this? Y/N ')
			if know.lower()=='y':
				asked.append(word)
				print ''
				continue
			elif know.lower()=='n':
				print meanings[word][0], meanings[word][1]
				asked.append(word)
				print ''
				continue
				
	except (KeyboardInterrupt,SystemExit):
		break
rev = raw_input('\nWould you like to review? Y/N ')
if rev.lower()=='y':
	print 'These are the words you reviewed today'
	for word in asked:
		print word, meanings[word]

else:
	exit(0)