from array import array
def findController(controllerName):
        line_number=0
        with open("PLC_IO.txt",'r') as read_obj:
            for line in read_obj:
                line_number+=1
                if controllerName in line:
                    return line_number

with open('CurrentWayside.txt','r') as file:
    Content=file.readlines()

if Content[0]=="CurrentWaysideLine=Red":
   pass
else:
    if Content[1]=="CurrentWaysideNumber=9":
        controllerLine=findController("GreenController 9")
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        blockOccs=[int(i) for i in Content[controllerLine+1].split() if i.isdigit()]
        faultStatuses=[int(i) for i in Content[controllerLine+2].split() if i.isdigit()]
        lightStatuses=[int(i) for i in Content[controllerLine+4].split() if i.isdigit()]
        routedBlocks=[int(i) for i in Content[controllerLine+6].split() if i.isdigit()]
        underground=[int(i) for i in Content[controllerLine+7].split() if i.isdigit()]
        AuthChange=[]
        light=[]
        trainLight=[]

        for i in range(len(blockOccs)-1):
            AuthChange.append(blockOccs[i+1] or faultStatuses[i+1])
            light.append(blockOccs[i+1] or faultStatuses[i+1])
        
        for i in range(len(underground)):
            trainLight.append(underground[i])
        
        Content[controllerLine+5]="AuthZero="
        for i in range(len(AuthChange)):
            Content[controllerLine+5]=Content[controllerLine+5]+str(int(AuthChange[i]))+','
        Content[controllerLine+5]=Content[controllerLine+5][:-1]
        Content[controllerLine+5]=Content[controllerLine+5]+'\n'
            
        Content[controllerLine+4]="LightStatuses="
        for i in range(len(lightStatuses)):
            Content[controllerLine+4]=Content[controllerLine+4]+str(int(lightStatuses[i]))+','
        Content[controllerLine+4]=Content[controllerLine+4][:-1]
        Content[controllerLine+4]=Content[controllerLine+4]+'\n'

        Content[controllerLine+8]="TrainLightSignals="
        for i in range(len(trainLight)):
            Content[controllerLine+8]=Content[controllerLine+8]+str(int(trainLight[i]))+','
        Content[controllerLine+8]=Content[controllerLine+8][:-1]
        Content[controllerLine+8]=Content[controllerLine+8]+'\n'
        
        with open('ControllerSignals.txt','w') as file:
            file.writelines(Content)
                
        
    elif Content[1]=="CurrentWaysideNumber=10":
        controllerLine=findController("GreenController 10")
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        blockOccs=[int(i) for i in Content[controllerLine+1].split() if i.isdigit()]
        faultStatuses=[int(i) for i in Content[controllerLine+2].split() if i.isdigit()]
        switchPos=faultStatuses=[int(i) for i in Content[controllerLine+3].split() if i.isdigit()]
        lightStatuses=[int(i) for i in Content[controllerLine+4].split() if i.isdigit()]
        routedBlocks=[int(i) for i in Content[controllerLine+6].split() if i.isdigit()]
        underground=[int(i) for i in Content[controllerLine+7].split() if i.isdigit()]
        AuthChange=[]
        light=[]
        trainLight=[]

        for i in range(len(blockOccs)-1):
            AuthChange.append(blockOccs[i+1] or faultStatuses[i+1])
            light.append(blockOccs[i+1] or faultStatuses[i+1])
        
        for i in range(len(underground)):
            trainLight.append(underground[i])
        
        Content[controllerLine+5]="AuthZero="
        for i in range(len(AuthChange)):
            Content[controllerLine+5]=Content[controllerLine+5]+str(int(AuthChange[i]))+','
        Content[controllerLine+5]=Content[controllerLine+5][:-1]
        Content[controllerLine+5]=Content[controllerLine+5]+'\n'
            
        Content[controllerLine+4]="LightStatuses="
        for i in range(len(lightStatuses)):
            Content[controllerLine+4]=Content[controllerLine+4]+str(int(lightStatuses[i]))+','
        Content[controllerLine+4]=Content[controllerLine+4][:-1]
        Content[controllerLine+4]=Content[controllerLine+4]+'\n'

        Content[controllerLine+8]="TrainLightSignals="
        for i in range(len(trainLight)):
            Content[controllerLine+8]=Content[controllerLine+8]+str(int(trainLight[i]))+','
        Content[controllerLine+8]=Content[controllerLine+8][:-1]
        Content[controllerLine+8]=Content[controllerLine+8]+'\n'

        with open('ControllerSignals.txt','w') as file:
            file.writelines(Content)

    elif Content[1]=="CurrentWaysideNumber=11":
        controllerLine=findController("GreenController 11")
        with open('PLC_IO.txt','r') as file:
            Content=file.readlines()
        blockOccs=[int(i) for i in Content[controllerLine+1].split() if i.isdigit()]
        faultStatuses=[int(i) for i in Content[controllerLine+2].split() if i.isdigit()]
        switchPos=faultStatuses=[int(i) for i in Content[controllerLine+3].split() if i.isdigit()]
        lightStatuses=[int(i) for i in Content[controllerLine+4].split() if i.isdigit()]
        routedBlocks=[int(i) for i in Content[controllerLine+6].split() if i.isdigit()]
        underground=[int(i) for i in Content[controllerLine+7].split() if i.isdigit()]
        AuthChange=[]
        light=[]
        trainLight=[]

        for i in range(len(blockOccs)-1):
            AuthChange.append(blockOccs[i+1] or faultStatuses[i+1])
            light.append(blockOccs[i+1] or faultStatuses[i+1])
        
        for i in range(len(underground)):
            trainLight.append(underground[i])
        
        Content[controllerLine+5]="AuthZero="
        for i in range(len(AuthChange)):
            Content[controllerLine+5]=Content[controllerLine+5]+str(int(AuthChange[i]))+','
        Content[controllerLine+5]=Content[controllerLine+5][:-1]
        Content[controllerLine+5]=Content[controllerLine+5]+'\n'
            
        Content[controllerLine+4]="LightStatuses="
        for i in range(len(lightStatuses)):
            Content[controllerLine+4]=Content[controllerLine+4]+str(int(lightStatuses[i]))+','
        Content[controllerLine+4]=Content[controllerLine+4][:-1]
        Content[controllerLine+4]=Content[controllerLine+4]+'\n'

        Content[controllerLine+8]="TrainLightSignals="
        for i in range(len(trainLight)):
            Content[controllerLine+8]=Content[controllerLine+8]+str(int(trainLight[i]))+','
        Content[controllerLine+8]=Content[controllerLine+8][:-1]
        Content[controllerLine+8]=Content[controllerLine+8]+'\n'

        with open('ControllerSignals.txt','w') as file:
            file.writelines(Content)
        
