// Use a DC buzzer to send Morse for SP Shasta

int startpin = 10;  // 0 but / 0v makes sound
int buzzerpin = 13; // 1 bit / 5V makes sound

// Shasta shield uses a 4N25 isolator with input to pin and gnd,
// load to + and to output emitter

// for continental code, see http://w1tp.com/percode.htm
// Dunsmuir DR -.. .-..
// Redding RD .-.. -..

void setup() {
    pinMode(startpin, INPUT);
    digitalWrite(startpin, 1);
    pinMode(buzzerpin, OUTPUT);
    
    digitalWrite(buzzerpin, 0); // ensure off
}  

int slice = 75;

void loop() {
    if (digitalRead(startpin) == 0) {

      // write D  (-..)
      digitalWrite(buzzerpin, 1);
      delay(slice);
      delay(slice);
      digitalWrite(buzzerpin, 0);
      delay(slice);
      //
      digitalWrite(buzzerpin, 1);
      delay(slice);
      digitalWrite(buzzerpin, 0);
      delay(slice);
      //
      digitalWrite(buzzerpin, 1);
      delay(slice);
      digitalWrite(buzzerpin, 0);
      delay(slice);

      // inter-char
      delay(slice);
      delay(slice);
      delay(slice);
    
      // write R (._..)
      digitalWrite(buzzerpin, 1);
      delay(slice);
      digitalWrite(buzzerpin, 0);
      delay(slice);
      // 
      digitalWrite(buzzerpin, 1);
      delay(slice);
      delay(slice);
      digitalWrite(buzzerpin, 0);
      delay(slice);
      //
      digitalWrite(buzzerpin, 1);
      delay(slice);
      digitalWrite(buzzerpin, 0);
      delay(slice);
      //
      digitalWrite(buzzerpin, 1);
      delay(slice);
      digitalWrite(buzzerpin, 0);
      delay(slice);

      // and cycle wait
      delay(5000); // was 5000
    }
}
