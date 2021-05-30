from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# start = "https://sims.erp.sfu.ca/psc/csprd/EMPLOYEE/SA/c/COMMUNITY_ACCESS.SSS_BROWSE_CATLG.GBL"
start = "https://sims.erp.sfu.ca/psc/csprd/EMPLOYEE/SA/s/WEBLIB_SFU.ISCRIPT1.FieldFormula.IScript_CASSignin"

browser = webdriver.Firefox()
browser.get(start)

elem = browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/div[1]/ul/li[2]/a")
elem.click()

browser.switch_to.frame('ptifrmtgtframe')

elem = browser.find_element_by_xpath('//*[@id="DERIVED_SSS_BCC_SSR_ALPHANUM_M"]')
elem.click()

# browser.execute_script("submitAction_win0(document.win0,'DERIVED_SSS_BCC_SSR_ALPHANUM_M');")

# browser.quit()


