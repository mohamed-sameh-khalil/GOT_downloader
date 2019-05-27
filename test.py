import os, subprocess, sys
from bs4 import BeautifulSoup
import requests
Q720 = 1
Q480 = 0
def getSeasonDiv(divs, n = 8):
	for div in divs:
		if int(div.h5.span.string) == n:
			print("season: ", n)
			return div
	sys.exit();

def getEpisodeDiv(divs, n = 2):
	
	for div in divs:
		if int(div.h3.span.string) == n:
			print("episode: ", n)
			return div
	sys.exit();


contents = requests.get("https://ettvtorrents.com/game-of-thrones-2011/").text


soup = BeautifulSoup(contents, 'html.parser')

files = soup.select("#content_wrapper > div > div > div > div.another-toggle")
files = getSeasonDiv(files)

ep = open("ep.txt", "r")
ep_num = int(ep.read())

# files = getEpisodeDiv(files.div.select(".row"), ep_num).a['href']
files = getEpisodeDiv(files.div.select(".row"), ep_num).select("a")[Q720]['href']

ep.close()

ep = open("ep.txt", "w")
ep.write(str(ep_num + 1))
ep.close()

print("the link downloaded is: \n" + str(files))
args = 'qbittorrent.exe ' + '\"' + files + '\"'
# os.system(args)
subprocess.Popen(args, close_fds = True)







