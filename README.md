# Overview

In order to show NASA our web app, we want to go one step further and polish it. Adding Mars's hemispheres images into our web app will allow our app to look more refined and thorough. We will scrape full resolution images of Mars's hemispheres (including the titles), store the scraped data on a Mongo database, use a web application to display the data and alter the design of the web app to accommodate the images. Here are the main environments we will be using:

- BeaitifulSoup
- MongoDB
- Python
- PyMongo
- Flask
- Bootstrap
- HTML

### Resources: 

- [Mars Hemisphere Website](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
- [CSS Bootstrap](https://getbootstrap.com/docs/3.3/css/#less)

## Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles

For this part of our project, we will be using BeautifulSoup and Splinter to scrape full-resolution images of Mars's hemispheres and the titles of those images.

In order to get full resolution images and titles for all 4 hemispheres, we created a for loop and stored our findings into a dictionary and added them to our list. For "title" we told soup to scrape through the codes that contained "h2" and class = "title." For our image urls, we used key words like "li" (for link) and "href" that are included in every image element.

![Screen Shot 2022-09-07 at 5 00 44 PM](https://user-images.githubusercontent.com/106577074/189029410-5d42a7e2-f6b6-4ef1-8f26-f37b7e24ce36.png)

## Deliverable 2: Update the Web App with Mars' Hemisphere Images and Titles 

In order to reflect the changes we made in Deliverable 1 by adding Mars' hemisphere images and titles to our code, we now have to reflect the change in our web app. We updated our *scraping.py* and *index.html* to visually reflect these changes to our website. Moreover, we connected MongoDB with the web app so it contains the full-resoluation image URL and title for each hemisphere image. 

Scraping is completed and Robin's web app contains all the information from this module and challenge as we've added full-resolution images and titles for the four hemisphere images. 

### Results 

![Screen Shot 2022-09-07 at 8 49 21 PM](https://user-images.githubusercontent.com/106577074/189030057-92ab5cdb-bb05-4098-b824-8019e1899738.png)

![Screen Shot 2022-09-07 at 8 49 29 PM](https://user-images.githubusercontent.com/106577074/189030077-74d0f139-0caa-46b6-804e-8333d5f1c11f.png)


