# web-scraping-challenge
Homework 12 - Web Scraping Challenge

# Web Scraping Homework - Mission to Mars
Web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### NASA Mars News
Scrapes the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image
Scrapes [here](https://spaceimages-mars.com) for the currently featured image.

### Mars Facts
Uses Pandas to scrape [here](https://galaxyfacts-mars.com) for the table containing facts about the planet including Diameter, Mass, etc. and converts the data to a HTML table string.

### Mars Hemispheres
Uses Splinter to visit [here](https://marshemispheres.com/) and navigate to each of the links to the hemispheres in order to find the image url to the full resolution image.

## Step 2 - MongoDB and Flask Application
Uses MongoDB with Flask to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Python script called `scrape_mars.py` with a function called `scrape` will execute scraping code and return one Python dictionary containing all of the scraped data.

* Route called `/scrape` will import `scrape_mars.py` script and call `scrape` function to store the return value in Mongo as a Python dictionary.

* Route `/` will query Mongo database and pass the Mars data into an HTML template to display the data.

## Rubric
[Unit 12 Rubric - Web Scraping Homework - Mission to Mars](https://docs.google.com/document/d/1paGEIFS5yp2VQu6G8F45B4uj1t1t29zL73KEQrD0xpo/edit?usp=sharing)