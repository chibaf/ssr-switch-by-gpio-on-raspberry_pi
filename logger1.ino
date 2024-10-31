void setup() {
  // initialize serial comms
  Serial.begin(19200);
  pinMode(LED_BUILTIN, OUTPUT);
}

//// print signals
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println(random(-2,2));
  delay(50);
  digitalWrite(LED_BUILTIN, LOW);
  delay(450);
}