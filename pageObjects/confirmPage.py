from selenium.webdriver.common.by import By


class ConfirmPage:

    successButton = (By.XPATH, "//button[@class='btn btn-success']")
    country = (By.ID, "country")
    countryName=(By.LINK_TEXT,"India")
    Buy = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    Purchase = (By.CSS_SELECTOR,"[type='submit']")
    Proceed = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver



    def successButtonItems(self):
        return self.driver.find_element(*ConfirmPage.successButton)

    def countryItems(self):
        return self.driver.find_element(*ConfirmPage.country)

    def countryNameItems(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def BuyItems(self):
        return self.driver.find_element(*ConfirmPage.Buy)

    def PurchaseItems(self):
        return self.driver.find_element(*ConfirmPage.Purchase)

    def ProceedItems(self):
        return self.driver.find_element(*ConfirmPage.Proceed)