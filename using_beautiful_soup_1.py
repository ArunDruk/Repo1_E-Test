# pip install beautifulsoup4
# pip install lxml
# pip install html5lib
# pip install requests

from bs4 import BeautifulSoup
import requests
with open("Jobvite.html") as file_html:
    soup=BeautifulSoup(file_html,'lxml')

#print(soup)
#print(soup.prettify())

#matches=soup.title
#matches=soup.title.text

#matches=soup.div
#matches=soup.find("div",class_="jobvite-clear") # class is a special variable, so we using "class_"

# We can also use like this
# headline = matches.h2.a.text
# summary= matches.p.text
#print(headline)
#print(summary)

matches=soup.find_all("div",class_="jobvite-clear")
print(matches)



