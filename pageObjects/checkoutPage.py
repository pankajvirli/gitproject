from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckoutPage:
    product = (By.XPATH, "//div[@class='card h-100']")
    text = (By.XPATH, "div/h4/a")
    button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def productItems(self):
        return self.driver.find_elements(*CheckoutPage.product)

    def textItems(self):
        return self.driver.find_element(*CheckoutPage.text)

    def buttonItems(self):
        self.driver.find_element(*CheckoutPage.button).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

