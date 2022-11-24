from db.from_db import loadTerminalsFromDB


class Terminal:

    terminalsJSON = loadTerminalsFromDB()

    def __init__(self):

        self.id = ""
        self.modesServed = ""
        self.terminalOperator = ""
        self.address = ""
        self.phone = ""
        self.web = ""
        self.openingHours = ""
        self.lat = ""
        self.lng = ""
        self.zipcode = ""
        self.country = ""
        self.region = ""
        self.city = ""
        self.state = ""

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

    def getTerminalById(id):
        terminal = list(filter(lambda x: x.get(
            "terminal") == id, Terminal.terminalsJSON))

        # check if terminal id exist
        if len(terminal) < 1:
            raise Exception("ID not found")

        tempTerminal = Terminal()
        tempTerminal.id = terminal[0]["terminal"]
        tempTerminal.modesServed = terminal[0]["Modes Served"]
        tempTerminal.terminalOperator = terminal[0]["Terminal Operator"]
        tempTerminal.address = terminal[0]["Address"]
        tempTerminal.phone = terminal[0]["Phone"]
        tempTerminal.web = terminal[0]["Web"]
        tempTerminal.lat = terminal[0]["address_info"]["lat"]
        tempTerminal.lng = terminal[0]["address_info"]["lng"]
        tempTerminal.zipcode = terminal[0]["address_info"]["zipcode"]
        tempTerminal.country = terminal[0]["address_info"]["country"]

        return tempTerminal
