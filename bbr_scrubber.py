from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 

year = 2019 # change year to analyze different eras
url_bbr = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'.format(year)
html_bbr = urlopen(url_bbr)

soup_bbr = BeautifulSoup(html_bbr, features='lxml') # parses HTML doc 

stat_headers = [txt.get_text() for txt in soup_bbr.find_all('tr', limit=2)[0].find_all('th')] #extracts headers for statistics such as PTS or MP

stat_headers = stat_headers[1:] # removes the first item, which is garbage

rows = soup_bbr.find_all('tr')[1:]
player_stats_bb = [[stats.get_text() for stats in rows[i].find_all('td')] for i in range(len(rows))] #double list comprehesion to extract stats as a 2D list, makes it complatible w/ DataFrame

stats = pd.DataFrame(player_stats_bb, columns=stat_headers)
first_ten = stats.head(10) # .head(int) extracts the first 10 rows from the DataFrame, just used to test the frame out
print(first_ten)