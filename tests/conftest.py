import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.refresh()
    driver.close()

