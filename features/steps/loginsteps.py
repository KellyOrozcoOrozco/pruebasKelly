from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
global driver

@given('User launch Chrome browser')
def step_impl(context):
    try:
        print("Abre Chrome")
        context.driver = webdriver.Chrome("C:\chromedriver.exe")
        context.driver.maximize_window()
    except Exception as e:
        print("Error:", e)

@when('User open SwagLabs Login')
def step_impl(context):
    try:
        context.driver.get('https://www.saucedemo.com/')
    except Exception as e:
        print("Error:", e)

@when('User enter username "{username}" and password "{password}"')
def step_impl(context,username,password):
    try:
        sleep(2)
        context.driver.find_element(By.ID, 'user-name').send_keys(username)
        sleep(2)
        context.driver.find_element(By.ID, 'password').send_keys(password)
    except Exception as e:
        print("Error:", e)

@when('User click on login button')
def step_impl(context):
    try:
        sleep(2)
        loginButton = context.driver.find_element(By.ID, 'login-button')
        loginButton.click()
    except Exception as e:
        print("Error:", e)

@when('Select products to add it to the shopping cart')
def step_impl(context):
    try:
        sleep(1)
        product = context.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        product.click()
        sleep(1)
        product2 = context.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
        product2.click()
        sleep(2)
    except Exception as e:
        print("Error:", e)

@when('User clicks on the shopping cart')
def step_impl(context):
    try:
        sleep(1)
        shoppingcar = context.driver.find_element(By.ID, 'shopping_cart_container')
        shoppingcar.click()
        sleep(1)
    except Exception as e:
        print("Error:", e)


@when('User clicks on checkout button')
def step_impl(context):
    checkoutButton = context.driver.find_element(By.ID, 'checkout')
    checkoutButton.click()
    sleep(1)


@when('User enter "{name}" and "{lastname}" and "{postalcode}"')
def step_impl(context,name,lastname,postalcode):
    try:
        sleep(1)
        print('hola')
        context.driver.find_element(By.ID, 'first-name').send_keys(name)
        sleep(1)
        context.driver.find_element(By.ID, 'last-name').send_keys(lastname)
        sleep(1)
        context.driver.find_element(By.ID, 'postal-code').send_keys(postalcode)
        sleep(1)
    except Exception as e:
        print("Error:", e)


@when('User clicks on Continue button')
def step_impl(context):
    try:
        sleep(1)
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        continuebutton = context.driver.find_element(By.ID, 'continue')
        continuebutton.click()
    except Exception as e:
        print("Error:", e)


@when('User clicks on finish button')
def step_impl(context):
    try:
        sleep(1)
        finishbutton = context.driver.find_element(By.ID, 'finish')
        finishbutton.click()
    except Exception as e:
        print("Error:", e)


@when('User clicks on menu logout')
def step_impl(context):
    try:
        sleep(1)
        menubutton = context.driver.find_element(By.ID, 'react-burger-menu-btn')
        menubutton.click()
    except Exception as e:
        print("Error:", e)

@then('User clicks on logout button')
def step_impl(context):
    try:
        sleep(1)
        finishbutton = context.driver.find_element(By.ID, 'logout_sidebar_link')
        finishbutton.click()
        sleep(1)
    except Exception as e:
        print("Error:", e)


