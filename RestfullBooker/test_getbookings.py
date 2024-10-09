#Validate request - GetBookingsAPI

import pytest
import allure
import requests


@pytest.mark.smoke
@allure.title("Validate GetBooking URL")
@allure.description("Test Case #1")
@allure.testcase("TC01")
def test_getbookings():
    url = "https://restful-booker.herokuapp.com/booking/"
    response = requests.get(url)
    print(response.text)
    print(response.status_code)

@pytest.mark.regression
@allure.title("Validate Negative Test")
@allure.description("Test Case #2")
@allure.testcase("TC02")
def test_getbookingsnegative():
    url = "https://restful-booker.herokuapp.com/booking/abc"
    response = requests.get(url)
    print(response.text)
    assert(response.status_code == 200)

