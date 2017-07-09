/*
    CMRIbuffer.cpp - LIbrary for access to a C/MRI network
    Created by Bob Jacobsen, February 2009
    Copyright, all rights reserved
*/

#ifndef CMRIbuffer_h
#define CMRIbuffer_h

//#include "WConstants.h"

// Load CMRI buffer

class CMRIbuffer {

public:

    CMRIbuffer();
    void setup();
    void loop();
    void setAddress(int addr) { address = addr; }
    
protected:

    void checkState(int newchar);
    virtual void msgComplete(int index);
    
    int address;    
    int buffer[25];
    int index;
    int state;

};

#endif 
