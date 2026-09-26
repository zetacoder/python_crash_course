def city_country(city, country, population = ""):

    if population == "":
        result = city.title() + ", " + country.title()
    else:
        result = city.title() + ", " + country.title() + " Population " + str(population)

    return result


if __name__ == "__main__":
    city = input("Enter the city name: ")

    country = input("Enter the country name: ")

    population = input("Enter the population for the city: ")

    print(city_country(city, country, population))