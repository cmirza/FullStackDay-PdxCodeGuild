FreshPoint
=================

### Model

- **Clean up JSON data**
	- ~~Go through captured JSON data and clean syntax~~
- **Model Structure**
	- Vegetable Table: Name (string), Type (string), Image (string), Desc (string)
	- States Table: Name (string)
	- Seasons Table: Vegetable ID, State ID, seasons (string)
- **Import JSON data into Model**
	- Use this method: https://stackoverflow.com/questions/8367609/most-elegant-approach-for-writing-json-data-to-a-relational-database-using-djang
	- create State table with all 50 state
	- iterate through JSON, creating an entry for each vegetable in Vegetable table
	- iterate through JSON, creating entry for each season and ID for each vegetable and state in Seasons table
- **Verify Model is correct**
	- Check if responses from the database are consistent with data in JSON file

### View

- **Get User Location**
	- Get user zip code from text box
	- Pass zip code to Google GeoCode API
		- https://developers.google.com/maps/documentation/geocoding/start
	- Parse JSON response to get state
- **Find vegetables for user**
	- Filter Seasons table by user's state
	- Get Season ID
		- Get string of current month
			- if day < ( days in month / 2 )
				- append 'early'
			- if day > ( days in month / 2 )
				- append 'late'
		- Filter Season ID dict to get current Season ID
	- Filter Seasons table again my Season ID
- **Populate results page**
	- Create context object for 'name', 'type', 'image' and 'description'
	- Render results template with context

### Template

- **Landing Page**
	- Header
	- Input box for zip code
	- Footer

- **Results Page**
	- Header
	- Input box for zip code
	- Body wrapper
   	- Multiple DIVs inside flex box
	- Footer

- **Detail Page**
	- Google GeoChart for states vegetable is grown in
	- Table with months vegetable is grown in user's state
	- Picture, type and description of vegetable
