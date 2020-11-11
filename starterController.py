#!/usr/bin/python3

import json
import serverService

class StarterController:

    def loadConfig():
        configFile = open('config.json')
        configuration = json.load(configFile)
        configFile.close()
        return configuration


    def getServices(self):
        services = self.loadConfig()
