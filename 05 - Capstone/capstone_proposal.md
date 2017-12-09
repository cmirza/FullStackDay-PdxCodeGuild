Capstone Proposal
=================

### Product Name

- Local Nature
- Fresh Finder

### Project Overview

The goal of the project is to take a user's zip code to find their county then reference a database of produce with counties each plant is grown in and time of year it's in season. The user will the receive a list of all the produce available to them within a specified radius. The point of the project is to advise users on what produce to buy that can be locally sourced.

### Functionality

1. Landing page with text box for zip code entry and finds their county
2. View sorts all counties within specified radius from user's county
3. View finds all produce applicable for list of counties
4. View filters produce by seasonality using current date
5. Data is sorted by distance to user's zip code
6. Data is displayed as a list to user
7. Pass list to map API and plot it on a map displayed to user

### Data Model

- Primary model of Counties
    - many to many relationship with individual produce
    - Produce model has in season dates

#### Sources

- USDA NASS Quick Stats (https://quickstats.nass.usda.gov/api)
- Manually lookup seasonality in Wikipedia

### Components

- Build small app that captures JSON from USDA NASS Quick Stats to populate model

- Web Framework
    - Django
- Model
    - PostgreSQL
- JS Framework
    - React
- CSS Framework
    - Material
- Map API
    - Google Maps
- Deployment 
    - AWS Elastic Beanstalk

### Schedule

- **Milestone 1**
    - Find relevant data with API or scrape data from other sources
    - Build model with appropriate data
        1. Portland Metro
        2. Greater Oregon
        3. Seattle/Tacoma Metro
        4. Greater Washington
    - Build basic front end
- **Milestone 2**
    - Display data geographically w/ map API
    - Redo front end with JS framework?
- **Milestone 3**
    - Apply CSS framework   
    - Deploy site on AWS or Digital Ocean
- **Milestone 4** (post-class)
    - Find more data sets
    - Use CAERS DB (https://www.fda.gov/Food/ComplianceEnforcement/ucm494015.htm) for alerts on unsafe foods
    - Allow email signups where monthly updates of 'whats fresh' is listed
    - Find recipe API, supply recipes for each item listed
