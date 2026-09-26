from city_functions import city_country

def test_city_country():

    city = 'santiago'

    country = 'chile'

    assert city_country(city=city, country=country) == 'Santiago, Chile'
