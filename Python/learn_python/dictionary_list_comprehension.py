cities = ['Dhaka', 'Mumbai', 'Paris']
countries = ['Bangladesh', 'India', 'France']

z = zip(cities, countries)  # zip returns tuple, i.e., (cities, countries) -> ('Dhaka', 'Bangladesh')

dictionary = {city: country for city, country in z}

print(dictionary)
