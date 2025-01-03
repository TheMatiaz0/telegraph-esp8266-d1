const int interruptPin = 14;  // GPIO14 (D14)
char prev = 'b';
bool buttonPressed = false;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 5;

void setup() {
  pinMode(interruptPin, INPUT_PULLUP);
  Serial.begin(921600);
}

void loop() {
  bool currentState = digitalRead(interruptPin);
  unsigned long currentTime = millis();

  if (currentState != buttonPressed) {
    lastDebounceTime = currentTime;
  }

  if ((currentTime - lastDebounceTime) > debounceDelay) {
    if (currentState == LOW && prev != 'a') {
      Serial.println('a');
      prev = 'a';
      buttonPressed = true;
    } else if (currentState == HIGH && prev != 'b') {
      Serial.println('b');
      prev = 'b';
      buttonPressed = false;
    }
  }
}