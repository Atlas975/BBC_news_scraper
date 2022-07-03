from selenium_config import ScrapeTool
from colorama import Fore,Style

import sys
from IPython.core import ultratb
sys.excepthook = ultratb.FormattedTB(mode='Context', color_scheme='Linux', call_pdb=None)

class BBCscraper(ScrapeTool):
    def __init__(self,browser="chrome"):
        ScrapeTool.__init__(self,browser, "https://www.bbc.com/news")
        self.focus='//div[@class="gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m"]'
        self.titleLoc='./div/a/h3'
        self.subtitleLoc='./div/p'
        self.urlLoc='./div/a'

    def get_summary(self):
        titles=self.element_extract('xpath',self.focus,self.titleLoc)
        subtitles=self.element_extract('xpath',self.focus,self.subtitleLoc)
        return titles,subtitles

    def __str__(self):
        return "BBCbot"

if __name__=="__main__":
    bbcbot=BBCscraper("firefox")
    print(f"\n{Fore.BLUE}BBC Articles\n")
    titles,subtitles=bbcbot.get_summary()
    for title,subtitle in list(zip(titles,subtitles)):
        print(f'{Fore.GREEN}{title}\n{Style.RESET_ALL}{subtitle}\n')
        


