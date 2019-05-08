// Drive the SP Shasta code line

int longstartpin = 7;  // 0 bit / 0v makes sound
int shortstartpin = 6;  // 0 bit / 0v makes sound
int button = 8;  // pressed / 0v makes sound
int buzzerpin = 13; // 1 bit / 5V makes drives line and Code led

int inputActive = 0; // 0 is active input

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
    pinMode(longstartpin, INPUT_PULLUP);
    pinMode(shortstartpin, INPUT_PULLUP);
    pinMode(button, INPUT_PULLUP);
    pinMode(buzzerpin, OUTPUT);
    
    digitalWrite(buzzerpin, 0); // ensure off
}  

int shortTime = 100;
int longTime = 330;
int debounceTime = 10;

// set output
void setLine(int val) {
      digitalWrite(buzzerpin, val);
} 

// set output and wait
void setLine(int val, int time) {
      setLine(val);
      delay(time);
}

// Drive machine through short (xmt) sequence
void driveShortSequence() {
    setLine(1, shortTime);
    setLine(0, 5*longTime);
    setLine(1, shortTime);
}

// Drive machine through long (rcv) sequence
void driveLongSequence() {
    setLine(1, longTime);
}

boolean anyInputsAreActive() {
  return (digitalRead(longstartpin) == inputActive || digitalRead(shortstartpin) == inputActive || digitalRead(button) == inputActive);
}

void loop() {
      // we run the sequence on first power up, putting control check at end
           
      // proceed to send
      if (digitalRead(longstartpin) == inputActive) driveLongSequence();
      else driveShortSequence();
     
      setLine(0); // clears the line

      // spin-wait for idle input, to keep from repeating if something gets stuck
      while (anyInputsAreActive()) {
        delay(debounceTime);
      }

      // at this point both are inactive
      
      // spin-wait for start
      while (true) {
        if  (anyInputsAreActive()) {
          // check for real input by waiting
          delay(debounceTime);
          if (anyInputsAreActive()) break; // send again if still active
        }
      }
}
