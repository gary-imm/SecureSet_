#!/usr/bin/python3
#Very basic Web Crawler
#Code template from SecureSet
import re
import requests

#website = input("Give me the FULL website address to crawl: ")
#Provide website, retrieve GET info from site
website = 'http://10.0.0.53/index2.php'
page = requests.get(website)

#Create empty list to be populated with unique sites
#Use regex to find http(s) sites on the site GET html
#****I was more successful with "page.content.decode" than just with "page.text"
visited_sites_or_something = []
mega_match = re.findall('https?:[^"]*', page.content.decode())

#print the first crawl, then continue crawling
print(mega_match)
print("...Let's keep crawling...")

#Loop to go for each item found in initial crawl, grab the GET page, search for http content, and
#add that to mega_match
#This should allow us to not repeat pages already crawled
for item in mega_match:
    visited_sites_or_something.append(item)
    new_page = requests.get(item)
    new_match = re.findall('https?:[^"?]*', new_page.content.decode())
    mega_match.extend(new_match)
#Defensive coding == vs >=...otherwise this crawl will go forever if we don't limit it
    if len(visited_sites_or_something) >= 10:
        break
print(visited_sites_or_something)