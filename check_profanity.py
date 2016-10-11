import urllib

def read_text():
	print "Please enter the absolute path of the file you want to check: "
	file_name = raw_input()
	curse_word = False
	with open(file_name) as contents:
		for num, line in enumerate(contents, 1):
			if check_profanity(line) == "true":
				curse_word = True
				print line
				print "Found curse word at line " + str(num)
	if not curse_word:
		print "This document has no curse words!"
	return

def check_profanity(texts):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+texts)
	result = connection.read()
	connection.close()
	return result

read_text()
