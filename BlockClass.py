class Block():
    def __init__(self):
        self.greenLineRoute = [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,85,84,83,82,81,80,79,78,77,101,102,103,104,105,106,107,108,109,110,111,112,
        113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,
        9,8,7,6,5,4,3,2,1,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]

        self.redLineRoute = [9,8,7,6,5,4,3,2,1,16,17,18,19,20,21,22,23,24,25,26,27]

    lineRoute = []
    yard = False
    

    def initialize(self,line):
        if line == "green":
            self.lineRoute = self.greenLineRoute
            self.yard = False
        elif line == "red":
            self.lineRoute = self.redLineRoute
            self.yard = False

    def greenSwitchYard(self,base,switchBlock):
        #goes into yard
        if base == 57 and switchBlock == 0:
            self.lineRoute.append(0)
            self.yard = True
        elif base == 57 and switchBlock == 58:
            self.lineRoute.append(58)
            self.lineRoute.append(59) 
            self.lineRoute.append(60) 
            self.lineRoute.append(61) 
            self.lineRoute.append(62)
            self.lineRoute.append(self.greenLineRoute) 

    def redSwitchYard(self,base,switchBlock):
        appended = [0]
        #check switch between section H and T
        if base == 27 and switchBlock == 28:
            appended = [28,29,30,31,32,33,34,35,36,37,38]
        elif base == 27 and switchBlock == 76:
            appended = [76,75,74,73,72,33,34,35,36,37,38]
        elif base == 38 and switchBlock == 39:
            appended = [39,40,41,42,43,44,45,46,47,48,49,50,51,52]
        elif base == 38 and switchBlock == 71:
            appended = [71,70,69,68,67,44,45,46,47,48,49,50,51,52]
        elif base == 52 and switchBlock == 53:
            appended = [53,54,55,56,57,58,59,60,61,62,63,64,65,66,52,51,50,49,48,47,46,45,44]
        elif base == 52 and switchBlock == 66:
            appended = [66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44]
        elif base == 44 and switchBlock == 43:
            appended = [43,42,41,40,39,38,37,36,35,34,33]
        elif base == 44 and switchBlock == 67:
            appended = [67,68,69,70,71,38,37,36,35,34,33]
        elif base == 33 and switchBlock == 32:
            appended = [32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16]
        elif base == 33 and switchBlock == 72:
            appended = [72,73,74,75,76,27,26,25,24,23,22,21,20,19,18,17,16]
        elif base == 16 and switchBlock == 15:
            appended = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,16,17,18,19,20,21,22,23,24,25,26,27]
        elif base == 16 and switchBlock == 1:
            appended = [1,2,3,4,5,6,7,8,9]
        elif base == 9 and switchBlock == 0:
            appended = [0]
        elif base == 9 and switchBlock == 10:
            appended = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        
        self.lineRoute.append(appended)
