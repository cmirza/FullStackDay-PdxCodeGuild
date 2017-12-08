Capstone Proposal
=================

### Product Name

- Local Nature
- Fresh Finder

### Project Overview

The goal of the project is to take a user's zip code then reference a database of fresh produce with zip codes each plant is grown in and time of year it's in season for that area. The point of the project is to advise users on what produce to buy that can be locally sourced.

### Functionality

1. Landing page with text box for zip code entry
    - Either static definition of local (250mi) or allow user to choose radius
2. View sorts all zip codes within specified radius from user's zip code
3. View finds all produce applicable for list of zip codes
4. View filters produce by seasonality using current date
5. Data is sorted by distance to user's zip code
6. Data is displayed as a list to user
7. Pass list to map API and plot it on a map displayed to user

### Data Model

- Primary model of Zip Codes
    - many to many relationship with individual produce
    - Produce model has in season dates
    
- For calculating distance between zip codes (http://code.activestate.com/recipes/393241-calculating-the-distance-between-zip-codes/) 

#### Sources

- USDA
    - USDA Census of Agriculture
        - issue: data is county level
- FDA
- _Issue:_ Contacted OSU, PSU & UofO dept. of Agriculture for assistance in finding data sources

### Components

- Data Scraping
    - Beautiful Soup (https://www.crummy.com/software/BeautifulSoup/)
- Model
    - PostgreSQL
- Django
    - Pagination
    - REST Framework? (would I need it if I use JS framework?)
- JS Framework? (would I need it if I use REST framework?)
    - React
    - _Alternative:_ Angular
- CSS Framework
    - Bootstrap
    - _Alternative:_ Material    
- Map API
    - Mapbox (https://www.mapbox.com/api-documentation/)
    - _Alternative:_ Google Maps (https://developers.google.com/maps/)
- Deployment 
    - AWS Elastic Beanstalk (http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)
        - EC2
        - RDS
    - _Alternative:_ Digital Ocean VPS
        - Ubuntu Server
        - Nginx

### Schedule

- **Milestone 1**
    - Find relevant data with API or scrape data from other sources
    - Build model with appropriate data
        1. Portland Metro
        2. Greater Oregon
        3. Seattle/Tacoma Metro
        4. Greater Washington
    - Build basic front end for testing
- **Milestone 2**
    - Expand front end with JS framework
    - Apply CSS framework
- **Milestone 3**
    - Display data geographically w/ map API
    - Deploy site on AWS or Digital Ocean
- **Milestone 4** (post-class)
    - Find more data sets to expand upon
    - Use CAERS DB (https://www.fda.gov/Food/ComplianceEnforcement/ucm494015.htm) for alerts on unsafe foods
    - create links to popular recipes for each item
