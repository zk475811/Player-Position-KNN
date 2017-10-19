import requests
from bs4 import BeautifulSoup
import time

url = 'http://games.espn.com/fba/tools/projections?startIndex='
position_options = {'pg' : 1, "sg" : 2, "sf" : 3, "pf" : 4, "c" : 5}
stop_index 	=  5
points_index 	= -1
rebounds_index 	= -5
assists_index 	= -4
position 	=  1
positions_index = -1

data = []
for i in range(0, stop_index):
	print('page')
	response = requests.get(url+str(40*(i+1)))
	soup = BeautifulSoup(response.text, 'html.parser')
	players = soup.select('[id^=plyr]')

	time.sleep(2)
	for player in players:
		points = player.contents[points_index].text
		rebounds = player.contents[rebounds_index].text
		assists = player.contents[assists_index].text
		player_position = player.contents[position].text.split()[positions_index]
		if player_position.lower() in position_options:
			data.append([points, rebounds, assists, str(position_options[player_position.lower()]) ])

f = open('playerstats.txt', 'w')
for player in data:
	for stat in player:
		f.write(stat)
		f.write('\t')
	f.write('\n')
f.close()
