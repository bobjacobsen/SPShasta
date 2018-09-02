// Use a DC buzzer to send Morse for SP Shasta

// Dunsmuir (Arduini Duemillo)
//int startpin = 10;  // 0 but / 0v makes sound
//int buzzerpin = 13; // 1 bit / 5V makes sound

// Redding (LEDuino)
int startpin = 4;  // 0 but / 0v makes sound
int buzzerpin = 13; // 1 bit / 5V makes sound

int slice = 75; // basic time slice, length of a dot

// Shield uses a 4N25 isolator with input to pin and gnd,
// load to + and to output emitter

// for continental code, see http://w1tp.com/percode.htm
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
      // check for real input
      delay(50);
      if (digitalRead(startpin) != 0) return;
        
        letterR();
        interCharDelay();
        letterD();    

      // and and wait for rest of cycle length
      delay(5000);
    }
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

