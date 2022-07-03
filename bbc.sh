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

farbros 
python -u news_scraper.py

# printf "%s\n" "${allargs[@]}" | python3 ./news_scraper.py

# python -u "news_scraper.py" &&  echo "${allargs[*]}"

# echo "${allargs[*]}"
