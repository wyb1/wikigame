import urllib
import re

pagesvisited = []


def findHorJ(url, count):
	if count > 2:
		pass
	else:
		htmlfile = urllib.urlopen(url)	#opens given wikipage
		htmltext = htmlfile.read()		#converts html to a text file

		
		pagename = getPageName(htmltext)		#gets the name of the page
		if pagename == 'Adolf Hitler' or pagename == "Jesus" or pagename == "United States":
			print "You found " + pagename + "!"
			quit()
		
		text = getText(htmltext)			#get relevent html text in <p> tags
		links = getLinks(text)				#gets all the links for text

		for link in links:
			if link[0:5] == '/wiki' and not hasVisitedPage(link):#if it is not a citiation 
				global pagesvisited			
				pagesvisited.append(link)
				print "pagename: " + pagename + " link: " +link + " count: " + str(count) 
				if link == "/wiki/Adolf_Hitler" or link == "/wiki/Jesus":
					print "You found " + link[5:]
				url = "https://en.wikipedia.org"+link
				if count < 2:
					findHorJ(url, count+1)	#recursive call

def hasVisitedPage(link):
	global pagesvisited
	for page in pagesvisited:
		if link == page:
			return True

	return False


def getPageName(htmltext):
	title = '<span dir="auto">(.+?)</span>'
	pattern = re.compile(title)
	pagename =  re.findall(pattern, htmltext)[0]
	return pagename

def getText(htmltext):
	text = '<p>(.+?)</p>'
	pattern = re.compile(text)
	words = re.findall(pattern, htmltext)
	for word in words:
			text = text + word
	return text

def getLinks(text):
	href = 'href="(.+?)"'
	pattern = re.compile(href)
	links = re.findall(pattern, text)
	return links


def main():
	#url = "https://en.wikipedia.org/wiki/Nazi_Germany"
	url = "https://en.wikipedia.org/wiki/Special:Random" #url for a random wikipedia page
	findHorJ(url, 0)

if __name__ == '__main__':
	main()

