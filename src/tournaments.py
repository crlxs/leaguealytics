#### IMPORTS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#### GLOBAL VARIABLES

# List of lists to store leagues by type
TOP = ["LCK", "LCS", "LEC", "LPL", "MSI", "WORLDS"]
WC = ["CBLOL", "IWC", "LCL", "LCO", "LJL", "LLA", "LST", "MSS", "PCS", "VCS"]
ERL = ["AL", "BL", "BM", "DL", "EBL", "EMEAM", "ESLOL", "GLL", "HM", "LFL", "LPLOL", "NLC", "PGN", "PRM", "SL", "TCL", "Ultraliga"]

LEAGUES = [TOP, WC, ERL]
#### FUNCTIONS

#############################################################################################################################################################
#From gol.gg, scrape a list of tournaments by season for:
#	TOP = Major regions (LCK, LEC, LPL, etc) + MSI/Worlds
#	WC  = Wildcard (CBLOL, PCS, etc)
#	ERL = Regionals (LVP, LFL,)
#Tournament = league+split+stage (e.g. LCK Summer 2023), stage can be none (regular season), playoffs or finals

#From gol.gg, scrape a list of tournaments by season for:
#   TOP = Major regions (LCK, LEC, LPL, etc) + MSI/Worlds
#   WC  = Wildcard (CBLOL, PCS, etc)
#   ERL = Regionals (LVP, LFL,)
#Tournament = league+split+stage (e.g. LCK Summer 2023), stage can be none (regular season), playoffs or finals

def tournaments(season):
	url = "https://gol.gg/tournament/list/"

	chrome_options = Options()
	chrome_options.add_argument("--incognito")
	driver = webdriver.Chrome(options=chrome_options)

	driver.get(url)
	driver.implicitly_wait(0.5)
############################################################################################################################################################

############################################################################################################################################################
#Scrape current roster given a team name and tournament (league+split)
#def roster ():
############################################################################################################################################################


##
#### EXECUTION
##

#tournaments('S13')
for i in LEAGUES:
	for j in i:
		print (j, end=" ")
	print() 
