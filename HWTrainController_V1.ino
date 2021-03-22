//Written by Jason Matuszak
//University of Pittsburgh ECE 1140

#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <Keypad.h> 

//-------------------- Keypad Setup --------------------
const byte ROWS = 4; 
const byte COLS = 4;

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {23, 22, 25, 26}; 
byte colPins[COLS] = {29, 30, 33, 34}; 

Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 
String keypad_input;
String trainSpeed = "000";
String kp;
String ki;
String temperature = "075";
String power;
//-------------------------------------------------------
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE); //Set LCD I2C Address for LCD



void setup() {
  Serial.begin(200000);
  keypad_input.reserve(3); //Reserves 4 inputs max per keypad input

  lcd.begin(20, 4); //Initializes cols/rows of LCD

//-------------------- Digital Output/Input Setup --------------------
  //Sets digital pin 49 as output (Headlights)
  pinMode(49, OUTPUT);
  //Sets digital pin 48 as output (Internal lights)
  pinMode(48, OUTPUT);
  //Sets digital pin 44 as output (Service Break)
  pinMode(44, OUTPUT);
  //Sets digital pin 6 as output (Emergency Break)
  pinMode(6, OUTPUT);
  //Sets digital pin 3 as output (Open/Close Doors)
  pinMode(3, OUTPUT);
  //Sets digital pin 40 as output (Intercom)
  pinMode(40, OUTPUT);
  //Sets digital pin 11 as output (Automatic Mode)
  pinMode(11, OUTPUT);
  
  //Sets digital pin 13 as input (Automatic Mode Switch)
  pinMode(13, INPUT);
  //Sets digital pin 53 as input (Headlight Switch)
  pinMode(53, INPUT);
   //Sets digital pin 52 as input (Internal light Switch)
  pinMode(52, INPUT);
   //Sets digital pin 45 as input (Service Brake Switch)
  pinMode(45, INPUT);
   //Sets digital pin 5 as input (Emergency Brake Switch)
  pinMode(5, INPUT);
   //Sets digital pin 2 as input (Open/Close door Switch)
  pinMode(2, INPUT);
   //Sets digital pin 41 as input (Intercom Switch)
  pinMode(41, INPUT);
  //Sets digital pin 37 as input (Engine on/off Switch)
  pinMode(37, INPUT);
//----------------------------------------------------------------------


}

void loop() {
  int read37 = digitalRead(37); 
 
 // If engine is on
 if (read37 == HIGH) {
    
  setKeypadLCD();
  
  setHeadlights();
  setInternalLights();
  setServiceBrake();
  setEmergencyBrake();
  setDoors();
  setIntercom();
  setAutomaticMode();

}
else
    //Engine is off
      lcd.clear();  
}

void setHeadlights() {
    int read53 = digitalRead(53);
    //Sets Headlight pin high if switch is pressed
  if (read53 == HIGH) {
       digitalWrite(49, HIGH);
       Serial.print("Headlights: On\n");
  }
  else if (read53 == LOW) {
       digitalWrite(49,LOW);
       Serial.print("Headlights: Off\n");
  }

}

void setInternalLights() {
  int read52 = digitalRead(52);
  //Sets internal light pin high if switch is pressed
  if (read52 == HIGH) {
      digitalWrite(48, HIGH);
      Serial.print("Internal Lights: On\n");
  }
  else if (read52 == LOW) {
      digitalWrite(48, LOW);
      Serial.print("Internal Lights: Off\n");
  }
}

void setServiceBrake() {
  int read45 = digitalRead(45); 
  //Sets Service Brake high if switch is pressed
  if (read45 == HIGH) {
      digitalWrite(44, HIGH);
      Serial.print("Service Break Initialized\n");
      delay(2000);
      trainSpeed = "000";
  }
  else if (read45 == LOW) {
      digitalWrite(44, LOW);
  }
}

void setEmergencyBrake() {
  int read5 = digitalRead(5);
  //Sets Emergency Brake high if switch is pressed
 if (read5 == HIGH ) {
      //Sets Emergency Break high
      digitalWrite(6, HIGH);
      //Waits 1/4 Sec
      delay(250);
      //Sets Emergency Break low
      digitalWrite(6, LOW);
      //Waits 1/4 Sec
      delay(250);
     //Sets Emergency Break high
      digitalWrite(6, HIGH);
      Serial.print("Emergency Break Initialized\n");
      trainSpeed = "000";
 }
 else if (read5 == LOW) {
      digitalWrite(6, LOW);
 }
}

void setDoors() {
  int read2 = digitalRead(2);
  //Opens doors if switch is pressed
 if (read2 == HIGH) {
      digitalWrite(3, HIGH);
      Serial.print("Doors are open\n");
 }
 else if (read2 == LOW) {
      digitalWrite(3, LOW);
      Serial.print("Doors are closed\n");
 }
}

void setIntercom(){
   int read41 = digitalRead(41); 
  //Turns on intercom for driver to speak if button is pressed
 if (read41 == HIGH) {
      digitalWrite(40, HIGH);
      Serial.print("Transit Driver is Speaking...\n");
 }
 else if (read41 == LOW) {
      digitalWrite(40, LOW);
 }
}

void setAutomaticMode() {
   int read13 = digitalRead(13); 
  //Initiliazes Automatic Mode
 if (read13 == HIGH) {
      digitalWrite(11, HIGH);
      Serial.print("Automatic Mode Initialized\n");
 }
 else if (read13 == LOW) {
      digitalWrite(11, LOW);
 }

}

void setKeypadLCD() {
   //Keypad scanning algorithm to set Speed, Kp, Ki, and Temperature/Climate Values
  char key = customKeypad.getKey();

   if (key){
  
     if(key == '#') {
       trainSpeed = keypad_input;
      keypad_input = ""; // clear keypad input
    }
    else if(key == 'A') {
      kp = keypad_input;
      keypad_input = "";
    }
    else if (key == 'B') {
      ki = keypad_input;
      keypad_input = "";
    }
    else if (key == 'C') {
      temperature = keypad_input;
      keypad_input = "";
    }
    else {
      keypad_input += key; // append new character to keypad input string
    }
  }
  
  //LCD Display setup
  lcd.setCursor(0, 0);
  lcd.print("Speed:");
  lcd.setCursor(9,0);
  lcd.print("MPH");
  lcd.setCursor(0, 1);
  lcd.print("Power:00000W");
  lcd.setCursor(0, 2);
  lcd.print("BCN: Pittsburgh,PA");
  lcd.setCursor(0, 3);
  lcd.print("FS: N/A");
  lcd.setCursor(6, 0);
  lcd.print(trainSpeed);
  lcd.setCursor(13,1);
  lcd.print(kp);
  lcd.setCursor(17,1);
  lcd.print(ki);
  lcd.setCursor(13,0);
  lcd.print("Tmp:");
  lcd.setCursor(17,0);
  lcd.print(temperature);
}
