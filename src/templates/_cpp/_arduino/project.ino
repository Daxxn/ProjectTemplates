const int ledPin = LED_BUILTIN;

int state = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  Serial.println('Startup Complete...');
}

void loop()
{
  Serial.println('Main Loop');
  state = !state;
  digitalWrite(ledPin, state);
  delay(1000);
}
