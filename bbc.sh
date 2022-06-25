#!/bin/bash
allargs=()
while getopts abcd*: flag; do
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
    d)
        allargs+=('sport')
        ;;
    esac
done

# printf "%s\n" "${allargs[@]}" | python3 ./news_scraper.py
python3 news_scraper.py "aaa"
python -u "news_scraper.py" &&  echo "${allargs[*]}"

