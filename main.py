from geopy.geocoders import Nominatim
from models import terminal
from engine import dist_calculator
from models import point


def main():

    # INPUT DATA

    terminalList = terminal.Terminal.getTerminalList()

    loadAddress = input("Please insert the loading Address: ")
    unloadAddress = input("\nPlease insert the loading Address: ")

    geolocator = Nominatim(user_agent="Bridge_coding_challenge")

    loadingLocation = geolocator.geocode(loadAddress)

    if loadingLocation is None:
        raise Exception(loadAddress + " not found")

    unloadingLocation = geolocator.geocode(unloadAddress)

    if unloadingLocation is None:
        raise Exception(unloadAddress + " not found")

    points = point.Point(loadingLocation.latitude, loadingLocation.longitude)
    shorterLoadTerminal = dist_calculator.calculateClosest(
        terminalList, points)

    points = point.Point(unloadingLocation.latitude,
                         unloadingLocation.longitude)
    shorterUnloadTerminal = dist_calculator.calculateClosest(
        terminalList, points)

    # OUTPUT DATA

    print("\n----------------------------------------------------------------------")
    print("\nThe closest train terminals to " +
          loadAddress + " is: "+shorterLoadTerminal.id)

    loadTerminalInfo = terminal.Terminal.getTerminalById(
        shorterLoadTerminal.id)

    print("\nSome terminal Info: " + loadTerminalInfo.address,
          loadTerminalInfo.terminalOperator, loadTerminalInfo.phone, loadTerminalInfo.zipcode+"\n")
    print("-------------------------------")
    print("\nThe closest train terminals to " +
          unloadAddress + " is: "+shorterUnloadTerminal.id)

    unloadTerminalInfo = terminal.Terminal.getTerminalById(
        shorterUnloadTerminal.id)

    print("\nSome terminal Info: " + unloadTerminalInfo.address,
          unloadTerminalInfo.terminalOperator, unloadTerminalInfo.phone, unloadTerminalInfo.zipcode+"\n")
    print("----------------------------------------------------------------------")


main()
