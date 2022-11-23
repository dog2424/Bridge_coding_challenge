from geopy.geocoders import Nominatim


def main():

    loadAddress = input("Please insert the loading Address: ")
    unloadAddress = input("Please insert the loading Address: ")

    geolocator = Nominatim(user_agent="Bridge_coding_challenge")

    loadingLocation = geolocator.geocode(loadAddress)

    unloadingLocation = geolocator.geocode(unloadAddress)

    print((loadingLocation.latitude, loadingLocation.longitude))
    print((unloadingLocation.latitude, unloadingLocation.longitude))


main()
