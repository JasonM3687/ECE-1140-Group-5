import pylightxl as xl

class Block:
	heat=False
	occ=False
	fail=0
	direc=False
	station=""
	envTemp=65
	under=0
	cross=0
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
		signals.append(Signal(wb.ws(sheet).index(i,1),wb.ws(sheet).index(i,2),wb.ws(sheet).index(i,3),wb.ws(sheet).index(i,4),wb.ws(sheet).index(i,5),wb.ws(sheet).index(i,6),wb.ws(sheet).index(i,9),wb.ws(sheet).index(i,10)))
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
		if(wb.ws(sheet).index(i,7).find("UNDERGROUND")!=-1):
			tracks[-1].under=1
		i=i+1
	
	sheet="Green Line"
	j=2
	while j<152:
		tracks.append(Block(wb.ws(sheet).index(j,1),wb.ws(sheet).index(j,2),wb.ws(sheet).index(j,3),wb.ws(sheet).index(j,4),wb.ws(sheet).index(j,5),wb.ws(sheet).index(j,6),wb.ws(sheet).index(j,9),wb.ws(sheet).index(j,10)))
		signals.append(Signal(wb.ws(sheet).index(i,1),wb.ws(sheet).index(i,2),wb.ws(sheet).index(i,3),wb.ws(sheet).index(i,4),wb.ws(sheet).index(i,5),wb.ws(sheet).index(i,6),wb.ws(sheet).index(i,9),wb.ws(sheet).index(i,10)))
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
			if(wb.ws(sheet).index(j,12)!=""):
				stations.append(Station(wb.ws(sheet).index(j,1),wb.ws(sheet).index(j,3),wb.ws(sheet).index(j,12)))
		if(wb.ws(sheet).index(j,7).find("UNDERGROUND")!=-1):
			tracks[-1].under=1
		j=j+1

		beacons.append(Beacon("Red",6,"Herron Ave"))
		beacons.append(Beacon("Red",8,"Herron Ave"))
		beacons.append(Beacon("Red",15,"Shadyside"))
		beacons.append(Beacon("Red",17,"Swissville"))
		beacons.append(Beacon("Red",20,"Herron Ave"))
		beacons.append(Beacon("Red",22,"Penn Station"))
		beacons.append(Beacon("Red",24,"Swissville"))
		beacons.append(Beacon("Red",26,"Steel Plaza"))
		beacons.append(Beacon("Red",34,"Penn Station"))
		beacons.append(Beacon("Red",36,"First Ave"))
		beacons.append(Beacon("Red",44,"Steel Plaza"))
		beacons.append(Beacon("Red",46,"Station Square"))
		beacons.append(Beacon("Red",47,"First Ave"))
		beacons.append(Beacon("Red",49,"South Hills Junction"))
		beacons.append(Beacon("Red",59,"Station Square"))
		beacons.append(Beacon("Red",61,"Station Square"))
  
		beacons.append(Beacon("Green",1,"Station"))
		beacons.append(Beacon("Green",8,"Pioneer"))
		beacons.append(Beacon("Green",15,"Edgebrook"))
		beacons.append(Beacon("Green",17,"Whited"))
		beacons.append(Beacon("Green",21,"Station"))
		beacons.append(Beacon("Green",23,"South Bank"))
		beacons.append(Beacon("Green",32,"Central"))
		beacons.append(Beacon("Green",40,"Inglewood"))
		beacons.append(Beacon("Green",49,"Overbrook"))
		beacons.append(Beacon("Green",58,"Glenbury"))
		beacons.append(Beacon("Green",66,"Dormont"))
		beacons.append(Beacon("Green",74,"Mt Lebanon"))
		beacons.append(Beacon("Green",78,"Poplar"))
		beacons.append(Beacon("Green",89,"Castle Shannon"))
		beacons.append(Beacon("Green",97,"Mt Lebanon"))
		beacons.append(Beacon("Green",101,"Dormont"))
		beacons.append(Beacon("Green",106,"Glenbury"))
		beacons.append(Beacon("Green",115,"Overbrook"))
		beacons.append(Beacon("Green",124,"Inglewood"))
		beacons.append(Beacon("Green",133,"Central"))
		beacons.append(Beacon("Green",142,"Whited"))

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