#!/bin/bash
allargs=()
while getopts abcs*: flag; do
    case ${flag} in
    a)
        break
        ;;
    b)
        allargs+=('business')
        ;;
    c)
        allargs+=('culture')
        ;;
    s)
        allargs+=('sport')
        ;;
    esac
done

python -u "/home/adilw/Dropbox/Adil_Code/LinuxScripts/BBC_news_scraper/news_scraper.py"
