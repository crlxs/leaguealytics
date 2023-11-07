#### IMPORTS

# basic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# select
from selenium.webdriver.support.select import Select

####

#Given a Tournament craft the URL. Just need to swap spaces for %20

#def teams(tournament):
#example URL "https://gol.gg/teams/list/season-ALL/split-ALL/tournament-LEC%20Spring%20Season%202023/"

def replace_spaces(input_string):
	return input_string.replace(" ", "%20")

tournament = "LEC Summer Playoffs 2023"
tournament_formated = replace_spaces(tournament)

url = "https://gol.gg/teams/list/season-ALL/split-ALL/tournament-{}/".format(tournament_formated)

print("Tournament: " + tournament)
print("Tournament formatted: " + tournament_formated)

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
driver.implicitly_wait(5) #Implicit wait is bad
