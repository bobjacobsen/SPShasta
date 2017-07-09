/*
    CMRIbuffer.cpp - LIbrary for access to a C/MRI network
    Created by Bob Jacobsen, February 2009
    Copyright, all rights reserved
*/

#include "Arduino.h"
#include "CMRIbuffer.h"

CMRIbuffer::CMRIbuffer() {
    index = 0;
    state = 1;
}

void CMRIbuffer::setup() {
  Serial.begin(19200);
}

void CMRIbuffer::loop() {
  // check for data
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    int newchar = Serial.read();
    // process it
    checkState(newchar);
  }
}

#define CMRI_FIND_STX           1
#define CMRI_DROP_DLE_FIND_STX  2
#define CMRI_CHECK_ADDRESS      3
#define CMRI_STORE_DATA         4
#define CMRI_STORE_DLE_DATA     5

void CMRIbuffer::checkState(int newchar) {
   switch (state) {
     case CMRI_FIND_STX:
       // waiting for STX
       if (newchar == 0x02) {
         // STX, now look for address
         state = CMRI_CHECK_ADDRESS;
       } else if (newchar == 0x10) {
         // DLE, drop next char
         state = CMRI_DROP_DLE_FIND_STX;
       }
       // otherwise, do nothing
       break;
       
     case CMRI_DROP_DLE_FIND_STX:
       // skip char after DLE while searching for STX
       state = CMRI_FIND_STX;
       break;
       
     case CMRI_CHECK_ADDRESS:
       // check address
       Serial.print(newchar);
       if (newchar == address) {
         // for this node, start accepting data
         state = CMRI_STORE_DATA;
         index = 0;
       } else {
         // command for some other node
         state = CMRI_FIND_STX;
       }
       break;
       
     case CMRI_STORE_DATA:
       // accumulating data
       if (newchar == 0x03) {
         // end of data
         Serial.println('/');
         state = CMRI_FIND_STX;
         msgComplete(index);
       } else if (newchar == 0x010) {
         // DLE, store char after
         state = CMRI_STORE_DLE_DATA;
       } else {
         // just data, store
         buffer[index++] = newchar;
       }
       break;
       
     case CMRI_STORE_DLE_DATA:
       // Store char after DLE
       buffer[index++] = newchar;
       state = CMRI_STORE_DATA;
       break;
       
     default:
       break;
   }
}

void CMRIbuffer::msgComplete(int index) {
  // process the data
}
