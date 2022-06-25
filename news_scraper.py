from selenium_config import ScrapeTool
# import subprocess as sp
# import argparse



# class BBCscraper():
#     def


if __name__=="__main__":
    # sp.run(["pip", "install", "selenium"])
    # strs=input()
    # print(strs)
    webBot=ScrapeTool("firefox","https://www.bbc.co.uk")
    webBot.search()
    webBot.url_append("Buisness")
    print(webBot.url)
    webBot.url_append("News",True)
    print(webBot.url)


    # parser = argparse.ArgumentParser(description='Pass in news category')



    # args = parser.parse_args()
    # print(args.accumulate(args.integers))

