from selenium_config import ScrapeTool

class BBCscraper(ScrapeTool):
    def __init__(self,browser="chrome"):
        ScrapeTool.__init__(self,browser, "https://www.bbc.com/news")
        # self.element_focus('xpath','//div[@class="gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m"]')
        # self.titleLoc='//div//a//h3'
        # self.subtitleLoc='//div//p'

    def get_article(self):
        return self.element_text('xpath',self.titleLoc,self.subtitleLoc)




    def article_titles(self):
        pass



if __name__=="__main__":
    bbcbot=BBCscraper("firefox")
    # bbcbot.search()
    # BBCscraper.get_article('xpath','//div[@class="gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m"]')

    # for i in bbcbot.get_article():
    #     print(i)


    # parser = argparse.ArgumentParser(description='Pass in news category')



    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

