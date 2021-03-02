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

byte rowPins[ROWS] = {38, 40, 42, 44}; 
byte colPins[COLS] = {46, 48, 50, 52}; 

Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 
String keypad_input;
String trainSpeed;
String kp;
String ki;
String temperature;
//-------------------------------------------------------
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE); //Set LCD I2C Address for LCD



void setup() {
  Serial.begin(2000000);
  keypad_input.reserve(3); //Reserves 4 inputs max per keypad input

  lcd.begin(20, 4); //Initializes cols/rows of LCD

//-------------------- Digital Output/Input Setup --------------------
  //Sets digital pin 2 as output (Headlights)
  pinMode(2, OUTPUT);
  //Sets digital pin 3 as output (Internal lights)
  pinMode(3, OUTPUT);
  //Sets digital pin 4 as output (Service Break)
  pinMode(4, OUTPUT);
  //Sets digital pin 5 as output (Emergency Break)
  pinMode(5, OUTPUT);
  //Sets digital pin 6 as output (Open/Close Doors)
  pinMode(6, OUTPUT);
  //Sets digital pin 7 as output (Intercom)
  pinMode(7, OUTPUT);
  //Sets digital pin 9 as output (Automatic Mode)
  pinMode(9, OUTPUT);
  
  //Sets digital pin 8 as input (Automatic Mode Switch)
  pinMode(8, INPUT);
  //Sets digital pin 36 as input (Headlight Switch)
  pinMode(36, INPUT);
   //Sets digital pin 34 as input (Internal light Switch)
  pinMode(34, INPUT);
   //Sets digital pin 32 as input (Service Brake Switch)
  pinMode(32, INPUT);
   //Sets digital pin 30 as input (Emergency Brake Switch)
  pinMode(30, INPUT);
   //Sets digital pin 28 as input (Open/Close door Switch)
  pinMode(28, INPUT);
   //Sets digital pin 26 as input (Intercom Switch)
  pinMode(26, INPUT);
  //Sets digital pin 53 as input (Engine on/off Switch)
  pinMode(53, INPUT);
//----------------------------------------------------------------------


}

void loop() {
  int read8 = digitalRead(8);
  int read36 = digitalRead(36);
  int read34 = digitalRead(34);
  int read32 = digitalRead(32);
  int read30 = digitalRead(30);
  int read28 = digitalRead(28);
  int read26 = digitalRead(26);
  int read53 = digitalRead(53);

 if (read53 == HIGH) {
    
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
  if (read8 == LOW) {
  //LCD Display setup
  lcd.setCursor(0, 0);
  lcd.print("Speed:");
  lcd.setCursor(9,0);
  lcd.print("MPH");
  lcd.setCursor(0, 1);
  lcd.print("Kp:   Ki:    ");
  lcd.setCursor(0, 2);
  lcd.print("BCN: Pittsburgh,PA");
  lcd.setCursor(0, 3);
  lcd.print("Fault Status: N/A");
  lcd.setCursor(6, 0);
  lcd.print(trainSpeed);
  lcd.setCursor(3,1);
  lcd.print(kp);
  lcd.setCursor(9,1);
  lcd.print(ki);
  lcd.setCursor(13,0);
  lcd.print("Tmp:");
  lcd.setCursor(17,0);
  lcd.print(temperature);
  }

  //Sets Headlight pin high if switch is pressed
  if (read36 == HIGH) {
       digitalWrite(2, HIGH);
       Serial.print("Headlights: On\n");
  }
  else if (read36 == LOW) {
       digitalWrite(2,LOW);
       Serial.print("Headlights: Off\n");
  }
//Sets internal light pin high if switch is pressed
  if (read34 == HIGH) {
      digitalWrite(3, HIGH);
      Serial.print("Internal Lights: On\n");
  }
  else if (read34 == LOW) {
      digitalWrite(3, LOW);
      Serial.print("Internal Lights: Off\n");
  }
  //Sets Service Brake high if switch is pressed
  if (read32 == HIGH) {
      digitalWrite(4, HIGH);
      Serial.print("Service Break Initialized\n");
      delay(2000);
      trainSpeed = "000";
  }
  else if (read32 == LOW) {
      digitalWrite(4, LOW);
  }
 //Sets Emergency Brake high if switch is pressed
 if (read30 == HIGH ) {
      //Sets Emergency Break high
      digitalWrite(5, HIGH);
      //Waits 1/4 Sec
      delay(250);
      //Sets Emergency Break low
      digitalWrite(5, LOW);
      //Waits 1/4 Sec
      delay(250);
     //Sets Emergency Break high
      digitalWrite(5, HIGH);
      Serial.print("Emergency Break Initialized\n");
      trainSpeed = "000";
 }
 else if (read30 == LOW) {
      digitalWrite(5, LOW);
 }
 //Opens doors if switch is pressed
 if (read28 == HIGH) {
      digitalWrite(6, HIGH);
      Serial.print("Doors are open\n");
 }
 else if (read28 == LOW) {
      digitalWrite(6, LOW);
      Serial.print("Doors are closed\n");
 }
//Turns on intercom for driver to speak if button is pressed
 if (read26 == HIGH) {
      digitalWrite(7, HIGH);
      Serial.print("Transit Driver is Speaking...\n");
 }
 else if (read26 == LOW) {
      digitalWrite(7, LOW);
 }
//Initiliazes Automatic Mode
 if (read8 == HIGH) {
      digitalWrite(9, HIGH);
      Serial.print("Automatic Mode Initialized\n");
 }
 else if (read8 == LOW) {
      digitalWrite(9, LOW);
 }

}
else
    //Engine is off
      lcd.clear();
   
}
