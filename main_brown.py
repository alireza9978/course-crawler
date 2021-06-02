from selenium import webdriver
from selenium.webdriver.support.ui import Select

start = "https://cab.brown.edu/"
result = []


def extract_instructor_email():
    try:
        temp_result = []
        for temp_ins in browser.find_elements_by_class_name("instructor"):
            temp_result.append(temp_ins.find_element_by_css_selector(".instructor-detail h4 a").text)
        return temp_result
    except Exception as e:
        return None


def extract_instructor_name():
    try:
        temp_result = []
        for temp_ins in browser.find_elements_by_class_name("instructor"):
            temp_result.append(temp_ins.find_element_by_css_selector(".instructor-detail a").text)
        return temp_result
    except Exception as e:
        return None


def extract_prerequisite():
    try:
        temp_result = []
        for temp_ins in browser.find_elements_by_css_selector(".prereq a"):
            temp_result.append(temp_ins.text)
        return temp_result
    except Exception as e:
        return None


def extract_courses_info(department_name):
    course_dict = {
        "Course title": browser.find_element_by_css_selector(".text.col-8.detail-title.text--huge").text,
        "Department": department_name,
        "Abbreviation": "BROWN",
        "Professor": extract_instructor_name(),
        "Professor Homepage": extract_instructor_email(),
        "Prerequisite": extract_prerequisite(),
        "Description": "Description",
        "References": "References"
    }

    result.append(course_dict)


def clrawl_department(name):
    browser.implicitly_wait(1)
    panel = browser.find_elements_by_class_name("panel__body")[1]
    for temp_course in panel.find_elements_by_class_name("result--group-start")[:-1]:
        temp_course.find_element_by_class_name("result__title").click()
        extract_courses_info(name)


browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
browser.get(start)
browser.find_element_by_xpath("//select[@id='crit-srcdb']/option[text()='Spring 2021']").click()

select_box_for_text = browser.find_element_by_xpath("//select[@id='crit-dept']")
select_box = Select(select_box_for_text)
# if your select_box has a name.. why use xpath?.....
# this step could use either xpath or name, but name is sooo much easier.

options = [x for x in select_box_for_text.find_elements_by_tag_name("option")]
temp = 0
for i in options[1:5]:
    browser.execute_script("document.getElementById('crit-dept').value = '{}'".format(i.get_attribute("value")))
    browser.execute_script("document.getElementById('search-button-sticky').click()")
    clrawl_department(i.text)
    print(i)


for item in result:
    print(item)
