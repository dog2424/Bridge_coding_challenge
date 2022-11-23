from db.from_db import loadTerminalsFromDB


class Terminal:

    terminalsJSON = loadTerminalsFromDB()

    def __init__(self):

        self.id = ""
        self.lat = ""
        self.lng = ""

    def getTerminalList():
        terminals = Terminal.terminalsJSON
        terminalsObjList = []
        for terminal in terminals:
            tempTerminal = Terminal()
            tempTerminal.id = terminal["terminal"]
            tempTerminal.lat = terminal["address_info"]["lat"]
            tempTerminal.lng = terminal["address_info"]["lng"]

            terminalsObjList.append(tempTerminal)

        return terminalsObjList
