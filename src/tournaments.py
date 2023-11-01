#### IMPORTS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

##
#### FUNCTIONS
##

#From gol.gg, scrape a list of tournaments by season for:
#	TOP = Major regions (LCK, LEC, LPL, etc) + MSI/Worlds
#	WC  = Wildcard (CBLOL, PCS, etc)
#	ERL = Regionals (LVP, LFL,)
#Tournament = league+split+stage (e.g. LCK Summer 2023), stage can be none (regular season), playoffs or finals
def tournaments(season):
#From gol.gg, scrape a list of tournaments by season for:
#   TOP = Major regions (LCK, LEC, LPL, etc) + MSI/Worlds
#   WC  = Wildcard (CBLOL, PCS, etc)
#   ERL = Regionals (LVP, LFL,)
#Tournament = league+split+stage (e.g. LCK Summer 2023), stage can be none (regular season), playoffs or finals

	url = "https://gol.gg/tournament/list/"

	chrome_options = Options()
	chrome_options.add_argument("--incognito")
	driver = webdriver.Chrome(options=chrome_options)

	driver.get(url)
	driver.implicitly_wait(0.5)

#Scrape current roster given a team name and tournament (league+split)
#def roster ():



##
#### EXECUTION
##

tournaments('S13')
