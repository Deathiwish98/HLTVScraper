from bs4 import BeautifulSoup	
import requests

terminalHeader ='''
db   db db      d888888b db    db      .d8888.  .o88b. d8888b.  .d8b.  d8888b. d88888b d8888b.
88   88 88      `~~88~~' 88    88      88'  YP d8P  Y8 88  `8D d8' `8b 88  `8D 88'     88  `8D
88ooo88 88         88    Y8    8P      `8bo.   8P      88oobY' 88ooo88 88oodD' 88ooooo 88oobY'
88~~~88 88         88    `8b  d8'        `Y8b. 8b      88`8b   88~~~88 88~~~   88~~~~~ 88`8b
88   88 88booo.    88     `8bd8'       db   8D Y8b  d8 88 `88. 88   88 88      88.     88 `88.
YP   YP Y88888P    YP       YP         `8888Y'  `Y88P' 88   YD YP   YP 88      Y88888P 88   YD
																								Version : 0.1
																								Author  : Pawan Sharma	
'''

def main():
	print(terminalHeader)
	scrapeMatches = HltvScraper('Matches')
	scrapeMatches.matchListScraper()


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.'
											'3112.113 Safari/537.36'}


class HltvScraper:
	def __init__(self, content):
		self.content = content
		self.teams = []

	def matchListScraper(self):
		soup = self.getSoup()
		for match_info in soup.find_all('div', class_='match-day'):
			print("DATE -", match_info.span.text, sep=" ")
			for each_table in match_info.find_all('table', class_='table'):
				print("\t\t", each_table.div.text, end=" -\t")
				for each_team in each_table.find_all('div', class_='team'):
					self.teams.append(each_team.text)
				print(self.teams[0], 'V/S', self.teams[1])
				del self.teams[:]

	def getSoup(self):
		if self.content == "Matches":
			source = requests.get('https://www.hltv.org/matches', headers=headers).text
		else:
			source = None
		return BeautifulSoup(source, 'lxml')

if __name__ == '__main__':
	main()




