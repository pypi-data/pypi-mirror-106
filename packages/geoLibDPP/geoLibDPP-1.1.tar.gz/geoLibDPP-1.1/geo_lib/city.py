class City:
    def __init__(self, name, country, region, latitude, longitude, population, timezone):
        self.name = name
        self.country = country
        self.region = region
        self.latitude = latitude
        self.longitude = longitude
        self.population = population
        self.timezone = timezone

    def __str__(self):
        return f"{self.name}, a city located in {self.country}, in the {self.region} region. " \
               f"Its geographical coordinates are {self.latitude}, {self.longitude}. " \
               f"It is inhabited by {self.population} people. It is in the {self.timezone} time zone."
