from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class ScrapeTool():
    def __init__(self, browser = "chrome", url = "https://www.google.com"):
        self.path = "/home/adilw/Dropbox/Adil_Code/WebDrivers/" # path to web driver file, webdriver name appended
        self.url = url
        self.focus = None
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

    def url_append(self, argument, replace_depth = 0):
        return f"{self.url}/{argument}" if replace_depth == 0 else f"{self.url_remove(replace_depth)}/{argument}"

    def url_remove(self, depth = 1):
        for _ in range(depth):
            cutoff = self.url.rfind("/")
            self.url = self.url[:cutoff]
        return self.url

    def element_focus(self, by='xpath', element='//div'):
        self.focus = self.driver.find_elements(by, element)

    def element_text(self,by='xpath',*args):
        return [item.find_element(by,arg).text for item in self.focus for arg in args]


# d
