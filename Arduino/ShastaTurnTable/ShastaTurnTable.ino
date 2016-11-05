#include "CMRIbuffer.h"
#include "AFMotor.h"

long encoderposition = 0;

// You can only use the "cmri" or "debugger" calls, not both
boolean debugSerial = false;  // true means no CMRI

#include "PositioningMotor.h"

#include "MotorButtonDriver.h"
#include "MotorSerialDriver.h"

PositioningMotor motor;
MotorButtonDriver buttons(motor);
MotorSerialDriver debugger(motor);

class MyCMRIbuffer : public CMRIbuffer {
  public:
    virtual void msgComplete(int index) {
       // copy the data into the motor commands
       long argument;
       argument = buffer[1]&0x0F;
       if (index > 2) argument = (argument*10) + (buffer[2]&0x0F);
       if (index > 3) argument = (argument*10) + (buffer[3]&0x0F);
       if (index > 4) argument = (argument*10) + (buffer[4]&0x0F);
       if (index > 5) argument = (argument*10) + (buffer[5]&0x0F);
       if (index > 6) argument = (argument*10) + (buffer[6]&0x0F);
       
       int cmd = buffer[0];
       
       if (cmd == 'm') {
           Serial.print("start move to");
           Serial.println(argument);
           motor.moveTo(argument);
       } else {
           Serial.print("motor cmd ");
           Serial.println(cmd);
           motor.stepper_cmd = cmd&0x0F;
       }
    };
};

MyCMRIbuffer cmri;

void setup() {
  encoder_setup();
  motor.setup();
  buttons.setup();
  if (debugSerial) {
    debugger.setup();
  } else {
    cmri.setAddress('0'+10);
    cmri.setup();
  }
  
  // on power-up, align on zero
  motor.align();
  if (debugSerial) Serial.println("setup done");
}

void loop() {
  encoder_loop();
  
  motor.loop();

  buttons.loop();
  if (debugSerial) {
    debugger.loop();
  } else {
    cmri.loop();
  }
}

// encoder, here for now

int encodernow = 0;
int encodersteps = 1024;
int encoderlaststep = 0;
long encoderoffset[] = {0, 8, 8+17, 8+17+12};  // 

void encoder_setup() {
  // set up encoder
  pinMode(5, INPUT);
  digitalWrite(5, 1);
  pinMode(6, INPUT);
  digitalWrite(6, 1);
  // read initial value
  encodernow = 0;
  if (digitalRead(5) == 1) encodernow |= 1; // A
  if (digitalRead(6) == 1) encodernow |= 2; // B

}

void encoder_loop() {
  // check inputs
  int encodernew = 0;
  if (digitalRead(5) == 1) encodernew |= 1; // A
  if (digitalRead(6) == 1) encodernew |= 2; // B
  // check for changes
  int encoderchanges = encodernow ^ encodernew;
  if (encoderchanges != 0) {
      switch (encoderchanges) {
        case 0:
        case 3:
          //Serial.print("***** error: was ");
          //Serial.print(encodernow);
          //Serial.print(" is ");
          //Serial.println(encodernew);
          break;
        case 1:
        case 2:
          //Serial.print("Now ");
          //Serial.print(encodernew);
          //Serial.print(" ");
          boolean down;
          switch (encodernow) {
            case 0:
              down = (encodernew == 2);
              break;
            case 1:
              down = (encodernew == 0);
              break;
            case 2:
              down = (encodernew == 3);
              break;
            case 3:
              down = (encodernew == 1);
              break;
          }

          if (down) {
            encoderposition--;
            if (encoderposition<0) encoderposition += encodersteps;
            Serial.print("\\");
            Serial.print(encoderposition);
            Serial.print(" "); Serial.print(encodernew);
            Serial.print(" "); Serial.print(motor.position);
            Serial.print(" "); Serial.print(motor.position - encoderlaststep);
            Serial.print(" "); Serial.print(encoderoffset[encoderposition&0x3]);
            long newposition = ((encoderposition>>2)*(13200/16))/16+encoderoffset[encoderposition&0x3];
            motor.position = newposition;
            Serial.print(" "); Serial.println(motor.position);
            encoderlaststep = motor.position;
          } else {
            encoderposition++;
            if (encoderposition>=encodersteps) encoderposition -= encodersteps;
            Serial.print("/");
            Serial.print(encoderposition);
            Serial.print(" "); Serial.print(encodernew);
            Serial.print(" "); Serial.print(motor.position);
            Serial.print(" "); Serial.print(motor.position - encoderlaststep);
            
            long delta;
            if ((encoderposition&0x3) == 0) {
              Serial.print(" .");
            } else {
              Serial.print(" "); Serial.print(encoderoffset[encoderposition&0x3] - encoderoffset[(encoderposition&0x3)-1]);
            }
            
            long newposition = ((encoderposition>>2)*(13200/16))/16+encoderoffset[encoderposition&0x3];
            motor.position = newposition;
            Serial.print(" "); Serial.println(motor.position);
            encoderlaststep = motor.position;
          }
          break;
      }
      encodernow = encodernew;
  }
}

//void encodersetposition() {
//   // set pseudo-step
//   long newstepposition = (encoderposition>>2)*13200*4/encodersteps;
//   newstepposition += encoderoffset[encodernow];
//}
