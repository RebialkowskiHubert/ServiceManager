#!/usr/bin/python3

class ServerService:

    ServiceStatus = {
        'INACTIVE': 'Zatrzymany',
        'ACTIVE': 'Uruchomiony',
        'WAITING': 'Oczekujący', 
        'EXITED': 'Zamykany',
        'OTHER': 'Nieznany'
    }

    def __init__(self, serviceName, cmdRun, cmdKill, cmdStatus):
        self.__serviceName = serviceName
        self.__serviceStatus = self.ServiceStatus.OTHER
        self.__cmdRun = cmdRun
        self.__cmdKill = cmdKill
        self.__cmdStatus = cmdStatus


    def runService(self):
        exec(self.__cmdRun)
    

    def killService(self):
        exec(self.__cmdKill)


    def getServiceStatus(self):
        return self.__serviceStatus

    
    def getEnabled():
        return 'TAK'