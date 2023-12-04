#Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille"], "total_visits":12},
    "Germany": {"cities_visited": ["Hamburg","Berlin", "Stuttgart"], "total_visits":5}
}

#Nesting Dictionary in a List
travel_log1 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille"],
        "total_visits":12
    },
    {
        "country": "Germany",
        "cities_visited": ["Hamburg","Berlin", "Stuttgart"],
        "total_visits":5
    }
]

#Added new dictionary
new_country = {}
def add_new_country(country, times_visited, cities_visited):
    new_country["country"] = country
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travel_log1.append(new_country)

add_new_country("Russia", 2, "Saint Petersburg")
print(travel_log1)