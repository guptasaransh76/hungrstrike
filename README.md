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
> Go to http://localhost:3000/foods

## Python Files
* BeautifulSoup was used to scrap data like restaurant names, url, location and ratings from Dinout - "https://www.dineout.co.in/bangalore-restaurants"

### setup steps:
* pip install beautifulsoup4
* python scrapper.py

## Scrapped data Storage
* data is stored in csv format in the file named "data.csv".

## *Screeshots*

#### Index Page
<img width="1436" alt="screen shot 2018-07-17 at 1 55 02 pm" src="https://user-images.githubusercontent.com/30376024/42805479-8856140c-89c9-11e8-899e-a2e4f7d1690e.png">

#### Show Pages
<img width="1434" alt="screen shot 2018-07-17 at 1 55 26 pm" src="https://user-images.githubusercontent.com/30376024/42805481-8887a94a-89c9-11e8-9ee2-bd748c052e83.png">

<img width="1433" alt="screen shot 2018-07-17 at 1 56 58 pm" src="https://user-images.githubusercontent.com/30376024/42805482-88b0e1b6-89c9-11e8-9261-8f4b4e9080fe.png">

<img width="1437" alt="screen shot 2018-07-17 at 1 57 16 pm" src="https://user-images.githubusercontent.com/30376024/42805483-88e3e264-89c9-11e8-9115-293db82cedfe.png">

<img width="1437" alt="screen shot 2018-07-17 at 1 57 27 pm" src="https://user-images.githubusercontent.com/30376024/42805484-890e71e6-89c9-11e8-90f8-7fa10c981fc5.png">

<img width="1430" alt="screen shot 2018-07-17 at 1 57 37 pm" src="https://user-images.githubusercontent.com/30376024/42805485-893ca4f8-89c9-11e8-8747-a108704bc491.png">
