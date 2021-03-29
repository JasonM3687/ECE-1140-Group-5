class Block():
    def __init__(self,trainID):
        self.ID = trainID

    lastSection = 'Z'
    currSection = 0
    currBlock = 0
    nextBlock = 0
    switchState = 0

    def setLine(self,line):
        self.line = line

    def determineNextBlock(self):
        if self.line == "green":
            self.currBlock = self.nextBlock
            self.updateCurrentSection()

            if self.currBlock == 0:
                self.nextBlock == 63
            elif (self.lastSection == 'Z') or (self.lastSection == 'K') or (self.lastSection == 'L') or (self.lastSection == 'M'):
                self.nextBlock += 1
            elif (self.lastSection == 'N' and self.currSection == 'O'):
                self.nextBlock += 1
            elif (self.lastSection == 'O') or (self.lastSection == 'P'):
                self.nextBlock += 1
            elif (self.lastSection == 'Q') and (self.currBlock == 100):
                self.nextBlock = 85
            elif (self.lastSection == 'Q') and (self.currBlock == 77):
                self.nextBlock == 101
            elif (self.lastSection == 'Q'):
                self.nextBlock -= 1
            elif (self.lastSection == 'Y') and (self.currBlock == 150):
                self.nextBlock = 28
            elif (self.lastSection == 'R') or (self.lastSection == 'S') or (self.lastSection == 'T') or (self.lastSection == 'U') or (self.lastSection == 'V') or (self.lastSection == 'W') or (self.lastSection == 'X') or (self.lastSection == 'Y'):
                self.nextBlock += 1
            elif (self.lastSection == 'Z'):
                self.nextBlock -= 1
            elif (self.lastSection == 'F' and self.currSection == 'E'):
                self.nextBlock -= 1
            elif (self.lastSection == 'E' and self.currSection == 'D'):
                self.nextBlock -= 1
            elif (self.lastSection == 'D' and self.currSection == 'C'):
                self.nextBlock -= 1
            elif (self.lastSection == 'B') and (self.currBlock == 1):
                self.nextBlock = 13
            elif (self.lastSection == 'C') or (self.lastSection == 'B'):
                self.nextBlock -= 1
            elif (self.lastSection == 'A'):
                self.nextBlock += 1
            elif (self.lastSection == 'D') and (self.currSection == 'E'):
                self.nextBlock += 1
            elif (self.lastSection == 'E') and (self.currSection == 'F'):
                self.nextBlock += 1
            elif (self.lastSection == 'F') and (self.currSection == 'G'):
                self.nextBlock += 1
            elif (self.currSection == 'J') and self.switchState == 0:
                self.nextBlock == 0
            elif (self.lastSection == 'G') or (self.lastSection == 'H') or (self.lastSection == 'I') or (self.lastSection == 'J'):
                self.nextBlock += 1

            self.updateCurrentSection() 
            
    def updateCurrentSection(self): 
        

        if (self.currBlock == 63):
            self.lastSection = self.currSection
            self.currSection = 'K'
        elif (self.currBlock == 69):
            self.lastSection = self.currSection
            self.currSection = 'L'
        elif (self.currBlock == 74):
            self.lastSection = self.currSection
            self.currSection = 'M'
        elif (self.currBlock == 77) and (self.currSection == 'M'):
            self.lastSection = self.currSection
            self.currSection = 'N'
        elif (self.currBlock == 86):
            self.lastSection = self.currSection
            self.currSection = 'O'
        elif (self.currBlock == 89):
            self.lastSection = self.currSection
            self.currSection = 'P'
        elif (self.currBlock == 98):
            self.lastSection = self.currSection
            self.currSection = 'Q'
        elif (self.currBlock == 85) and (self.currSection == 'Q'):
            self.lastSection = self.currSection
            self.currSection = 'P'
        elif (self.currBlock == 101):
            self.lastSection = self.currSection
            self.currSection = 'R'
        elif (self.currBlock == 102):
            self.lastSection = self.currSection
            self.currSection = 'S'
        elif (self.currBlock == 105):
            self.lastSection = self.currSection
            self.currSection = 'T'
        elif (self.currBlock == 110):
            self.lastSection = self.currSection
            self.currSection = 'U'
        elif (self.currBlock == 117):
            self.lastSection = self.currSection
            self.currSection = 'V'
        elif (self.currBlock == 122):
            self.lastSection = self.currSection
            self.currSection = 'W'
        elif (self.currBlock == 144):
            self.lastSection = self.currSection
            self.currSection = 'X'
        elif (self.currBlock == 147):
            self.lastSection = self.currSection
            self.currSection = 'Y'
        elif (self.currBlock == 150):
            self.lastSection = self.currSection
            self.currSection = 'Z'
        #elif (self.currBlock == 28) and (self.curr)