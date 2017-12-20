Capstone Proposal
=================

### Product Name

- **FreshPoint**

### Project Overview

The goal of the project is to take a user's zip code to find the state they're closest to, then provide a list of produce in that state that is currently season

### Functionality

1. Landing page with text box for zip code entry
2. View finds which state they're in
3. View gathers all produce for that state
4. View filters list by current season using date
5. Data is displayed to user as grid of items with images and description
6. When user clicks on item, a detail view is given with season data for the user's state and map of states in which the item is grown

### Data Model

- Vegetable Model
    - name, type, image, description
- US states Model
    - state name
- Seasons Model
    - Vegetable ID, State ID, seasons (string)

#### Sources

- NRDC Local Food Systems (https://www.nrdc.org/issues/local-food-systems)

### Components

- **Web Framework**
    - Django
        - Get location (Google GeoCode API (https://developers.google.com/maps/documentation/geocoding/start))
        - Find all produce for that state
        - Filter list by items currently in season
- **Model**
    - PostgreSQL (can I initially use SQLite then migrate to PostgreSQL later?)
- **JS Framework**
    - React
- **CSS Framework**
    - Material-UI
- **Map**
    - Google GeoCharts https://developers.google.com/chart/interactive/docs/gallery/geochart
- **Deployment**
    - AWS Elastic Beanstalk

### Schedule

- **Milestone 1**
    - Gather data
    - Create database
    - Implement basic functionality
    - Build basic front end
- **Milestone 2**
    - Create detail view for each vegetable
    - Redo templates with Material-UI
    - Move database to PostgreSQL
- **Milestone 3**
    - Rework site with React to implement single page functionality
    - Deploy site on AWS
- **Milestone 4**
    - Use Yummly API to get recipe ideas: https://developer.yummly.com/
    - Create email newsletter function
