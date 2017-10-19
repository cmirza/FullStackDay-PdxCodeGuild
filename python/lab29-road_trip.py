'''
Lab 29 - Road Trip
'''

# Dictionary of cities and cities they're accessible to
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

# List of cities accessible in two hops
dest_cities = []


# Road trip function - Create a dict of cities accessible in one hop. Loop through list of one hop cities while
# looping through that cities destinations. If that city is in the one hop cities, skip it. If that city is selected
# city, skip it. Otherwise, add it to the two hop cities. Then return list of two hop cities.
def road_trip(city):
    hop_cities = city_to_accessible_cities[city]
    for cities in hop_cities:
        for hop_city in city_to_accessible_cities[cities]:
            if hop_city in hop_cities:
                continue
            if hop_city == city:
                continue
            elif hop_city not in dest_cities:
                dest_cities.append(hop_city)
    return dest_cities


# Prompt for current city, pass to function then print result.
print(road_trip(input("What city are you in: ")))
