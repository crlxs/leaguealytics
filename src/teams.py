#### IMPORTS

# basic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# select
from selenium.webdriver.support.select import Select

####

#Given a league, season and split, list all teams.

#def teams():
url = "https://gol.gg/"

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
