# Overview

In order to show NASA our web app, we want to go one step further and polish it. Adding Mars's hemispheres images into our web app will allow our app to look more refined and thorough. We will scrape full resolution images of Mars's hemispheres (including the titles), store the scraped data on a Mongo database, use a web application to display the data and alter the design of the web app to accommodate the images. Here are the main environments we will be using:

- BeaitifulSoup
- MongoDB
- Python
- PyMongo
- Flask
- Bootstrap
- HTML

## Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles 

For this part of our project, we will be using BeautifulSoup and Splinter to scrape full-resolution images of Mars's hemispheres and the titles of those images. 

In order to get full resolution images and titles for all 4 hemispheres, we created a for loop and stored our findings into a dictionary and added them to our list. For "title" we told soup to scrape through the codes that contained "h2" and class = "title." For our image urls, we used key words like "li" (for link) and "href" that are included in every image element.

![Screen Shot 2022-09-07 at 5 00 44 PM](https://user-images.githubusercontent.com/106577074/189005350-eb766fe1-09a1-4e67-bbb3-f86c520af9dc.png)
