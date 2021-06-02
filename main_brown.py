import time

from joblib import Parallel, delayed
from selenium import webdriver

start = "https://cab.brown.edu/"


def extract_instructor_email(browser):
    try:
        temp_result = []
        for temp_ins in browser.find_elements_by_class_name("instructor"):
            temp_result.append(temp_ins.find_element_by_css_selector(".instructor-detail h4 a").text)
        return temp_result
    except:
        return None


def extract_instructor_name(browser):
    try:
        temp_result = []
        for temp_ins in browser.find_elements_by_class_name("instructor"):
            temp_result.append(temp_ins.find_element_by_css_selector(".instructor-detail a").text)
        return temp_result
    except:
        return None


def extract_references(browser, ):
    pass


def extract_courses_info(browser, department_name):
    course_dict = {
        "Course title": browser.find_element_by_css_selector(".col-8").text,
        "Department": department_name,
        "Abbreviation": "BROWN",
        "Professor": extract_instructor_name(browser),
        "Professor Homepage": extract_instructor_email(browser),
        "Prerequisite": "as",
        "Description": "Description",
        "References": "References"
    }

    return course_dict


def clrawl_department(browser, name):
    temp_result = []
    time.sleep(0.5)
    panel = browser.find_element_by_css_selector("div.panel__body:nth-child(3)")
    for temp_course in panel.find_elements_by_css_selector("div.result")[:-1]:
        temp_course.find_element_by_class_name("result__title").click()
        time.sleep(0.5)
        temp_result.append(extract_courses_info(browser, name))
    return temp_result


def new_crawler(i):
    browser = webdriver.Firefox()
    browser.get(start)
    browser.find_element_by_xpath("//select[@id='crit-srcdb']/option[text()='Spring 2021']").click()

    select_box_for_text = browser.find_element_by_xpath("//select[@id='crit-dept']")

    options = [x for x in select_box_for_text.find_elements_by_tag_name("option")]
    option = options[i + 1]
    browser.execute_script("document.getElementById('crit-dept').value = '{}'".format(option.get_attribute("value")))
    browser.execute_script("document.getElementById('search-button-sticky').click()")
    temp_result = clrawl_department(browser, option.text)

    browser.close()
    return temp_result


result = Parallel(n_jobs=1)(delayed(new_crawler)(i) for i in range(1, 10))
print(result)
