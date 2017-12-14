Capstone Proposal
=================

### Product Name

- **FreshPoint**

### Project Overview

The goal of the project is to take a user's zip code to find the state they're closest to, then provide a list of produce in that state that is currently season

### Functionality

1. Landing page with text box for zip code entry
2. View finds which state they're closest to
3. View gathers all produce for that state
4. View filters list by current season using current date
5. Data is displayed to user as grid of items with images and description
6. When user clicks on item, a detail view is given with complete season data for the user's state and map view of states in which the item is grown

### Data Model

- Primary model of vegetables
    - many to many relationship with states
    - **issue:** not sure where season months is kept

#### Sources

- NRDC Local Food Systems (https://www.nrdc.org/issues/local-food-systems)

### Components

- **Web Framework**
    - Django
        1. Take user zip code to find user's state
        2. Find all produce for that state
        3. Filter list by items currently in season
- **Model**
    - PostgreSQL (can I initially use SQLite then migrate to PostgreSQL later?)
        - Name of produce
            - Months in season (do I use an Associative Entity: https://en.wikipedia.org/wiki/Associative_entity ?)
        - List of US states
- **JS Framework**
    - React (not sure how React would fit exactly)
- **CSS Framework**
    - Material-UI
- **Map**
    - Use D3.js to highlight states
        - http://bl.ocks.org/michellechandra/0b2ce4923dc9b5809922
        - https://bl.ocks.org/chucklam/f628765b873d707a3d0e44ffc78deab8
        
- **Deployment**
    - AWS Elastic Beanstalk

### Schedule

- **Milestone 1**
    - Gather data set ✓
    - Import data set into database
    - Implement basic functionality
    - Build basic front end
- **Milestone 2**
    - Implement map in detail view with D3.js
    - Redo front end with JS framework?
- **Milestone 3**
    - Apply CSS framework   
    - Deploy site on AWS
- **Milestone 4** (stretch goals)
    - Use Yummly API to get recipe ideas: https://developer.yummly.com/
    - Allow email signups where monthly updates of 'whats fresh' is listed
