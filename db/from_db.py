import os
import json


def loadTerminalsFromDB():

    with open(os.path.join("data", "result_w_address.json"), "r") as terminalsDB:
        terminals = json.load(terminalsDB)

    return terminals
