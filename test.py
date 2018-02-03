from bs4 import BeautifulSoup
import requests


page = "https://en.wikipedia.org/wiki/Python_(programming_language)"



#this line gets makes the request to given page and sets it to r
r = requests.get(page)

#this line is using bs4 to grab all of the content of the page and saving it in the soup variable to be able to use 
soup = BeautifulSoup(r.content, 'html.parser')

# This line will parse the whole page and prints it out to the command line 
#print(soup.prettify())

# This line parses the title of given document and prints it out to the command line 
print(soup.title)



