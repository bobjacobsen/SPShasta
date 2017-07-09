// UDrive the SP Shasta code line

int startpin = 7;  // 0 bit / 0v makes sound
int button = 8;  // pressed / 0v makes sound
int buzzerpin = 13; // 1 bit / 5V makes sound

// inputs 6 - 0 are available 
//
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
    pinMode(button, INPUT_PULLUP);
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

int counter = 0;

void loop() {
    
    // wait for start
    if (digitalRead(startpin) == 0  || digitalRead(button) == 0) {
      // check for real input
      delay(50);
      if (digitalRead(startpin) != 0  && digitalRead(button) != 0) return;
     
      counter++;
      
      // proceed to send
      setLine(1, longTime); 
    
      setLine(0, (  counter & 1) ? shortTime : longTime);
      setLine(1, (! counter & 1) ? shortTime : longTime);
      setLine(0, (  counter & 2) ? shortTime : longTime);
      setLine(1, (! counter & 2) ? shortTime : longTime);
      setLine(0, (  counter & 4) ? shortTime : longTime);
      setLine(1, (! counter & 4) ? shortTime : longTime);
      setLine(0, (  counter & 8) ? shortTime : longTime);
      setLine(1, (! counter & 8) ? shortTime : longTime);
        
      setLine(0, longTime); // clears the line
      
      # total time should be 50+6*longTime+4*shortTime = 2430

      // wait for idle input, to keep from repeating if something gets stuck
      while (digitalRead(startpin) == 0  || digitalRead(button) == 0) {
        delay(10);
      }
    }
}
