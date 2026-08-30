rivers = {
           "nile" : "egypt",
           "ganga" : "bharat",
           "san jacinto" : "america"
         }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for country in rivers.values():
    print(country.title())


for river in rivers:
    print(river.title())
