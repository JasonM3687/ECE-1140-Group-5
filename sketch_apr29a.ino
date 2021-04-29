#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <string.h>
#include <math.h>
#define joyX A0
#define joyY A1

using namespace std;

LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7,3,POSITIVE); //Set LCD I2C Address

//inputs
int routedBlocks [153] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int blockOccupancies [153] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int faultStatuses [153] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int underGround [153] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

//outputs
int SwitchOut [153];
int AuthChange [153];
int LightStatus [153];
int CrossStatus [153];

void setup() {
  //switch test
  routedBlocks[12] = 1;
  routedBlocks[0] = 1;
  blockOccupancies[0] = 0;
  blockOccupancies[12] = 0;
  blockOccupancies[11] = 0;
  
  //cross status test
  blockOccupancies[17] = 1;

  //light and auth test
  faultStatuses[12] = 1;
  
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin(20,4);

  lcd.setCursor(0,0);
  lcd.print("Inputs 0");
  lcd.setCursor(0,1);
  lcd.print("RB:");
  lcd.setCursor(0,2);
  lcd.print("BO:");
  lcd.setCursor(0,3);
  lcd.print("FS:");
  for(int k = 3; k < 20; k++)
  {
    printValueToLCD(0,k,1);
    printValueToLCD(0,k,2);
    printValueToLCD(0,k,3);
  }
  delay(500);
}

void printLCDInputs()
{
  //first lcd output
  int increment = 1;
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Inputs 0");
  lcd.setCursor(0,1);
  lcd.print("RB:");
  lcd.setCursor(0,2);
  lcd.print("BO:");
  lcd.setCursor(0,3);
  lcd.print("FS:");
  int i = 0;
  while(i <= 150)
  {
    lcd.setCursor(0,0);
    lcd.print(intputText(increment));
    for(int k = 3; k < 20; k++)
    {
      printValueToLCD(routedBlocks[i],k,1);
      printValueToLCD(blockOccupancies[i],k,2);
      printValueToLCD(faultStatuses[i],k,3);       
      i++;
    }
    increment++;
    delay(2000);
  }
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Inputs");
  lcd.setCursor(0,1);
  lcd.print("UG:");
  int p = 0;
  while(p <= 150)
  {
    lcd.setCursor(0,0);
    lcd.print(intputText(increment));
    for(int k = 3; k < 20; k++)
    {
      printValueToLCD(underGround[p],k,1);
      p++;
    }
    increment++;
    delay(2000);
  }
}

void printLCDOutputs()
{
  //first lcd output
  int increment2 = 1;
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(outputText(0));
  lcd.setCursor(0,1);
  lcd.print("SW:");
  lcd.setCursor(0,2);
  lcd.print("AC:");
  lcd.setCursor(0,3);
  lcd.print("LS:");
  int i = 0;
  while(i <= 150)
  {
    lcd.setCursor(0,0);
    lcd.print(outputText(increment2));
    for(int k = 3; k < 20; k++)
    {
      printValueToLCD(SwitchOut[i],k,1);
      printValueToLCD(AuthChange[i],k,2);
      printValueToLCD(LightStatus[i],k,3);       
      i++;
    }
    increment2++;
    delay(2000);
  }
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Output");
  lcd.setCursor(0,1);
  lcd.print("CS:");
  int p = 0;
  while(p <= 150)
  {
    lcd.setCursor(0,0);
    lcd.print(outputText(increment2));
    for(int k = 3; k < 20; k++)
    {
      printValueToLCD(CrossStatus[p],k,1);
      p++;
    }
    increment2++;
    delay(2000);
  }
}

void printValueToLCD(int num, int pos1, int pos2)
{
  lcd.setCursor(pos1,pos2);
  lcd.print(num);
}

String intputText(int num)
{
  String str = "Inputs";
  str += " ";
  str += num;
  return str;
}

String outputText(int num)
{
  String str = "Output";
  str += " ";
  str += num;
  return str;
}

void loop() {
  // put your main code here, to run repeatedly:
  
  SwitchOut[0]=routedBlocks[12] and routedBlocks[0] and not(blockOccupancies[0]) and not(blockOccupancies[12]) and not(blockOccupancies[11]);
  SwitchOut[1]=routedBlocks[28] and routedBlocks[29] and not(blockOccupancies[28]) and not(blockOccupancies[29]) and not(blockOccupancies[149]);
  SwitchOut[2]=routedBlocks[56] and routedBlocks[57] and not(blockOccupancies[56]) and not(blockOccupancies[57]);
  SwitchOut[3]=routedBlocks[62] and routedBlocks[61] and not(blockOccupancies[61]) and not(blockOccupancies[62]);
  SwitchOut[4]=routedBlocks[76] and routedBlocks[75] and not(blockOccupancies[75]) and not(blockOccupancies[76]) and not(blockOccupancies[100]);
  SwitchOut[5]=routedBlocks[84] and routedBlocks[85] and not(blockOccupancies[84]) and not(blockOccupancies[85]) and not(blockOccupancies[99]);

  CrossStatus[0] = blockOccupancies[17] or blockOccupancies[19];

  for(int i  = 0; i < 153; i++)
  {
    LightStatus[i]=underGround[i] and blockOccupancies[i];
  }

  for(int i = 0; i < 153; i++)
  {
    if(i==0)
    {
        LightStatus[0] = blockOccupancies[12] or blockOccupancies[11] or faultStatuses[12] or faultStatuses[11];
        AuthChange[0] = blockOccupancies[12] or blockOccupancies[11] or faultStatuses[12] or faultStatuses[11];
    }
    else if(i==12)
    {
        LightStatus[12] = blockOccupancies[0] or blockOccupancies[11] or faultStatuses[0] or faultStatuses[11];
        AuthChange[12] =  blockOccupancies[0] or blockOccupancies[11] or faultStatuses[0] or faultStatuses[11];
    }
    else if(i==149)
    {
        LightStatus[149] = blockOccupancies[28] or faultStatuses [28];
        AuthChange[149] = blockOccupancies[28] or faultStatuses[28];
    }
    else if(i==99)
    {
        LightStatus[99] = blockOccupancies[84] or blockOccupancies[83] or blockOccupancies[82] or blockOccupancies[81] or blockOccupancies[80] or blockOccupancies[79] or blockOccupancies[78] or blockOccupancies[77] or blockOccupancies[76] or faultStatuses[84];
        AuthChange[99]= blockOccupancies[84] or blockOccupancies[83] or blockOccupancies[82] or blockOccupancies[81] or blockOccupancies[80] or blockOccupancies[79] or blockOccupancies[78] or blockOccupancies[77] or blockOccupancies[76] or faultStatuses[84];
    }
    else
    {
        LightStatus[i] = blockOccupancies[i+1]  or faultStatuses[i+1] or blockOccupancies[i-1]  or faultStatuses[i-1];
        AuthChange[i] = blockOccupancies[i+1] or faultStatuses[i+1] or blockOccupancies[i-1]  or faultStatuses[i-1];
    }
  }
  printLCDInputs();
  printLCDOutputs();
}
