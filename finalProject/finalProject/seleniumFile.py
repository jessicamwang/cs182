from selenium import webdriver

def chooseMove(moveName):
	driver.find_element_by_css_selector('[data-move="'+moveName+'"]').click()

def switchPokemon(num):
	driver.find_element_by_css_selector('[name="chooseSwitch"] [value="'+num+'"]').click()

def getChat():
	parentElement = driver.find_element_by_css_selector('.battle-log')
	chatElements = parentElement.find_elements_by_tag_name("div")
	for element in chatElements:
		print element.text

driver = webdriver.Chrome('chrome/chromedriver')
driver.get("http://play.pokemonshowdown.com/battle-randombattle-481132409")
# insert functions

driver.quit()