# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    ### NASA Mars News
    print('Scraping NASA Mars News...')
    # Scrapes redplanetscience.com for title and body of first article
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    browser.quit()


    ### JPL Mars Space Images - Featured Image
    print('Scraping JPL Mars Space Images - Featured Image...')
    # Scrapes spaceimages-mars.com for the currently featured image url
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = url + soup.find('a', class_='showimg fancybox-thumbs')['href']
    featured_image_title = soup.find('h1', class_="media_feature_title").text
    browser.quit()


    ### Mars Facts
    print('Scraping Mars Facts...')
    # Scrapes galaxyfacts-mars.com for planet profile table
    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)
    mars_df = tables[1]
    mars_df.columns = ["Planet Profile", "Mars"]
    mars_html_table = mars_df.to_html(index=False).replace('\n', '')


    ### Mars Hemispheres
    print('Scraping Mars Hemispheres...')
    # Scrapes marshemispheres.com for image URL of each hemisphere
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres = soup.find_all('div', class_='description')

    hemisphere_image_urls = []

    for each in hemispheres:
        title = each.find('a', class_='itemLink product-item').text.strip().rstrip('Enhanced')
        browser.links.find_by_partial_text(title).click()
        hemi_html = browser.html
        hemi_soup = BeautifulSoup(hemi_html, 'html.parser')
        img_url = url + hemi_soup.find('img', class_='wide-image')['src']
        browser.back()
        
        hemisphere_image_urls.append({
            'title': title,
            'img_url': img_url
        })
        
    browser.quit()

    print('Scraping Complete!')


    scraped_data = {
        'news_title': news_title,
        'news_paragraph': news_p,
        'featured_img_url': featured_image_url,
        'featured_img_title': featured_image_title,
        'mars_table': mars_html_table,
        'hemisphere_img': hemisphere_image_urls,
        }

    return scraped_data