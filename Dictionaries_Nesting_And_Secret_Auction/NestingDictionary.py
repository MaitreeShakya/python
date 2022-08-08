print("***Welcome to the Nesting Dictionary")

travel_log = {"France": ["Paris", "Lille", "Dijon"], "Germany": ["Berlin", "Hamburg", "Stuttgart"]}

city_dictionary = {}

travel_list = []

for country in travel_log:
    cities = travel_log[country]
    city_dictionary["country"] = country
    city_dictionary["cities_visited"] = cities
    city_dictionary["total_visits"] = 12
    travel_log[country] = city_dictionary
    travel_list.append(city_dictionary)
    city_dictionary = {}
  


print(travel_list)
