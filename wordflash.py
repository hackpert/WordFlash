import pickle
import random
import sys
import requests
from bs4 import BeautifulSoup
import os


wfile = open('words.b','rb')
mfile = open('m.b','rb')
words = pickle.load(wfile)
meanings = pickle.load(mfile)

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

print 'Vocabulary Flash Cards'
asked = []
knew = 0
dknw = 0
while True:
	try:	
		word = random.choice(words)
		if word not in asked:
			print ' '*25 + word.upper()
			know = raw_input('Do you know this? Y/N ')
			if know.lower()=='y' or know == '':
				#asked.append(word)
				knew += 1
				print ''
				continue
			elif know.lower()=='n':
				try:
					print meanings[word][0], meanings[word][1]
				except KeyError:
					pass
				try:
					res = requests.get('http://www.vocabulary.com/dictionary/' + word, headers={'user-agent': 'Mozilla/5.0'}).text
					souped = BeautifulSoup(res)
					dn = souped.find('p', {'class': 'short'})
					print strip_tags(dn.prettify('ascii')).replace('\n','')
				except AttributeError:
					pass
				asked.append(word)
				dknw += 1
				print ''
				continue
				
				
	except (KeyboardInterrupt,SystemExit):
		break
rev = raw_input('\nWould you like to review? Y/N ')
if rev.lower()=='y':
	#unused_variable = os.system('cls')
	unused_variable = os.system('clear')
	print 'These are the words you reviewed today\n'
	for word in asked:
		print word.upper() + ' '*(20 - len(word)), meanings[word][0] + ' '*(5-len(meanings[word][0])) + '|', meanings[word][1]
	print 'This time you knew %d words and didn\'t know %d words'%(knew,dknw)
else:
	exit(0)
	
