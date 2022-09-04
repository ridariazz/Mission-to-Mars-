# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# set executable path in the next cell 
# then, set up the URL NASA Mars News for scraping 

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
# searching for elements with a specific combination of tag (div) and attriute (list_text) 
# telling browser to wait one second before searching for components 
browser.is_element_present_by_css('div.list_text', wait_time=1)

# setting up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
# parent element: this holds all the other elements within it, we reference this when we want to filter search results even further 
slide_elem = news_soup.select_one('div.list_text')

# scraping the data
# chained ".find" onto our previously assigned variable, slide_elem
# = this variable holds a ton of information, look inside that info to find this specific data
slide_elem.find('div', class_='content_title')


# Use the parent element to find the first `a` tag and save it as `news_title`
# .get_text() only the text of the element is returned 
# in this code, we have created a new variable for the title, added the get_text() method and we're searching within the parent element for the title
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL

# this way, when JPL updates its image page, our code will still pull the most recent image 
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# scrpaing the entire table with Pandas' read.html() fxn


# creating a new DF from the HTML table 
# read_html() specifically searches for and returns a list of tables found in the HTML 
df = pd.read_html('https://galaxyfacts-mars.com')[0]

# assign columns to the new DF for additional clarity 
df.columns=['description', 'Mars', 'Earth']

# we're turning the description column into the DF's index
# inplace=True means that the updated index will remain in place w/out having to readdign the DF to a new variable
df.set_index('description', inplace=True)
df

# convert DF back into HTML-ready code using the .to_html() fxn 
df.to_html()


# end the session
browser.quit()




