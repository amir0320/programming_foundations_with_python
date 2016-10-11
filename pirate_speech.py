import urllib

def read_text():
	print "Enter the absolute path of the txt file you want to translate into a pirate speech: "
	file_name = raw_input()
	quotes = open(file_name)
	contents_of_file = quotes.read()
	print pirate_speech(contents_of_file)
	quotes.close()
	return

def pirate_speech(texts):
	connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + texts)
	result = connection.read()
	connection.close()
	return result
	
read_text()
