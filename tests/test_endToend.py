import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkoutPage import CheckoutPage
from pageObjects.confirmPage import ConfirmPage
from pageObjects.homePage import Homepage
from utilities.baseClass import BaseClass


class Testfirst(BaseClass):
    def test_e2e(self):
        homepage = Homepage(self.driver)
        checkoutPage = homepage.shopItems()
        log = self.getlogger()
        allproducts = checkoutPage.productItems()

       # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

#//div[@class='card h-100']/div/h4/a
#product =//div[@class='card h-100']
        for product in allproducts:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
            #Add item into cart
                product.find_element_by_xpath("div/button").click()

        confirmPage = checkoutPage.buttonItems()
        confirmPage.successButtonItems().click()
        confirmPage.countryItems().send_keys("ind")
        self.checkCountryName("India")
        confirmPage.countryNameItems().click()
        confirmPage.PurchaseItems().click()
        successText = confirmPage.ProceedItems().text
        log.info("success text is "+successText)
       # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        #self.driver.find_element_by_id("country").send_keys("ind")

        #self.driver.find_element_by_link_text("India").click()
       # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
       # self.driver.find_element_by_css_selector("[type='submit']").click()
       # successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")


