## IMPLEMENT COMPETITIVE ASWELL, THIS IS ONLY SOLOQ INFO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
####

def assemble_matchup_url_moba(champ1, champ2, lane, rank):
	url = "https://app.mobalytics.gg/lol/champions/{}/counters/{}/vs-{}?rank={}".format(champ1, lane, champ2, rank)
	return url

def assemble_matchup_url_opgg(champ1, champ2, lane, region, rank):
	#https://www.op.gg/champions/irelia/counters/top?region=global&tier=master_plus&target_champion=jax
	url = "https://www.op.gg/champions/{}/counters/{}?region={}&tier={}&target_champion={}".format(champ1, lane, region, rank, champ2)

def get_matchup(url, champ1, champ2):
	chrome_options = Options()
	chrome_options.add_argument("--incognito")

	driver = webdriver.Chrome(options=chrome_options)

	driver.get(url)
	driver.implicitly_wait(2) #This is bad and shouldn't be used
	#Find td elements that contain the texts (Level 2, GD@15, etc...)
	td_elements = driver.find_elements(By.XPATH,	"//td[contains(text(), 'Level 2')] | \
													//td[contains(text(), 'GD@15')] | \
													//td[contains(text(), 'XPD@15')] | \
													//td[contains(text(), 'CSD@15')]")

	# For loop printing elements found
	for td_element in td_elements:
		print(td_element.text + ":", end =" ")
		siblings = td_element.find_elements(By.XPATH, "preceding-sibling::*[1] | following-sibling::*[1]") # Find previous and next td element, which contain the data

		for sibling in siblings:
			if sibling.text == siblings[0].text: # Checks if this is this equal to the first position of siblings array (= precending-sibling), i.-e. = first champ
				print(champ1.capitalize() + " " + sibling.text, end =" - ")
			elif sibling.text == siblings[1].text: # Checks if this is this equal to the second position of siblings array (= following-sibling), i.-e. = first champ
				print(champ2.capitalize() + " " + sibling.text)
			else:
				print("You stupid")

def main():
	champ1 = input("First champion: ")
	champ2 = input("Second champion: ")
	lane = input("Lane: ")
	rank = input ("Rank: ")

	url = assemble_matchup_url_moba(champ1.lower(), champ2.lower(), lane.lower(), rank.capitalize())

	print(url)
	get_matchup(url, champ1, champ2)

main()