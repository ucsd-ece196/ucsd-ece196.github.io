// set the pin numbers we connected the leds to.
#define LED_RED 5
#define LED_GRN 6
#define LED_BLU 7

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pins for LED as an output.
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GRN, OUTPUT);
  pinMode(LED_BLU, OUTPUT);
  Serial.begin(9600);
}

void handleLedState(char inByte){
  switch (inByte) {
    case 'r':    // red
      Serial.println("red");
      digitalWrite(LED_RED, HIGH);
      digitalWrite(LED_GRN, LOW);
      digitalWrite(LED_BLU, LOW);
      break;
    case 'g':    // green
      Serial.println("grn");
      digitalWrite(LED_RED, LOW);
      digitalWrite(LED_GRN, HIGH);
      digitalWrite(LED_BLU, LOW);
      break;
    case 'b':    // blue
      Serial.println("blu");
      digitalWrite(LED_RED, LOW);
      digitalWrite(LED_GRN, LOW);
      digitalWrite(LED_BLU, HIGH);
      break;
    case 'o':    // none
      Serial.println("off");
      digitalWrite(LED_RED, LOW);
      digitalWrite(LED_GRN, LOW);
      digitalWrite(LED_BLU, LOW);
      break;
    default:
      break;
  }
}

// the loop function runs over and over again forever
void loop() {
  
  if (Serial.available()) {
    char inByte = Serial.read();
    handleLedState(inByte);
  }

}
