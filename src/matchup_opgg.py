## IMPLEMENT COMPETITIVE ASWELL, THIS IS ONLY SOLOQ INFO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

####

def assemble_matchup_url_opgg(champ1, champ2, lane, region, rank):
	#https://www.op.gg/champions/irelia/counters/top?region=global&tier=master_plus&target_champion=jax
	#You can also specify a patch with op.gg, might be worthwhile
		#https://www.op.gg/champions/irelia/counters/top?region=euw&tier=master_plus&target_champion=jax&patch=13.22
	url = "https://www.op.gg/champions/{}/counters/{}?region={}&tier={}&target_champion={}".format(champ1, lane, region, rank, champ2)
	return url

def get_matchup(url):
	chrome_options = Options()
	chrome_options.add_argument("--incognito")

	driver = webdriver.Chrome(options=chrome_options)

	driver.get(url)
	driver.implicitly_wait(10) #This is bad and shouldn't be used

####

champ1 = input("First champion(lowercase): ")
champ2 = input("Second champion(lowercase): ")
lane = input("Lane(lowercase): ")
region = input("Region(lowercase acronyms: kr, euw, etc): ")
rank = input ("Rank(UpperCaseInitials): ")

url = assemble_matchup_url_opgg(champ1, champ2, lane, region, rank)

print(url)
get_matchup(url)
