import pylightxl as xl

class Block:
	heat=False
	occ=0
	fail=0
	direc=False
	station=""
	envTemp=65
	under=0
	cross=0
	light=0
	def __init__(self, line, section, bNum, bLength, bGrade, sLimit, elev, cElev):
		self.line=line
		self.section=section
		self.bNum=bNum
		self.bLength=bLength
		self.bGrade=bGrade
		self.sLimit=sLimit
		self.elev=elev
		self.cElev=cElev
	def getSpeed(self):
		return self.sLimit
	def setTemp(self, temp):
		self.envTemp=temp
		if(self.envTemp<=32):
			self.heat=1
		else:
			self.heat=0
	def checkFail(self):
		if(self.fail!=0 or self.occ==1):
			self.occ=1
		else:
			self.occ=0

class Beacon:
	def __init__(self,line,block,data):
		self.line=line
		self.block=block
		self.data=data
	def readBeacon(self):
		return self.data

class Switch:
	def __init__(self,line,base,branch1,branch2,state=False):
		self.line=line
		self.base=base
		self.branch1=branch1
		self.branch2=branch2
		self.state=state

class Signal(Block):
    state=0
    cSpeed=0
    auth=0
    def readSignal(self):
        return self.cSpeed,self.auth
    def setAuth(self, auth):
        self.auth=auth
    def setcSpeed(self, c):
        self.cSpeed=c
    def setState(self, s):
        self.state=s
    def getState(self):
        return self.state

class Station:
	board=0
	disemb=0
	sales=0
	def __init__(self,line,block,name):
		self.posLine=line
		self.posBlock=block
		self.name=name
	def addBoard(self,num):
		self.board+=num
	def addDisemb(self,num):
		self.disemb+=num
	def addSales(self,num):
		self.sales+=num
		self.addBoard(num)
		self.addDisemb(num)

def trackPull(text):
	loc=("Track Layout & Vehicle Data vF2.xlsx")
	wb=xl.readxl(loc)
	sheet="Red Line"

	signals=[]
	beacons=[]
	stations=[]
	i=2
	tracks=[]
	while i<78:
		tracks.append(Block(wb.ws(sheet).index(i,1),wb.ws(sheet).index(i,2),wb.ws(sheet).index(i,3),wb.ws(sheet).index(i,4),wb.ws(sheet).index(i,5),wb.ws(sheet).index(i,6),wb.ws(sheet).index(i,9),wb.ws(sheet).index(i,10)))
		signals.append(Signal(tracks[-1].line,tracks[-1].section,tracks[-1].bNum,tracks[-1].bLength,tracks[-1].bGrade,tracks[-1].sLimit,tracks[-1].elev,tracks[-1].cElev))
		if(tracks[-1].direc=="Uni"):
			tracks[-1].direc=False
		else:
			tracks[-1].direc=True
		if(wb.ws(sheet).index(i,8)=="Left/Right"):
			tracks[-1].station="Both"
		elif(wb.ws(sheet).index(i,8)=="Right"):
			tracks[-1].station="Right"
		elif(wb.ws(sheet).index(i,8)=="Left"):
			tracks[-1].station="Left"
		else:
			tracks[-1].station="None"
		if(i!=2):
			if(wb.ws(sheet).index(i,12)!=""):
				stations.append(Station(wb.ws(sheet).index(i,1),wb.ws(sheet).index(i,3),wb.ws(sheet).index(i,12)))
				beacons.append(Beacon(wb.ws(sheet).index(i,1),wb.ws(sheet).index(i,3),wb.ws(sheet).index(i,12)))
		if(wb.ws(sheet).index(i,7).find("UNDERGROUND")!=-1):
			tracks[-1].under=1
		i=i+1
	
	sheet="Green Line"
	j=2
	while j<152:
		tracks.append(Block(wb.ws(sheet).index(j,1),wb.ws(sheet).index(j,2),wb.ws(sheet).index(j,3),wb.ws(sheet).index(j,4),wb.ws(sheet).index(j,5),wb.ws(sheet).index(j,6),wb.ws(sheet).index(j,9),wb.ws(sheet).index(j,10)))
		signals.append(Signal(wb.ws(sheet).index(j,1),wb.ws(sheet).index(j,2),wb.ws(sheet).index(j,3),wb.ws(sheet).index(j,4),wb.ws(sheet).index(j,5),wb.ws(sheet).index(j,6),wb.ws(sheet).index(j,9),wb.ws(sheet).index(j,10)))
		if(tracks[-1].direc=="Uni"):
			tracks[-1].direc=False
		else:
			tracks[-1].direc=True
		if(wb.ws(sheet).index(j,8)=="Left/Right"):
			tracks[-1].station="Both"
		elif(wb.ws(sheet).index(j,8)=="Right"):
			tracks[-1].station="Right"
		elif(wb.ws(sheet).index(j,8)=="Left"):
			tracks[-1].station="Left"
		else:
			tracks[-1].station="None"
		if(j!=2):
			if(wb.ws(sheet).index(j,13)!=""):
				stations.append(Station(wb.ws(sheet).index(j,1),wb.ws(sheet).index(j,3),wb.ws(sheet).index(j,13)))
				beacons.append(Beacon(wb.ws(sheet).index(j,1),wb.ws(sheet).index(j,3),wb.ws(sheet).index(j,13)))
		if(wb.ws(sheet).index(j,7).find("UNDERGROUND")!=-1):
			tracks[-1].under=1
		j=j+1

		beacons.append(Beacon("Red",6,"HERRON AVE"))
		beacons.append(Beacon("Red",8,"HERRON AVE"))
		beacons.append(Beacon("Red",9,"SHADYSIDE"))
		beacons.append(Beacon("Red",15,"SHADYSIDE"))
		beacons.append(Beacon("Red",17,"SWISSVILLE"))
		beacons.append(Beacon("Red",20,"HERRON AVE"))
		beacons.append(Beacon("Red",22,"PENN STATION"))
		beacons.append(Beacon("Red",24,"SWISSVILLE"))
		beacons.append(Beacon("Red",26,"STEEL PLAZE"))
		beacons.append(Beacon("Red",34,"PENN STATION"))
		beacons.append(Beacon("Red",36,"FIRST AVE"))
		beacons.append(Beacon("Red",44,"STEEL PLAZE"))
		beacons.append(Beacon("Red",46,"STATION SQUARE"))
		beacons.append(Beacon("Red",47,"FIRST AVE"))
		beacons.append(Beacon("Red",49,"SOUTH HILLS JUNCTION"))
		beacons.append(Beacon("Red",59,"STATION SQUARE"))
		beacons.append(Beacon("Red",61,"STATION SQUARE"))
  
		beacons.append(Beacon("Green",1,"STATION"))
		beacons.append(Beacon("Green",8,"PIONEER"))
		beacons.append(Beacon("Green",15,"EDGEBROOK"))
		beacons.append(Beacon("Green",17,"WHITED"))
		beacons.append(Beacon("Green",21,"STATION"))
		beacons.append(Beacon("Green",23,"SOUTH BANK"))
		beacons.append(Beacon("Green",32,"CENTRAL"))
		beacons.append(Beacon("Green",40,"INGLEWOOD"))
		beacons.append(Beacon("Green",49,"OVERBROOK"))
		beacons.append(Beacon("Green",58,"GLENBURY"))
		beacons.append(Beacon("Green",63,"GLENBURY"))
		beacons.append(Beacon("Green",66,"DORMONT"))
		beacons.append(Beacon("Green",74,"MT LEBANON"))
		beacons.append(Beacon("Green",78,"POPLAR"))
		beacons.append(Beacon("Green",89,"CASTLE SHANNON"))
		beacons.append(Beacon("Green",97,"MT LEBANON"))
		beacons.append(Beacon("Green",101,"DORMONT"))
		beacons.append(Beacon("Green",106,"GLENBURY"))
		beacons.append(Beacon("Green",115,"OVERBROOK"))
		beacons.append(Beacon("Green",124,"INGLEWOOD"))
		beacons.append(Beacon("Green",133,"CENTRAL"))
		beacons.append(Beacon("Green",142,"WHITED"))

	return tracks, beacons, signals, stations


def switchMake():
	switches=[]

	switches.append(Switch("Red",9,0,10))
	switches.append(Switch("Red",16,1,15))
	switches.append(Switch("Red",27,28,76))
	switches.append(Switch("Red",33,32,72))
	switches.append(Switch("Red",38,39,71))
	switches.append(Switch("Red",44,43,67))
	switches.append(Switch("Red",52,53,66))
	switches.append(Switch("Green",13,1,12))
	switches.append(Switch("Green",29,30,150))
	switches.append(Switch("Green",57,0,58))
	switches.append(Switch("Green",63,0,62))
	switches.append(Switch("Green",77,76,101))
	switches.append(Switch("Green",85,86,100))
	return switches