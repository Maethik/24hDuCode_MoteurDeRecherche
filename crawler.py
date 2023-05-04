from bs4 import BeautifulSoup
import requests
import os, os.path, csv

listingurl = "https://fr.wikipedia.org/wiki/Tabouret"

response = requests.get(listingurl)
soup = BeautifulSoup(response.text, "html.parser")

def getTitle():
    title = soup.find('h1').get_text()
    return title

print(getTitle())

       