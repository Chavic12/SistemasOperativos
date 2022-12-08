class priorityData:

    def __init__(self, idProcess, rafagaCPU, timeLlegada, priority):
        self.idProcess = idProcess
        self.rafagaCPU = rafagaCPU
        self.timeLlegada = timeLlegada
        self.priority = priority
        self.timeWait = 0
        self.returnTime = 0

    def orderPriorityApropiacion(self, orderlist):
        for i in range(len(orderlist) - 1, -1, -1):
            j = i
            while orderlist[j].priority == orderlist[j - 1].priority and i != 0:
                if orderlist[j].timeLlegada < orderlist[j - 1].timeLlegada:
                    objTemp = orderlist[j - 1]
                    orderlist[j - 1] = orderlist[j]
                    orderlist[j] = objTemp
                    j = j + 1
                else:
                    j = j + 1
                if (j > len(orderlist) - 1) or (orderlist[j].priority != orderlist[j - 1].priority):
                    break
        objLlegada = orderlist[len(orderlist) - 2]
        for i in range(len(orderlist) - 1, -1, -1):
            if orderlist[i].timeLlegada <= objLlegada.timeLlegada:
                objLlegada = orderlist[i]
        orderlist.remove(objLlegada)
        orderlist.insert(0, objLlegada)
        return orderlist

    def orderPriority(self, listObjects):
        for i in range(0, len(listObjects)):
            j = i
            while listObjects[j].priority < listObjects[j - 1].priority and j != 0:
                objTemp = listObjects[j - 1]
                listObjects[j - 1] = listObjects[j]
                listObjects[j] = objTemp
                j = j - 1
                if listObjects[j].priority > listObjects[j - 1].priority:
                    break
        return listObjects

    def calculateAverageWaitTime(self,listToCalculate):
        sum = 0
        for i in range(0,len(listToCalculate)):
            sum = listToCalculate[i].timeWait + sum
        return sum/len(listToCalculate)

    def calculateReturnTime(self,lisToCalculateReturn):
        sum = 0
        for i in range(0, len(lisToCalculateReturn)):
            sum = lisToCalculateReturn[i].returnTime + sum
        return sum / len(lisToCalculateReturn)

    def presentationOrderProcess(self,listToOrder):
        sum = 0
        for i in range(0,len(listToOrder)):
            listToOrder[i].timeWait = sum - listToOrder[i].timeLlegada
            sum = listToOrder[i].rafagaCPU + sum
            listToOrder[i].returnTime = sum

    def conversionListObject(self,listOrder):
        listSend=[]
        for i in range(0,len(listOrder)):
            idProce = listOrder[i].idProcess
            rafaga = listOrder[i].rafagaCPU
            timeLlegada = listOrder[i].timeLlegada
            prioridad = listOrder[i].priority
            tiempoEspera = listOrder[i].timeWait
            tiempoRetorno = listOrder[i].returnTime
            listPreSend =[idProce,rafaga,timeLlegada,prioridad,tiempoEspera,tiempoRetorno]
            listSend.append(listPreSend)
        return listSend

    def __str__(self):
        return f"\t{self.idProcess}\t\t\t{self.rafagaCPU}\t\t\t\t{self.timeLlegada}\t\t\t{self.priority}\t\t\t{self.timeWait}\t\t\t{self.returnTime}"



def main(processes, priorities):
    listProcess = []
    t=0
    for i in range(len(processes)):
        obj = priorityData(processes[i][0], processes[i][1], processes[i][2], priorities[i])
        listProcess.append(obj)
        listProcess = obj.orderPriority(listProcess)
    listApropiacion = obj.orderPriority(listProcess)
    listPriority = obj.orderPriorityApropiacion(listApropiacion)
    ordenPresentacion = obj.presentationOrderProcess(listPriority)
    averageTimeWait = obj.calculateAverageWaitTime(listPriority)
    averageTimeReturn = obj.calculateReturnTime(listPriority)
    listSend = obj.conversionListObject(listPriority)
    print("IdProcess\t rafagaCPU\t tiempoLlegada\t prioridad\t tiempoEspera\ttiempoRetorno")
    for i in (listPriority):
        print(i)

    print("Tiempo de espera:",averageTimeWait,"\nTiempo de retorno:",averageTimeReturn)

    result = [averageTimeWait,averageTimeReturn,listSend]
    return result