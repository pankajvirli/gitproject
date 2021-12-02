import pytest
from select import select
from selenium.webdriver.support.select import Select

from pageObjects.homePage import Homepage
from testdata.test_homePageData import TestFormData
from utilities.baseClass import BaseClass
from selenium import webdriver


class TestForm(BaseClass):

    def test_submitForm(self, fields):
        homepage = Homepage(self.driver)

        homepage.getName().send_keys(fields["firstName"])
        homepage.getEmail().send_keys(fields["Email"])
        homepage.getpassword().send_keys("abc123")
        self.selectOption(homepage.getGender(), fields["gender"])
        homepage.getDate().send_keys("2020-01-01")
        homepage.getSuccess().click()
        print("update from gt1 ")
        print("update from gt1 ")
        print("update from gt1 ")
        print("update from gt1 ")
    @pytest.fixture(params=TestFormData.test_form_data)
    def fields(self, request):
        return request.param
