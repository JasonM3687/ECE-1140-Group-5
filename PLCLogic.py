
from array import array
import re
with open('PLC_IO.txt','r') as file:
    Content=file.readlines()

GreenBlockOcc = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[12])]
GreenFaults = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[13])]
GreenSwitches = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[14])]
GreenTrafficLights = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[15])]
GreenRoute = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[17])]
GreenUnderground = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[18])]


GreenSWOut=[0]*6
TrainLightSigs=[0]*150
AuthChange=[0]*150
LightStatuses=[0]*150

GreenSWOut[0]=GreenRoute[12] and GreenRoute[0] and not(GreenBlockOcc[0]) and not(GreenBlockOcc[12]) and not(GreenBlockOcc[11])
GreenSWOut[1]=GreenRoute[28] and GreenRoute[29] and not(GreenBlockOcc[28]) and not(GreenBlockOcc[29]) and not(GreenBlockOcc[149])
GreenSWOut[2]=GreenRoute[56] and GreenRoute[57] and not(GreenBlockOcc[56]) and not(GreenBlockOcc[57])
GreenSWOut[3]=GreenRoute[62] and GreenRoute[61] and not(GreenBlockOcc[61]) and not(GreenBlockOcc[62])
GreenSWOut[4]=GreenRoute[76] and GreenRoute[75] and not(GreenBlockOcc[75]) and not(GreenBlockOcc[76]) and not(GreenBlockOcc[100])
GreenSWOut[5]=GreenRoute[84] and GreenRoute[85] and not(GreenBlockOcc[84]) and not(GreenBlockOcc[85]) and not(GreenBlockOcc[99])

for i in range(len(TrainLightSigs)):
    TrainLightSigs[i]=GreenUnderground[i] and GreenBlockOcc[i]

for i in range(len(GreenBlockOcc)):
    if(i==0):
        LightStatuses[0] = GreenBlockOcc[12] = GreenFaults[28]
        AuthChange[0] = GreenBlockOcc[12] or GreenFaults[28]
    elif(i==149):
        LightStatuses[149] = GreenBlockOcc[28] or GreenFaults [28]
        AuthChange[0] = GreenBlockOcc[28] or GreenFaults[28]
    elif(i==99):
        LightStatuses[99] = GreenBlockOcc[84] or GreenBlockOcc[83] or GreenBlockOcc[82] or GreenBlockOcc[81] or GreenBlockOcc[80] or GreenBlockOcc[79] or GreenBlockOcc[78] or GreenBlockOcc[77] or GreenBlockOcc[76] or GreenFaults[84]
        AuthChange[99]= GreenBlockOcc[84] or GreenBlockOcc[83] or GreenBlockOcc[82] or GreenBlockOcc[81] or GreenBlockOcc[80] or GreenBlockOcc[79] or GreenBlockOcc[78] or GreenBlockOcc[77] or GreenBlockOcc[76] or GreenFaults[84]
    else:
        LightStatuses[i] = GreenBlockOcc[i+1] or GreenFaults[i+1]
        AuthChange[i] = GreenBlockOcc[i+1] or GreenFaults[i+1]

with open('PLC_IO.txt','r') as file:
    Content=file.readlines()

tempstringSW=""
for i in range(len(GreenSWOut)):
    tempstringSW=tempstringSW+str(int(GreenSWOut[i]))+","
tempstringSW=tempstringSW[:-1]

Content[14]="SwitchPos="+tempstringSW+"\n"

tempstringTrainL=""
for i in range(len(TrainLightSigs)):
    tempstringTrainL=tempstringTrainL+str(int(TrainLightSigs[i]))+","
tempstringTrainL=tempstringTrainL[:-1]

Content[19]="TrainLightSignals="+tempstringTrainL+"\n"

tempstringAuth=""
for i in range(len(AuthChange)):
    tempstringAuth=tempstringAuth+str(int(AuthChange[i]))+","
tempstringAuth=tempstringAuth[:-1]

Content[20]="AuthChange="+tempstringAuth+"\n"

tempstringTrafL=""
for i in range(len(LightStatuses)):
    tempstringTrafL=tempstringTrafL+str(int(LightStatuses[i]))+","
tempstringTrafL=tempstringTrafL[:-1]

Content[15]="LightStatuses="+tempstringTrafL+"\n"

with open('PLC_IO.txt','w') as file:
    file.writelines(Content)