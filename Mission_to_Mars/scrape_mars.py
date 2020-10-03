# Import dependencies
# Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

# Set up path and browser 
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False) 

def scrape():
    browser = init_browser()
    mars = {}

#### NASA MArs News
# Use Splinter to visit the NASA news website to be scraped
# Scrape https://mars.nasa.gov/news/ and collect the latest News Title and Paragraph Text
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

# Iterate through pages and pull articles
# Create HTML object   
    html=browser.html

# Create BeautifulSoup object to parse using html.parser
    soup = bs(html, 'html.parser')

# Use classes to extract information
# Assign the text to variables that you can reference later
    news_title = soup.find('div', class_='list_text').find('div', class_='content_title').text
    print(f'The most current article on NASA.gov is "{news_title}."')

# Extract the teaser paragraph for the first article
    news_p = soup.find('div', class_='article_teaser_body').text
    print(f'The article, "{news_title}," is about {news_p}')

#### Mars Space Images-------Featured Image
# Import website to be scraped 
# Visit the url for JPL Featured Space Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

# Use splinter to navigate the site and find the image url for the current Featured Mars Image
    full_image = browser.find_by_id('full_image')
    full_image.click()

# Find the more info button and click it
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info = browser.links.find_by_partial_text('more info')
    more_info.click()

# Parse the resulting html with soup
    html = browser.html
    soup_img = bs(html, 'html.parser')

# Assign the url string to a variable called `featured_image_url`
    featured_image_url = soup_img.select_one('figure.lede a img').get("src")
    featured_image_url

#### Mars facts
# Bring in link for Mars Facts scrape
    url = 'https://space-facts.com/mars/'

# Use Pandas to read in facts table from the webpage defined
# Print table
    table_df = pd.read_html(url)
    table_df

# Save table to files and organize in dataframe
    tables = table_df[0]
    tables.set_index(0, inplace=True)
    tables

# Transpose previous dataframe 
    tables = tables.transpose()
    tables

# Bring dataframe into html
    html_table = tables.to_html()
    html_table

#### Mars Hemispheres
# Bring in Mars website to be scraped and visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

# Parse the Hemispheres html with soup
# Create BeautifulSoup object to parse using html.parser
    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('div', class_='item')
    title = []
    img_url = []

# Iterate through Hemisphere pages, visit pages and pull title and image url
    for result in results:
        link = "https://astrogeology.usgs.gov" + result.find('a', class_='itemLink product-item')['href']
        browser.visit(link)
        html = browser.html
        soup = bs(html, 'html.parser')
        page_result = soup.find('div', class_='container')
    
        title. append(page_result.find('h2', class_= 'title').text)
        img_url.append("https://astrogeology.usgs.gov" + page_result.find('img', class_="wide-image")['src'])
        print(title, img_url)

# Save Hemisphere information to a dataframe
    hemisphere_image_urls = pd.DataFrame({
    "title": title,
    "img_url": img_url
    })
    hemisphere_image_urls