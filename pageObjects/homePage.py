from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class Homepage:

    shop =(By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.CSS_SELECTOR,"input[name='email']")
    password = (By.CSS_SELECTOR,"input[type='password']")
    gender = (By.CSS_SELECTOR,"select[id='exampleFormControlSelect1']")
    date = (By.CSS_SELECTOR,"input[class='form-control']")
    success = (By.CSS_SELECTOR,"input[class='btn btn-success']")
    def __init__(self, driver):
        self.driver = driver #driver of homepage class

    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return  checkoutPage

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getpassword(self):
        return self.driver.find_element(*Homepage.password)

    def getGender(self):
        return self.driver.find_element(*Homepage.gender)

    def getDate(self):
        return self.driver.find_element(*Homepage.date)

    def getSuccess(self):
        return self.driver.find_element(*Homepage.success)
