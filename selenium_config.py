from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ServiceConfig():
    def __init__(self,browser="chrome"):
        self.path="/home/adilw/Dropbox/Adil_Code/WebDrivers/"
        match(browser.lower()):
            case "chrome":
                self.path+="chromedriver"
                self.driver=webdriver.Chrome(executable_path=Service(executable_path=self.path))
            case "firefox":
                self.path+="geckodriver"
                self.driver=webdriver.Firefox(service=Service(executable_path=self.path))

    def search(self,website="https://www.google.com"):
        try:
            self.driver.get(website)
        except Exception:
            print("Invalid URL input")







