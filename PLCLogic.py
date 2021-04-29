
from array import array
import re



#####  #####  #####  ####     #####  ##      ####    #####  #   #  #####  ## ##  #####   ###
##  #  ##     #   #  ##  #    ##  #  ##     ##         #    ##  #  ##  #  ## ##    #    #
#####  ####   #####  ##  #    #####  ##     ##         #    # # #  #####  ## ##    #     ###
## #   ##     #   #  ##  #    ##     ##     ##         #    #  ##  ##     ## ##    #        #
##  #  #####  #   #  ####     ##     #####   ####    #####  #   #  ##      ###     #     ###


with open('PLC_IO.txt','r') as file:
    Content=file.readlines()
file.close()


RedBlockOcc = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[1])]
RedFaults = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[2])]
RedRoute = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[3])]
RedUnderground = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[4])]

GreenBlockOcc = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[7])]
GreenFaults = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[8])]
GreenRoute = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[9])]
GreenUnderground = [bool(int(s)) for s in re.findall(r'\b\d+\b', Content[10])]

ManualSW = int(Content[45].strip()[-1])


GreenSWOut=[0]*6
GreenTrainLightSigs=[0]*150
GreenAuthChange=[0]*150
GreenLightStatuses=[0]*150
GreenCrossStatus=0

RedSWOut=[0]*7
RedTrainLightSigs=[0]*76
RedAuthChange=[0]*76
RedLightStatuses=[0]*76
RedCrossStatus=0

#print("Manual =" + str(ManualSW))



#####  ##      ####    ####    ###    ###   ##     #####  #####  #   #    ##      ###    ####   #####   ####
##  #  ##     ##       ##  #  #   #  #   #  ##     ##     #   #  ##  #    ##     #   #  #         #    ##
#####  ##     ##       ####   #   #  #   #  ##     ####   #####  # # #    ##     #   #  # ###     #    ##
##     ##     ##       ##  #  #   #  #   #  ##     ##     #   #  #  ##    ##     #   #  #   #     #    ##
##     #####   ####    ####    ###    ###   #####  #####  #   #  #   #    #####   ###    ###    #####   ####

#Green Logic
#switch Logic
if(ManualSW == 0):
    GreenSWOut[0]=GreenRoute[12] and GreenRoute[0] and not(GreenBlockOcc[0]) and not(GreenBlockOcc[12]) and not(GreenBlockOcc[11])
    GreenSWOut[1]=GreenRoute[28] and GreenRoute[29] and not(GreenBlockOcc[28]) and not(GreenBlockOcc[29]) and not(GreenBlockOcc[149])
    GreenSWOut[2]=GreenRoute[56] and GreenRoute[57] and not(GreenBlockOcc[56]) and not(GreenBlockOcc[57])
    GreenSWOut[3]=GreenRoute[62] and GreenRoute[61] and not(GreenBlockOcc[61]) and not(GreenBlockOcc[62])
    GreenSWOut[4]=GreenRoute[76] and GreenRoute[75] and not(GreenBlockOcc[75]) and not(GreenBlockOcc[76]) and not(GreenBlockOcc[100])
    GreenSWOut[5]=GreenRoute[84] and GreenRoute[85] and not(GreenBlockOcc[84]) and not(GreenBlockOcc[85]) and not(GreenBlockOcc[99])
#crossing logic
GreenCrossStatus = GreenBlockOcc[17] or GreenBlockOcc[19] or GreenBlockOcc[18]

#Train light signals for tunnels logic
for i in range(len(GreenTrainLightSigs)):
    GreenTrainLightSigs[i]=GreenUnderground[i] and GreenBlockOcc[i]

#Authority and traffic light logic
for i in range(len(GreenBlockOcc)):
    if(i==0):
        GreenLightStatuses[0] = GreenBlockOcc[12] or GreenBlockOcc[11] or GreenFaults[12] or GreenFaults[11]
        GreenAuthChange[0] = GreenBlockOcc[12] or GreenBlockOcc[11] or GreenFaults[12] or GreenFaults[11]
    elif(i==12):
        GreenLightStatuses[12] = GreenBlockOcc[0] or GreenBlockOcc[11] or GreenFaults[0] or GreenFaults[11]
        GreenAuthChange[12] =  GreenBlockOcc[0] or GreenBlockOcc[11] or GreenFaults[0] or GreenFaults[11]
    elif(i==149):
        GreenLightStatuses[149] = GreenBlockOcc[28] or GreenFaults [28]
        GreenAuthChange[149] = GreenBlockOcc[28] or GreenFaults[28]
    elif(i==99):
        GreenLightStatuses[99] = GreenBlockOcc[84] or GreenBlockOcc[83] or GreenBlockOcc[82] or GreenBlockOcc[81] or GreenBlockOcc[80] or GreenBlockOcc[79] or GreenBlockOcc[78] or GreenBlockOcc[77] or GreenBlockOcc[76] or GreenFaults[84]
        GreenAuthChange[99]= GreenBlockOcc[84] or GreenBlockOcc[83] or GreenBlockOcc[82] or GreenBlockOcc[81] or GreenBlockOcc[80] or GreenBlockOcc[79] or GreenBlockOcc[78] or GreenBlockOcc[77] or GreenBlockOcc[76] or GreenFaults[84]
    else:
        GreenLightStatuses[i] = GreenBlockOcc[i+1]  or GreenFaults[i+1] #or GreenBlockOcc[i-1]  or GreenFaults[i-1]
        GreenAuthChange[i] = GreenBlockOcc[i+1] or GreenFaults[i+1] #or GreenBlockOcc[i-1]  or GreenFaults[i-1]
        #or GreenBlockOcc[i-1]  or GreenFaults[i-1]





#Red Logic
#switch Logic
if(ManualSW == 0):
    RedSWOut[0]=RedRoute[8] and RedRoute[9] and not(RedBlockOcc[8]) and not(RedBlockOcc[9])
    RedSWOut[1]=RedRoute[0] and RedRoute[15] and not(RedBlockOcc[0]) and not(RedBlockOcc[15]) and not(RedBlockOcc[14])
    RedSWOut[2]=RedRoute[27] and RedRoute[26] and not(RedBlockOcc[27]) and not(RedBlockOcc[26]) and not(RedBlockOcc[75])
    RedSWOut[3]=RedRoute[31] and RedRoute[32] and not(RedBlockOcc[31]) and not(RedBlockOcc[32]) and not(RedBlockOcc[71])
    RedSWOut[4]=RedRoute[37] and RedRoute[38] and not(RedBlockOcc[37]) and not(RedBlockOcc[38]) and not(RedBlockOcc[70])
    RedSWOut[5]=RedRoute[42] and RedRoute[43] and not(RedBlockOcc[42]) and not(RedBlockOcc[43]) and not(RedBlockOcc[66])
    RedSWOut[6]=RedRoute[52] and RedRoute[51] and not(RedBlockOcc[52]) and not(RedBlockOcc[51]) and not(RedBlockOcc[65])

#crossing logic
RedCrossStatus = RedBlockOcc[47] or RedBlockOcc[45] or RedBlockOcc[46]

#Train light signals for tunnels logic
for i in range(len(RedTrainLightSigs)):
    RedTrainLightSigs[i]=RedUnderground[i] and RedBlockOcc[i]

#Authority and traffic light logic
for i in range(len(RedBlockOcc)):
    if(i==0):
        RedLightStatuses[0] = RedBlockOcc[14] or RedBlockOcc[15] or RedFaults[14] or RedFaults[15]
        RedAuthChange[0] = RedBlockOcc[14] or RedBlockOcc[15] or RedFaults[14] or RedFaults[15]
    elif(i==75):
        RedLightStatuses[75] = RedBlockOcc[26] or RedBlockOcc[27] or RedBlockOcc[74] or RedFaults[26] or RedFaults[27] or RedFaults[74]
        RedAuthChange[75] = RedBlockOcc[26] or RedBlockOcc[27] or RedBlockOcc[74] or RedFaults[26] or RedFaults[27] or RedFaults[74]
    elif(i==71):
        RedLightStatuses[71] = RedBlockOcc[31] or RedBlockOcc[32] or RedBlockOcc[72] or RedFaults[31] or RedFaults[32] or RedFaults[72]
        RedAuthChange[71] = RedBlockOcc[31] or RedBlockOcc[32] or RedBlockOcc[72] or RedFaults[31] or RedFaults[32] or RedFaults[72]
    elif(i==70):
        RedLightStatuses[70] = RedBlockOcc[37] or RedBlockOcc[38] or RedBlockOcc[69] or RedFaults[37] or RedFaults[38] or RedFaults[69]
        RedAuthChange[70] = RedBlockOcc[37] or RedBlockOcc[38] or RedBlockOcc[69] or RedFaults[37] or RedFaults[38] or RedFaults[69]
    elif(i==66):
        RedLightStatuses[66] = RedBlockOcc[42] or RedBlockOcc[43] or RedBlockOcc[67] or RedFaults[42] or RedFaults[43] or RedFaults[67]
        RedAuthChange[66] = RedBlockOcc[42] or RedBlockOcc[43] or RedBlockOcc[67] or RedFaults[42] or RedFaults[43] or RedFaults[67]
    elif(i==65):
        RedLightStatuses[65] = RedBlockOcc[52] or RedBlockOcc[51] or RedBlockOcc[64] or RedFaults[52] or RedFaults[51] or RedFaults[64]
        RedLightStatuses[65] = RedBlockOcc[52] or RedBlockOcc[51] or RedBlockOcc[64] or RedFaults[52] or RedFaults[51] or RedFaults[64]
    else:
        RedLightStatuses[i] = RedBlockOcc[i+1] or RedFaults[i+1] #or RedBlockOcc[i-1] or RedFaults[i-1]
        RedAuthChange[i] = RedBlockOcc[i+1] or RedFaults[i+1] #or RedBlockOcc[i-1] or RedFaults[i-1]






##         ##  #####  #####  #####  #####     ###   ## ##  #####  #####  ## ##  #####   ###
##   ###   ##  ##  #    #      #    ##       #   #  ## ##    #    ##  #  ## ##    #    #
##  ## ##  ##  #####    #      #    ####     #   #  ## ##    #    #####  ## ##    #     ###
##  ## ##  ##  ## #     #      #    ##       #   #  ## ##    #    ##     ## ##    #        #
 ####  ####    ##  #  #####    #    #####     ###    ###     #    ##      ###     #     ###





#Start process of writing to output file
with open('PLC_IO.txt','r') as file:
    Content=file.readlines()
file.close()


#figure out what wayside is currently running the PLC
with open('CurrentWayside.txt','r') as file:
    CurrentWayside=file.readlines()
file.close()
CurrentWayside=CurrentWayside[0][19:].strip()

#Write the output to the green 1 output section
if CurrentWayside == "Green1":
    if ManualSW == 0:
        tempstringSW=""
        for i in range(len(GreenSWOut)):
            tempstringSW=tempstringSW+str(int(GreenSWOut[i]))+","
        tempstringSW=tempstringSW[:-1]
        Content[22]="SwitchPos="+tempstringSW+"\n"

    tempstringTrainL=""
    for i in range(len(GreenTrainLightSigs)):
        tempstringTrainL=tempstringTrainL+str(int(GreenTrainLightSigs[i]))+","
    tempstringTrainL=tempstringTrainL[:-1]
    Content[24]="TrainLightSignals="+tempstringTrainL+"\n"

    tempstringAuth=""
    for i in range(len(GreenAuthChange)):
        tempstringAuth=tempstringAuth+str(int(GreenAuthChange[i]))+","
    tempstringAuth=tempstringAuth[:-1]
    Content[25]="AuthChange="+tempstringAuth+"\n"

    tempstringTrafL=""
    for i in range(len(GreenLightStatuses)):
        tempstringTrafL=tempstringTrafL+str(int(GreenLightStatuses[i]))+","
    tempstringTrafL=tempstringTrafL[:-1]
    Content[23]="LightStatuses="+tempstringTrafL+"\n"

    tempstringCross=str(int(GreenCrossStatus))
    Content[27]="CrossStatus="+tempstringCross+"\n"

elif CurrentWayside == "Green2":
    if ManualSW == 0:
        tempstringSW=""
        for i in range(len(GreenSWOut)):
            tempstringSW=tempstringSW+str(int(GreenSWOut[i]))+","
        tempstringSW=tempstringSW[:-1]
        Content[38]="SwitchPos="+tempstringSW+"\n"

    tempstringTrainL=""
    for i in range(len(GreenTrainLightSigs)):
        tempstringTrainL=tempstringTrainL+str(int(GreenTrainLightSigs[i]))+","
    tempstringTrainL=tempstringTrainL[:-1]
    Content[40]="TrainLightSignals="+tempstringTrainL+"\n"

    tempstringAuth=""
    for i in range(len(GreenAuthChange)):
        tempstringAuth=tempstringAuth+str(int(GreenAuthChange[i]))+","
    tempstringAuth=tempstringAuth[:-1]
    Content[41]="AuthChange="+tempstringAuth+"\n"

    tempstringTrafL=""
    for i in range(len(GreenLightStatuses)):
        tempstringTrafL=tempstringTrafL+str(int(GreenLightStatuses[i]))+","
    tempstringTrafL=tempstringTrafL[:-1]
    Content[39]="LightStatuses="+tempstringTrafL+"\n"

    tempstringCross=str(int(GreenCrossStatus))
    Content[43]="CrossStatus="+tempstringCross+"\n"

elif CurrentWayside == "Red1":
    if ManualSW == 0:
        tempstringSW=""
        for i in range(len(RedSWOut)):
            tempstringSW=tempstringSW+str(int(RedSWOut[i]))+","
        tempstringSW=tempstringSW[:-1]
        Content[14]="SwitchPos="+tempstringSW+"\n"

    tempstringTrainL=""
    for i in range(len(RedTrainLightSigs)):
        tempstringTrainL=tempstringTrainL+str(int(RedTrainLightSigs[i]))+","
    tempstringTrainL=tempstringTrainL[:-1]
    Content[16]="TrainLightSignals="+tempstringTrainL+"\n"

    tempstringAuth=""
    for i in range(len(RedAuthChange)):
        tempstringAuth=tempstringAuth+str(int(RedAuthChange[i]))+","
    tempstringAuth=tempstringAuth[:-1]
    Content[17]="AuthChange="+tempstringAuth+"\n"

    tempstringTrafL=""
    for i in range(len(RedLightStatuses)):
        tempstringTrafL=tempstringTrafL+str(int(RedLightStatuses[i]))+","
    tempstringTrafL=tempstringTrafL[:-1]
    Content[15]="LightStatuses="+tempstringTrafL+"\n"

    tempstringCross=str(int(RedCrossStatus))
    Content[19]="CrossStatus="+tempstringCross+"\n"

elif CurrentWayside == "Red2":
    if ManualSW == 0:
        tempstringSW=""
        for i in range(len(RedSWOut)):
            tempstringSW=tempstringSW+str(int(RedSWOut[i]))+","
        tempstringSW=tempstringSW[:-1]
        Content[30]="SwitchPos="+tempstringSW+"\n"

    tempstringTrainL=""
    for i in range(len(RedTrainLightSigs)):
        tempstringTrainL=tempstringTrainL+str(int(RedTrainLightSigs[i]))+","
    tempstringTrainL=tempstringTrainL[:-1]
    Content[32]="TrainLightSignals="+tempstringTrainL+"\n"

    tempstringAuth=""
    for i in range(len(RedAuthChange)):
        tempstringAuth=tempstringAuth+str(int(RedAuthChange[i]))+","
    tempstringAuth=tempstringAuth[:-1]
    Content[33]="AuthChange="+tempstringAuth+"\n"

    tempstringTrafL=""
    for i in range(len(RedLightStatuses)):
        tempstringTrafL=tempstringTrafL+str(int(RedLightStatuses[i]))+","
    tempstringTrafL=tempstringTrafL[:-1]
    Content[31]="LightStatuses="+tempstringTrafL+"\n"

    tempstringCross=str(int(RedCrossStatus))
    Content[35]="CrossStatus="+tempstringCross+"\n"

with open('PLC_IO.txt','w') as file:
    file.writelines(Content)
file.close
