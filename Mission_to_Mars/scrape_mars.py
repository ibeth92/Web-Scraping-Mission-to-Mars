# Import dependencies
# Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

# Set up browser object
def init_browser():
# Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False) 

def scrape():
    browser = init_browser()
    mars = {}

#### NASA Mars News
# Use Splinter to visit the NASA news website to be scraped
# Scrape https://mars.nasa.gov/news/ and collect the latest News Title and Paragraph Text
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Iterate through pages and pull articles
# Create HTML object   
html = browser.html

# Create BeautifulSoup object to parse using html.parser
soup_news = bs(html, 'html.parser')

# Use classes to extract information
# Assign the text to variables that you can reference later
news_title = soup_news.find('div', class_='list_text').find('div', class_='content_title').text
print(f'The most current article on NASA.gov is "{news_title}."')

# Extract the teaser paragraph for the first article
news_p = soup_news.find('div', class_='article_teaser_body').text
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

# Use Pandas to convert the data to a HTML table string
# Define column headers
tables.columns = ['Mars Data', 'Value']

# Save table to files
mars_facts = tables.to_html('mars_facts.html')

# !open mars_facts.html

tables

#### Mars Hemispheres
# Bring in Mars website to be scraped and visit URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Create a list to hold the images and titles.
hemisphere_image_urls = []

# Write code to retrieve the image urls and titles for each hemisphere.
# First, get a list of all of the hemispheres
links = browser.find_by_css("a.product-item h3")

# Next, loop through those links, click the link, find the sample anchor, and return the href
for i in range(len(links)):
    hemisphere = {}
    
# Find the elements on each loop to avoid a stale element exception
    browser.find_by_css("a.product-item h3")[i].click()
    
# Find the Sample image anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first
    sample_elem = browser.links.find_by_partial_text('Sample')
    sample_elem = browser.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
# Get Hemisphere title
    hemisphere['title'] = browser.find_by_css("h2.title").text
    
# Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    
#  Navigate backwards to iterate all 4 images
    browser.back()

    print(len(links))

# Save Hemisphere information to a dataframe
# Iterate image list
hemisphere_image_urls

# Quit the browser
browser.quit()

# Save hemisphere urls to a dataframe
hemisphere_image_urls_df = pd.DataFrame(hemisphere_image_urls)
hemisphere_image_urls_df

mars["title0"] = hemisphere_image['title'][0]
mars["url0"] = hemisphere_image['img_url'][0]
mars["title1"] = hemisphere_image['title'][1]
mars["url1"] = hemisphere_image['img_url'][1]
mars["title2"] = hemisphere_image['title'][2]
mars["url2"] = hemisphere_image['img_url'][2]
mars["title3"] = hemisphere_image['title'][3]
mars["url3"] = hemisphere_image['img_url'][3]

return mars