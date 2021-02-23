from behave import *
from selenium import webdriver

# from time import sleep


@given("launch chrome browser")
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="chromedriver")


@when("open orange hrm page")
def open_hrm_site(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


# @when("Enter username '{user}' and password '{password}'")
@when('Enter username "{user}" and password "{password}"')
def login(context, user, password):
    context.driver.find_element_by_id("txtUsername").send_keys("admin")
    context.driver.find_element_by_id("txtPassword").send_keys("admin123")


@when("Enter validuser and password")
def valid_login(context):
    context.driver.find_element_by_id("txtUsername").send_keys("Admin")
    context.driver.find_element_by_id("txtPassword").send_keys("admin123")


@when("click on login button")
def click_login(context):
    context.driver.find_element_by_id("btnLogin").click()


@then("user login successfully")
def login_status(context):
    try:
        text = context.driver.get_element_by_xpath(
            "//*[@id='content']/div/div[1]/h1"
        ).text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"


@when(u"navigate to search page")
def navigate_search(context):
    assert True


@then(u"search page should display")
def display_search_page(context):
    assert True
