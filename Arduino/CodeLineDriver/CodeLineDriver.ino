// UDrive the SP Shasta code line

int startpin = 8;  // 0 bit / 0v makes sound
int buzzerpin = 13; // 1 bit / 5V makes sound

// Shield uses a 4N25 isolator with input to pin and gnd,
// load to + and to output emitter

// Ansaldo 506 manual page labeled 33 says pulses are 1/10 and 1/3, alternating open and closed.

// 16 pulses
// first is always long
// 7 pulses (3 long 4 short) to select station
// 7 pulses (each long or short) for setting conditions
// last is always long

void setup() {
    pinMode(startpin, INPUT_PULLUP);
    pinMode(buzzerpin, OUTPUT);
    
    digitalWrite(buzzerpin, 0); // ensure off
}  

int shortTime = 100;
int longTime = 330;

void setLine(int val, int time) {
      digitalWrite(buzzerpin, val);
      digitalWrite(13, val); // LED follows output
      delay(time);
}

void loop() {
    if (digitalRead(startpin) == 0) {

      setLine(1, longTime); 
    
      setLine(0, shortTime);
      setLine(1, longTime);
      setLine(0, shortTime);
      setLine(1, longTime);
      setLine(0, shortTime);
      setLine(1, longTime);
      setLine(0, shortTime);
    
      //setLine(1, longTime);
      //setLine(0, shortTime);
      //setLine(1, longTime);
      //setLine(0, shortTime);
      //setLine(1, longTime);
      //setLine(0, shortTime);
      //setLine(1, shortTime);
    
      setLine(0, longTime); // clears the line

      // and cycle wait before checking again to avoid overheat
      delay(200);

    }
}
