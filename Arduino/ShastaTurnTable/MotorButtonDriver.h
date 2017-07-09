/*
    MotorButtonDriver - generalize a motor with a fixed position
    Created by Bob Jacobsen, February 2009
    Copyright, all rights reserved
*/

#ifndef MotorButtonDriver_h
#define MotorButtonDriver_h

#include "Arduino.h"

//
// The button pins are "zero means pressed"
//

#include "PositioningMotor.h"

void set_last_position();

class MotorButtonDriver {
public:
    MotorButtonDriver(PositioningMotor& m) : motor(m) {
        runLeftPin = 19;
        runLeftVal = 1;
        
        bumpLeftPin = 14;
        bumpLeftVal = 1;
        
        setZeroPin = 15;
        setZeroVal = 1;
        
        bumpRightPin = 16;
        bumpRightVal = 1;
        
        runRightPin = 17;
        runRightVal = 1;
        
        rptMillis = 200;
        
        serialDebug = false;
    }
    
    bool serialDebug;  // print button pushes?
    
    PositioningMotor& motor;
    
    int runLeftPin;
    int runLeftVal;
    
    int bumpLeftPin;
    int bumpLeftVal;
    
    int setZeroPin;
    int setZeroVal;
    
    int bumpRightPin;
    int bumpRightVal;
    
    int runRightPin;
    int runRightVal;
    
    unsigned long buttonDownTime;
    unsigned long rptMillis;
    
    void setup() {
      // set modes, pullups
      pinMode(runLeftPin, INPUT);
      digitalWrite(runLeftPin,1);
      
      pinMode(bumpLeftPin, INPUT);
      digitalWrite(bumpLeftPin,1);
      
      pinMode(setZeroPin, INPUT);
      digitalWrite(setZeroPin,1);
      
      pinMode(bumpRightPin, INPUT);
      digitalWrite(bumpRightPin,1);
      
      pinMode(runRightPin, INPUT);
      digitalWrite(runRightPin,1);
      
      pinMode(runLeftPin, INPUT);
      digitalWrite(runLeftPin,1);
    }
    
    void loop() {
      int pinNow;
    
      if (digitalRead(runLeftPin) == 0)  
        if (serialDebug) Serial.print("-");
      if (digitalRead(runRightPin) == 0)
        if (serialDebug) Serial.print("+");
      if (digitalRead(bumpLeftPin) == 0)
        if (serialDebug) Serial.print("<");
      if (digitalRead(bumpRightPin) == 0)
        if (serialDebug) Serial.print(">");
      if (digitalRead(setZeroPin) == 0)
        if (serialDebug) Serial.print("z");
      
      pinNow = digitalRead(runLeftPin);  
      if (pinNow != runLeftVal) {
        if (pinNow == 0) {
          motor.stepper_cmd = STEPPER_RUN_BACKWARD;
        } else {
          motor.stepper_cmd = STEPPER_STOP;      
        }
        runLeftVal = pinNow;
      }
      
      pinNow = digitalRead(runRightPin);  
      if (pinNow != runRightVal) {
        if (pinNow == 0) {
          motor.stepper_cmd = STEPPER_RUN_FORWARD;      
        } else {
          motor.stepper_cmd = STEPPER_STOP;      
        }
        runRightVal = pinNow;
      }
      
      pinNow = digitalRead(bumpLeftPin);  
      if (pinNow != bumpLeftVal) {
        if (pinNow == 0) {
          motor.stepper_cmd = STEPPER_BUMP_BACKWARD;      
          buttonDownTime = millis();
        }
        bumpLeftVal = pinNow;
      }
      
      pinNow = digitalRead(bumpRightPin);  
      if (pinNow != bumpRightVal) {
        if (pinNow == 0) {
          motor.stepper_cmd = STEPPER_BUMP_FORWARD;      
          buttonDownTime = millis();
        }
        bumpRightVal = pinNow;
      }
      
      pinNow = digitalRead(setZeroPin);  
      if (pinNow != setZeroVal) {
        if (pinNow == 0) {
          // set current position to last commanded position
          // so that we're on target now
          set_last_position();
          
          // previous commands to move to switch and zero
          // motor.stepper_cmd = STEPPER_ALIGN;
          // if (serialDebug) Serial.println("align");
        }
        setZeroVal = pinNow;
      } // end processing changes
      
      // now look for buttons held down
      if (buttonDownTime+rptMillis < millis()) {
        // time to tick
        buttonDownTime = millis();
        
        if (digitalRead(bumpRightPin) == 0) {
          // repeat bump
          motor.stepper_cmd = STEPPER_BUMP_FORWARD;
        }
        
        if (digitalRead(bumpLeftPin) == 0) {
          // repeat bump
          motor.stepper_cmd = STEPPER_BUMP_BACKWARD;
        }
        
      }  // end processing held
    }
};

#endif 
