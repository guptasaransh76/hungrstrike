# HungerStrike
It is a Ruby on Rails application that displays restaurant details and displays on a map using google maps.

* Ruby version: 2.5.1
* Rails version: 5.2.0
* Database: Postgresql
* Data Collection: Python (BeautifulSoup4)

## Setup steps:
*  Git clone https://github.com/guptasaransh76/hungrstrike.git
*  bundle install
*  rails db:create 
*  rails db:migrate
*  rails db:seed

* rails server
> Go to http://localhost:3000

## Python Files
* BeautifulSoup was used to scrap data like restaurant names, url, location and ratings from Dinout - "https://www.dineout.co.in/bangalore-restaurants"

### setup steps:
* pip install beautifulsoup4
* python scrapper.py

## Scrapped data Storage
* data is stored in csv format in the file named "data.csv".

*Screeshots*

## Index Page
<img width="1203" alt="screen shot 2018-07-16 at 12 54 30 pm" src="https://user-images.githubusercontent.com/30376024/42747113-8e16410e-88f8-11e8-96c4-a7cd6df8fbc3.png">

## Show Page
<img width="972" alt="screen shot 2018-07-16 at 12 54 58 pm" src="https://user-images.githubusercontent.com/30376024/42747084-7319b818-88f8-11e8-91c0-9ff8273048e2.png">
