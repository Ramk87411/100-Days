"""
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
############
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
############
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.
"""

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country,visits,cities):
    new_country = {}
    new_country["country"] =country
    new_country["visits"]  = visits
    new_country["cities"] = cities
    travel_log.append(new_country)


add_new_country(country="Russia", visits=2, cities=["Moscow", "Saint Petersburg"])
print(travel_log)