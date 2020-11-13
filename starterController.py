#!/usr/bin/python3

import json
from serverService import ServerService

class StarterController:

    servicesList = []

    def getServices(self):
        self.servicesList.clear()
        configList = self.loadConfig()
        if len(configList) == 0:
            return None

        servicesStrList = configList['services']

        if len(servicesStrList) == 0:
            return None

        for serv in servicesStrList:
            service = ServerService(serv['serviceName'], serv['cmdRun'], serv['cmdKill'], serv['cmdRestart'], serv['cmdStatus'])
            self.getActualStatus(service)
            self.servicesList.append(service)

        return self.servicesList


    def loadConfig(self):
        configFile = open('config.json')
        configuration = json.load(configFile)
        configFile.close()
        return configuration


    def getActualStatus(self, service):
        status = str(service.getServiceStatusFromCmd())
        info = status.split(';')
        service.setEnabled('TAK' if info[1] == 'enabled' else 'NIE')
        state = info[2].split(':')
        service.setServiceStatus(state[2].split(' ', 2)[1].upper())