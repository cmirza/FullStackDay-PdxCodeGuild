FreshPoint
=================

### Model
- **~~Clean up JSON data~~**
	- ~~Go through captured JSON data and clean syntax~~
- **~~Model Structure~~**
	- ~~Vegetable Table: Name (string), Type (string), Image (string), Desc (string)~~
	- ~~States Table: Name (string)~~
	- ~~Seasons Table: Vegetable ID, State ID, seasons (string)~~
- **~~Import JSON data into Model~~**
	- ~~Create State table with all 50 states~~
	- ~~Create custom management commands for importing JSON~~
	    - ~~Iterate through JSON, creating an entry for each vegetable in Vegetable table~~
	    - ~~Iterate through JSON, creating entry for each season and ID for each vegetable and state in Seasons table~~
- **~~Verify Model is correct~~**
	- ~~Check if responses from the database are consistent with data in JSON file~~

### View
- **Results Page**
	- ~~Get user zip code from text box~~
	- ~~Pass zip code to Google GeoCode API~~
		- ~~https://developers.google.com/maps/documentation/geocoding/start~~
		- ~~Parse JSON response to get state~~
	- ~~Get Season ID~~
		- ~~Get string of current month, day and year~~
		- ~~Find days in month~~
			- ~~if day < ( days in month / 2 )~~
				- ~~month = current month*2-1~~
			- ~~otherwise~~
				- ~~month = current month*2~~
		- ~~Add leading zero if single digit~~
    - ~~Find vegetables for user~~
    	- ~~Get user's state object from model~~
    	- ~~Filter season data by user's state and current month~~
    	- ~~Iterate over filtered season data~~
    		- ~~Create new list with relevant vegetables from vegetable model~~
    - ~~Pass context to template~~
    - ~~Create warning if item is in last month~~ (27010 for example)
	- ~~Create URL links to detail template~~

### Template
- **Landing Page**
	- Header
	- Input box for zip code
	- Footer
- **Results Page**
	- Header
	- Input box for zip code
	- Google GeoChart highlighting user's state
	- Body wrapper
   	- Multiple DIVs inside flex box
	- Footer

### Enhancements
- **~~Google GeoChart Map Visualization~~**
- **~~Apply Bootstrap CSS framework~~**
- **~~REST API~~**
- **~~Vue.js~~**
- **Edamam Reipe API**




