def city_country(city, country):
    return city.title() + ", " + country.title()


if __name__ == "__main__":
    city = input("Enter the city name: ")

    country = input("Enter the country name: ")

    print(city_country(city, country))