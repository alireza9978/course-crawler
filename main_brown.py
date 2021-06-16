import time
from functools import reduce
import datetime
import pandas as pd
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


def extract_prerequisites(browser: webdriver.Firefox):
    pass


def extract_references(browser: webdriver.Firefox):
    pass


def extract_description(browser: webdriver.Firefox):
    try:
        return browser.find_element_by_css_selector(".section--description .section__content").text
    except:
        return None


def extract_courses_info(browser, department_name):
    course_dict = {
        "University": None,
        "Abbreviation": "BROWN",
        "Department": department_name,
        "Course title": browser.find_element_by_css_selector(".col-8").text,
        "Professor": extract_instructor_name(browser),
        "Objective": None,
        "Prerequisite": None,
        "Required Skills": None,
        "Outcome": None,
        "References": None,
        "Scores": None,
        "Description": extract_description(browser),
        "Projects": None,
        "University Homepage": "https://www.brown.edu/",
        "Course Homepage": None,
        "Professor Homepage": extract_instructor_email(browser),
    }
    return course_dict


def crawl_department(browser, name):
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
    try:
        browser.get(start)
        browser.find_element_by_xpath("//select[@id='crit-srcdb']/option[text()='Spring 2021']").click()

        select_box_for_text = browser.find_element_by_xpath("//select[@id='crit-dept']")

        options = [x for x in select_box_for_text.find_elements_by_tag_name("option")]
        option = options[i]
        browser.execute_script(
            "document.getElementById('crit-dept').value = '{}'".format(option.get_attribute("value")))
        browser.execute_script("document.getElementById('search-button-sticky').click()")
        temp_result = crawl_department(browser, option.text)
        browser.close()
        return temp_result
    except Exception as e:
        browser.close()
        return []


result = Parallel(n_jobs=2)(delayed(new_crawler)(i) for i in range(1, 3))
result = reduce(lambda x, y: x + y, result)
result = pd.DataFrame(result)
result.to_csv("brown_courses_{}.csv".format(str(datetime.datetime.now())), index=False)
