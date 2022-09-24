"""

PyTest's classic configuration file for fixtures
We definie a fixture to setup browser and close browser when the test ends
We also pass four different browsers as params
    CR: Chrome
    FF: Firefox
    ED: Edge
    IE: Internet Explorer
Create webdriver options with desired capabilities for each browser type

"""


import pytest
from selenium import webdriver


@pytest.fixture(params=['CR', 'FF', 'ED', 'IE'], scope='class')
def setup_browser(request):

    """
    
    Setup browser with options and desired capabilities
    We also pass four different browsers as params
    CR: Chrome
    FF: Firefox
    ED: Edge
    IE: Internet Explorer
    Launch web browser at remote site - Lambdatest Hub

    """

    lambdatest_usr = "iamramuhere"
    lambdatest_key = "96pQHvrEYTbumnaMY7svaferQRhvdYSknl49M9mPJv59hxpfi9"
    desired_capabilities_cr = {
    "single_test": {
    "browserName": "Chrome",
    "browserVersion": "88.0",
    "LT:Options": {
		"username": "iamramuhere",
		"accessKey": "96pQHvrEYTbumnaMY7svaferQRhvdYSknl49M9mPJv59hxpfi9",
        "visual": True,
        "video": True,
       	"w3c": True,
        "network": True,
        "console": True,
		"build": "YrnrBuild",
		"project": "Lambdatest101Cert",
		"name": "Scenarios123",
		"networkThrottling": "DSL",
        "platformName": "Windows 10",
        "driver_version": "88.0",
		"plugin": "python-pytest"
            }
        }
    }
    desired_capabilities_ff ={
    "single_test": {
    "browserName": "Firefox",
    "browserVersion": "82.0",
    "LT:Options": {
        "username": "iamramuhere",
		"accessKey": "96pQHvrEYTbumnaMY7svaferQRhvdYSknl49M9mPJv59hxpfi9",
        "platformName": "Windows 7",
        "driver_version": "82.0",        
        "visual": True,
        "video": True,
        "w3c": True,        
        "network": True,
        "console": "true",
        "build": "YrnrBuild",
        "project": "Lambdatest101Cert",
		"name": "Scenarios123",
        "networkThrottling": "DSL",
        "plugin": "python-pytest"
            }
        }
    }
    desired_capabilities_ed = {
    "single_test": {
	"browserName": "MicrosoftEdge",
	"browserVersion": "87.0",
	"LT:Options": {
		"username": "iamramuhere",
		"accessKey": "96pQHvrEYTbumnaMY7svaferQRhvdYSknl49M9mPJv59hxpfi9",
		"platformName": "macOS Sierra",
        "driver_version": "87.0",
        "visual": True,
        "video": True,
        "w3c": True,        
        "network": True,
        "console": "true",
        "build": "YrnrBuild",
        "project": "Lambdatest101Cert",
		"name": "Scenarios123",
        "networkThrottling": "DSL",
        "plugin": "python-pytest"
	}
  }
}
    desired_capabilities_ie = {
    "single_test": {
	"browserName": "Internet Explorer",
	"browserVersion": "11.0",
	"LT:Options": {
		"username": "iamramuhere",
		"accessKey": "96pQHvrEYTbumnaMY7svaferQRhvdYSknl49M9mPJv59hxpfi9",
		"platformName": "Windows 10",
        "visual": True,
        "video": True,
        "w3c": True,        
        "network": True,
        "console": "true",
        "build": "YrnrBuild",
        "project": "Lambdatest101Cert",
		"name": "Scenarios123",
        "networkThrottling": "DSL",
        "plugin": "python-pytest"
	}
  }
}
    
    # Create webdriver options with desired capabilities for each browser type
    if request.param == 'CR':
        desired_capabilities = desired_capabilities_cr
        browser_options = webdriver.ChromeOptions()
    if request.param == 'FF':
        desired_capabilities = desired_capabilities_ff
        browser_options = webdriver.FirefoxOptions()
    if request.param == 'ED':
        desired_capabilities = desired_capabilities_ed
        browser_options = webdriver.EdgeOptions()
    if request.param == 'IE':
        desired_capabilities = desired_capabilities_ie
        browser_options = webdriver.IeOptions()
    
    browser_options.set_capability('LT:Options', desired_capabilities)

    # Launch web browser at remote site - Lambdatest Hub
    driver = webdriver.Remote(
        command_executor= f"http://{lambdatest_usr}:{lambdatest_key}@hub.lambdatest.com:80/wd/hub",
        options= browser_options
    )
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # tearDown: close browser after each test case
    driver.quit()
