from city_functions import city_country

def test_city_country():

    city = 'santiago'

    country = 'chile'

    assert city_country(city=city, country=country) == 'Santiago, Chile'



def test_city_country_population():

    assert city_country("santiago", "chile", "500000") == "Santiago, Chile Population 500000"