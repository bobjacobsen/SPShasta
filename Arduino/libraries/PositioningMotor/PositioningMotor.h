/*
    PositioningMotor - generalize a motor with a fixed position
    Created by Bob Jacobsen, February 2009
    Copyright, all rights reserved
*/

#ifndef PositioningMotor_h
#define PositioningMotor_h

#include "Arduino.h"

// AFMotor v2 from http://www.ladyada.net/make/mshield/download.html
//#include "AFMotor.h"

AF_Stepper stepper(48, 1); // create 1st stepper, 48 steps before divide by 50, 5.5

class PositioningMotor {
public:
    PositioningMotor() {
        position = 0;
        direction = FORWARD;

        // full rotation is 48*50*5.5 = 13,200 steps
        stepsPerTurn = 48*50*5.5;
        
        // 6*2 steps is a rail width
        // backlash is more like 60, but don't want to overshoot
        backlash = 50;
        overshoot = 300;
        
        bumpstep = 1;  // movement for a "bump" operation
        runstep = 1;   // atom of movement for a "move" operation
        
        // full speed is rotation at 1 RPM final, 5.5 at spur, 5.5*50 at motor
        baserate = (5.5*50)*1/2;    // 1/2 RPM base rate
        
        switchPin = 10;
        runningPin = 13;
        
        // motor current
        mode = DOUBLE;  // SINGLE, DOUBLE, INTERLEAVE, MICROSTEP
    }
    
    int position;
    int direction;
    
    // full rotation is 48*50*5.5 = 13,200 steps times 2 for meta-turn
    int stepsPerTurn;
    
    // 6*2 steps is a rail width
    // backlash is more like 60, but don't want to overshoot
    int backlash;
    // how far to overshoot on a position move
    int overshoot;
    
    int bumpstep;  // total move for a "bump" operation
    int runstep;  // atom of movement for a "move" operation
    
    // full speed is rotation at 1 RPM final, 5.5 at spur, 5.5*50 at motor
    //int baserate = (5.5*50)*1/2;    // 1/2 RPM base rate
    int baserate;
    
    int switchPin;
    int runningPin;
    
    unsigned long stopPosition;
    
    void setup() {
      pinMode(switchPin, INPUT);
      pinMode(runningPin, OUTPUT);
    }
    
    #define STEPPER_STOP        0
    #define STEPPER_ALIGN       1
    #define STEPPER_RUN_BACKWARD    2
    #define STEPPER_RUN_FORWARD   3
    #define STEPPER_BUMP_BACKWARD   4
    #define STEPPER_BUMP_FORWARD  5
    #define STEPPER_REPORT      6
    #define STEPPER_MOVE_FORWARD_TO_POSN 7
    #define STEPPER_MOVE_BACKWARD_TO_POSN 8
    
    int stepper_cmd;
    
    int mode;  // SINGLE, DOUBLE, INTERLEAVE, MICROSTEP
    
    void loop() {
      switch (stepper_cmd) {
        case STEPPER_STOP: 
          // drop current
          //stepper.release();
          digitalWrite(runningPin, 0);
          break;
        case STEPPER_ALIGN:
        case STEPPER_REPORT:
          // run until switch active
          digitalWrite(runningPin, 1);
          if (digitalRead(switchPin) == 0) {
            stepper.setSpeed(baserate);
            stepper.step(1, FORWARD, mode);
            position += 1;
            checkEnd();
          } else {
            if (stepper_cmd == STEPPER_ALIGN) {
              Serial.print("   @"); Serial.println(position);
              position = 0;
              encoderposition = 0;
            } else {
              stepper_dump();
            }
            stepper_cmd = STEPPER_STOP;
          }
          break;
        case STEPPER_RUN_BACKWARD: 
          stepperMove(runstep, BACKWARD);
          break;
        case STEPPER_RUN_FORWARD: 
          stepperMove(runstep, FORWARD);
          break;
        case STEPPER_BUMP_BACKWARD: 
          stepperMove(bumpstep, BACKWARD);
          stepper_cmd = STEPPER_STOP;
          break;
        case STEPPER_BUMP_FORWARD: 
          stepperMove(bumpstep, FORWARD);
          stepper_cmd = STEPPER_STOP;
          break;
        case STEPPER_MOVE_FORWARD_TO_POSN:
          {
            if ( (position >= stopPosition) && (position < stopPosition+20) ) {
              stepper_cmd = STEPPER_STOP;
            } else {
              move(1, FORWARD);
            }
          }
          break;
        case STEPPER_MOVE_BACKWARD_TO_POSN:
          { // find distance to final spot, moving backwards
            long target = stopPosition - overshoot;
            if (target < 0) target += stepsPerTurn;
            
            if ( (position <= target) && (position > target-20) ) {
              stepper_cmd = STEPPER_MOVE_FORWARD_TO_POSN;
            } else {
              move(1, BACKWARD);
            }
          }
          break;
        default:
          break;
      }
    }
    
    void stepper_dump() {
         Serial.print("P: ");
         Serial.println(position);
    }
    
    void align() {
      // if on switch, bump off
      if (digitalRead(switchPin) != 0) {
        stepperMove(500, BACKWARD);
        delay(100);
      }
      // align and zero
      stepper_cmd = STEPPER_ALIGN;
    }
    
    // Move, keeping track of position
    void move(int steps, int dir) {
          digitalWrite(runningPin, 1);
          stepper.setSpeed(baserate);
          stepper.step(steps, dir, mode);

          // record move            
          if (dir == FORWARD) {
            position += steps;
          } else {
            position -= steps;
          }
          checkEnd();
    }
    
    // Move, correcting for backlash on direction change
    void stepperMove(int steps, int dir) {
          // basic move
          move(steps, dir);
          
          // do backlash correction
          if (dir == FORWARD) {
            if (direction == BACKWARD) removeBacklash(FORWARD);
          } else {
            if (direction == FORWARD) removeBacklash(BACKWARD);
          }
    }
    
    void moveTo(unsigned long newPos) {
        // section to find optimal move direction
        long move = newPos - position;
        if (move > stepsPerTurn/2) move -= stepsPerTurn;
        if (move < -stepsPerTurn/2) move += stepsPerTurn;
        
        stopPosition = newPos;
        if (position == stopPosition) {
            stepper_cmd = STEPPER_STOP;
        } else if (move > 0) {
            stepper_cmd = STEPPER_MOVE_FORWARD_TO_POSN;
        } else {
            stepper_cmd = STEPPER_MOVE_BACKWARD_TO_POSN;
        }
    }
    
    // take out backlash
    void removeBacklash(int dir) {
      direction = dir;
      stepperMove(backlash, dir);
    }
    
    void checkEnd() {
        if (position >= stepsPerTurn) 
          position -= stepsPerTurn;
        else if (position < 0) 
          position += stepsPerTurn;
    }

};

#endif 
