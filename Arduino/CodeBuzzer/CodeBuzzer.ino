// Use a DC buzzer to send Morse for SP Shasta
//              Bob Jacobsen  2014

// Dunsmuir (Arduino Duemillo)
//int startpin = 10;  // input: 0 bit / 0v makes sound
//int buzzerpin = 13; // output: 1 bit / 5V makes sound

// Redding (LEDuino)
int startpin =  4;  // input: 0 bit / 0v makes sound
int buzzerpin = 13; // output: 1 bit / 5V makes sound

int slice = 75; // basic time slice, length of a dot

// Shield uses a 4N25 isolator with drive between buzzerpin and gnd,
// load to + and to output emitter

// For Continental (Railroad) Code, see http://w1tp.com/percode.htm
// Dunsmuir DR -.. .-..
// Redding RD .-.. -..

void setup() {
    pinMode(startpin, INPUT_PULLUP);
    digitalWrite(startpin, 1);
    pinMode(buzzerpin, OUTPUT);
    
    digitalWrite(buzzerpin, 0); // ensure off
}  

void loop() {
    // wait for start
    if (digitalRead(startpin) == 0) {
      // avoid noise spikes
      delay(50);
      if (digitalRead(startpin) != 0) return;
        
        // sound code
        letterR();
        interCharDelay();
        letterD();    

      // and and wait for rest of cycle length
      delay(5000);
    }
    // can sound continuously; do _not_ wait for input to go inactive then active again
}

void dot() {
    // short (.) plus inter-symbol delay
    digitalWrite(buzzerpin, 1);
    delay(slice);
    digitalWrite(buzzerpin, 0);
    delay(slice);
}

void dash() {
    // long (-) plus inter-symbol delay
    digitalWrite(buzzerpin, 1);
    delay(slice);
    delay(slice);
    digitalWrite(buzzerpin, 0);
    delay(slice);
}

void interCharDelay() {
    // three dot times
    delay(slice);
    delay(slice);
    delay(slice);
}

void letterR() {
    // Letter R (._..)
    dot();
    dash();
    dot();
    dot();
}

void letterD() {
    // Letter D  (-..)
    dash();
    dot();
    dot();
}

