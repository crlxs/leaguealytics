#### IMPORTS

# basic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# select
from selenium.webdriver.support.select import Select

####

#def playerstats(player, position, team, season, split):

#def tournaments():
url = "https://gol.gg/players/list/season-S13/split-ALL/tournament-ALL/"

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

driver.implicitly_wait(5) #Implicit wait is rarely the best solution, need to research a better way.

tournament_box = driver.find_element(By.NAME, 'cbtournament')
select = Select(tournament_box)
tournament_list = select.options

for t in tournament_list:
	print(t.get_attribute("value"))
	# https://stackoverflow.com/questions/18515692/listing-select-option-values-with-selenium-and-python
