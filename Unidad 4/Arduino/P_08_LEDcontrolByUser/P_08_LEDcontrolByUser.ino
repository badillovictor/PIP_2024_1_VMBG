int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(15);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    // --With Semi-Perfect Users
    // Any numeric value != 0 will turn on the LED
    // Any non.mumeric value will turn off the LED
    int v = Serial.readString().toInt();
    digitalWrite(led, v);

  }
}
