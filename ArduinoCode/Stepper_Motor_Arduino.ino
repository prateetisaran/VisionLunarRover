// Overshoot.pde
// -*- mode: C++ -*-
//
// Check overshoot handling
// which sets a new target position and then waits until the stepper has 
// achieved it. This is used for testing the handling of overshoots
//
// Copyright (C) 2009 Mike McCauley
// $Id: Overshoot.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $
#include <AccelStepper.h>
int x;
// Define a stepper and the pins it will use
AccelStepper stepper(AccelStepper::FULL2WIRE, 9, 8); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5

void setup()
{ 
  stepper.setMaxSpeed(1000);//set Max possible
  stepper.setAcceleration(1000);//set Max possible
   Serial.begin(115200);
  Serial.setTimeout(1); 
  digitalWrite(13,LOW);
  
}

void loop()
{ 
  while (!Serial.available());
  x = Serial.readString().toInt(); 
  stepper.runToNewPosition(x);
  Serial.println(x);\
  delay(100);
}
