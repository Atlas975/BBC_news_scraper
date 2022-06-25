import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ScrapeTool():
    def __init__(self,browser="chrome"):
        self.path="/home/adilw/Dropbox/Adil_Code/WebDrivers/" # path to web driver file, webdriver name appended
        match(browser.lower()):
            case "chrome":
                self.path+="chromedriver"
                self.driver=webdriver.Chrome(service=Service(executable_path=self.path))
            case "edge":
                self.path+="msedgedriver"
                self.driver=webdriver.Edge(sevice=Service(executable_path=self.path))
            case "firefox":
                self.path+="geckodriver"
                self.driver=webdriver.Firefox(service=Service(executable_path=self.path))

    def search(self,website="https://www.google.com"):
        try:
            self.driver.get(website)
        except Exception:
            print("Invalid URL input")

    def findelement(self):
        self.driver.find_elements()
        







