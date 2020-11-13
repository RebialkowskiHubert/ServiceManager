#!/usr/bin/python3

import subprocess

class ServerService:

    ServiceStatus = {
        'INACTIVE': 'Zatrzymany',
        'ACTIVE': 'Uruchomiony',
        'WAITING': 'Oczekujący', 
        'EXITED': 'Zamykany',
        'OTHER': 'Nieznany'
    }

    def __init__(self, serviceName, cmdRun, cmdKill, cmdRestart, cmdStatus):
        self.__serviceName = serviceName
        self.__serviceStatus = self.ServiceStatus['OTHER']
        self.__cmdRun = cmdRun
        self.__cmdKill = cmdKill
        self.__cmdRestart = cmdRestart
        self.__cmdStatus = cmdStatus
        self.__isEnabled = False


    def getServiceName(self):
        return self.__serviceName

    
    def getServiceStatus(self):
        return self.__serviceStatus

    
    def setServiceStatus(self, strStatus):
        self.__serviceStatus = self.ServiceStatus[strStatus]


    def runService(self):
        self.runProcess(self.__cmdRun)
    

    def killService(self):
        self.runProcess(self.__cmdKill)

    
    def restartService(self):
        self.runProcess(self.__cmdRestart)


    def getServiceStatusFromCmd(self):
        return self.runProcess(self.__cmdStatus)

    
    def getEnabled(self):
        return self.__isEnabled


    def setEnabled(self, enabled):
        self.__isEnabled = enabled


    def runProcess(self, cmd):
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output