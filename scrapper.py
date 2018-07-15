import csv
import urllib2
from bs4 import BeautifulSoup
import subprocess


url = "https://www.dineout.co.in/bangalore-restaurants"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

links = []
ratings = []
locations = []
names = []
all_data = []
results = soup.find_all("div", {"class":"location"})

for result in results:

    locations.append(result.text)

all_links = soup.find_all("a")
for link in all_links:
    links.append(link.get("href"))


total_names = soup.find_all("a", {"data-type": "Name"})
for name in total_names:
    names.append(name.text)

all_ratings = soup.find_all("a", {"data-w-onclick": "reviewLinkClickHandler|w1-restarant"})
for rating in all_ratings:
    ratings.append(rating.text)


all_data.append(names)
all_data.append(locations)
all_data.append(links)
all_data.append(ratings)

print all_data

csvfile = '/Users/sanchi_vinayek/Desktop/axc.csv'

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(all_data)

print open("/Users/sanchi_vinayek/Desktop/axc.csv", 'rt').read()