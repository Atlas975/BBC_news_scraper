
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class ScrapeTool():
    def __init__(self, browser = "chrome",url= "https://www.google.com"):
        self.path = "/home/adilw/Dropbox/Adil_Code/WebDrivers/" # path to web driver file, webdriver name appended
        self.url=url
        match(browser.lower()):
            case "chrome":
                self.path += "chromedriver"
                try:
                    self.driver = webdriver.Chrome(service = Service(executable_path = self.path))
                except Exception:
                    print("Chrome driver not found in file path")
            case "edge":
                self.path += "msedgedriver"
                try:
                    self.driver = webdriver.Edge(sevice = Service(executable_path = self.path))
                except Exception:
                    print("Edge driver not found in file path")
            case "firefox":
                self.path += "geckodriver"
                try:
                    self.driver = webdriver.Firefox(service = Service(executable_path = self.path))
                except Exception:
                    print("Firefox driver not found in file path")

    def search(self):
        try:
            self.driver.get(self.url)
        except Exception:
            print("Invalid URL input")

    def url_append(self, argument, replace = False):
        if(replace):
            self.url_remove()
        self.url += f"/{argument}"

    def url_remove(self,depth=1):
        for _ in range(depth):
            cutoff = self.url.rfind("/")
            self.url = self.url[:cutoff]

    def findelement(self):
        self.driver.find_elements()








