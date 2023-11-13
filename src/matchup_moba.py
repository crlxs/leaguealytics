## IMPLEMENT COMPETITIVE ASWELL, THIS IS ONLY SOLOQ INFO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

####

def assemble_matchup_url_moba(champ1, champ2, lane, rank):
	url = "https://app.mobalytics.gg/lol/champions/{}/counters/{}/vs-{}?rank={}".format(champ1, lane, champ2, rank)
	return url

def assemble_matchup_url_opgg(champ1, champ2, lane, region, rank):
	#https://www.op.gg/champions/irelia/counters/top?region=global&tier=master_plus&target_champion=jax
	url = "https://www.op.gg/champions/{}/counters/{}?region={}&tier={}&target_champion={}".format(champ1, lane, region, rank, champ2)

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
rank = input ("Rank(UpperCaseInitials): ")

url = assemble_matchup_url_moba(champ1, champ2, lane, rank)

print(url)
get_matchup(url)
