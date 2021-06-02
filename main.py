from selenium import webdriver
from selenium.webdriver.support.ui import Select

start = "https://cab.brown.edu/"

browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
browser.get(start)

select = Select(browser.find_element_by_id("seligo-container"))
select.select_by_index(0)
select.select_by_visible_text('Africana Studies')
# elem = browser.find_element_by_id()
# elem.click()

# browser.switch_to.frame('ptifrmtgtframe')
#
# elem = browser.find_element_by_xpath('//*[@id="DERIVED_SSS_BCC_SSR_ALPHANUM_M"]')
# elem.click()

# browser.execute_script("submitAction_win0(document.win0,'DERIVED_SSS_BCC_SSR_ALPHANUM_M');")

# browser.quit()
