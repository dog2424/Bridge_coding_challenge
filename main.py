from geopy.geocoders import Nominatim
from models import terminal
from engine import dist_calculator
from models import point


def main():

    terminalList = terminal.Terminal.getTerminalList()

    loadAddress = input("Please insert the loading Address: ")
    unloadAddress = input("Please insert the loading Address: ")

    geolocator = Nominatim(user_agent="Bridge_coding_challenge")

    loadingLocation = geolocator.geocode(loadAddress)

    unloadingLocation = geolocator.geocode(unloadAddress)

    points = point.Point(loadingLocation.latitude, loadingLocation.longitude)
    shorterLoadTerminal = dist_calculator.calculateClosest(
        terminalList, points)

    points = point.Point(unloadingLocation.latitude,
                         unloadingLocation.longitude)
    shorterUnloadTerminal = dist_calculator.calculateClosest(
        terminalList, points)

    print(shorterLoadTerminal.id)
    print(shorterUnloadTerminal.id)


main()
