/*
    MotorSerialDriver - generalize a motor with a fixed position
    Created by Bob Jacobsen, February 2009
    Copyright, all rights reserved
*/

#ifndef MotorSerialDriver_h
#define MotorSerialDriver_h

#include "Arduino.h"

#include "PositioningMotor.h"

class MotorSerialDriver {
public:
    PositioningMotor& motor;
    
    MotorSerialDriver(PositioningMotor& m) : motor(m) {
    }
    
    void setup() {
      Serial.begin(9600);           // set up Serial library at 9600 bps
      Serial.println("s crash stop");
      Serial.println("i show info");
      Serial.println("< >  1 step CCW or CW");
      Serial.println("- + run CCW or CW");
      Serial.println("a Align zero on switch");
      Serial.println("r find and Report switch position");
      Serial.println("z set current position as Zero");
      Serial.println("m Move to zero");
      Serial.println("1 move to val1");
      Serial.println("2 move to val2");
      Serial.println("3 move to val3");
      
    }
    
    void loop() {
      // check for control request
      if (Serial.available() > 0) {
        // read the incoming byte:
        int ctlchar = Serial.read();
        
        switch (ctlchar) {
           case 's': 
             // crash stop
             motor.stepper_cmd = STEPPER_STOP;
             break;
           case 'i': 
             // print inputs
             motor.stepper_dump();
             break;
           case '.':
           case '>':
             // CW one spot
             motor.stepper_cmd = STEPPER_BUMP_FORWARD;
             break;
           case ',':
           case '<':
             // CCW one spot
             motor.stepper_cmd = STEPPER_BUMP_BACKWARD;
             break;
           case '=':
           case '+':
             // CW run
             motor.stepper_cmd = STEPPER_RUN_FORWARD;
             break;
           case '-':
           case '_':
             // CCW run
             motor.stepper_cmd = STEPPER_RUN_BACKWARD;
             break;

           case 'a':
             motor.align();
             break;
    
           case 'z':
             motor.position = 0;
             break;
             
           case 'r':
             // if on switch, bump off
             if (digitalRead(motor.switchPin) != 0) {
               motor.stepperMove(500, BACKWARD);
               delay(100);
             }
             motor.stepper_cmd = STEPPER_REPORT;
             break;         
    
           case 'm':
             motor.moveTo(0);
             break;
           
           case '1':
             motor.moveTo(11763);
             break;
             
           case '2':
             motor.moveTo(11499);
             break;
             
           case '3':
             motor.moveTo(11236);
             break;
             
           default:
             // just ignore
             break;
        }
      }
    
    }
};

#endif
