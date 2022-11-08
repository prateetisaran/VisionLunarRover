#include <PWM.h>

int motorPin=9;
int x=75; //initial value of variable
int32_t frequency = 900;

void setup()
{
  //initialize all timers except for 0, to save time keeping functions
  InitTimersSafe(); 
  Serial.begin(115200);
  Serial.setTimeout(1);

  //sets the frequency for the specified pin
  bool success = SetPinFrequencySafe(motorPin, frequency);
  Serial.println(success);
  
}


void loop(){
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.println(x);
  pwmWrite(motorPin, x);}



 /*
  pwmWrite(motorPin, x);
  Serial.println(x);
  delay(500);}

 */

 /*

  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.println(x);
  pwmWrite(motorPin, x);}

*/
  /*
 for (int i = 60; i < 90; i++){
   pwmWrite(motorPin, i);
   delay(1000);
   Serial.println(i);}}
   /*Serial.println("Starting running");
   pwmWrite(motorPin, x);
   delay(500);
   */

/*
int motorPin=9;
int x=0; //initial value of variable

void setup(){
  pinMode (motorPin, OUTPUT); //setting pin to be output
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop(){
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.println(x);
  analogWrite(motorPin, x);
  

}
*/
  
