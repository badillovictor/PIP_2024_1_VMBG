int led[] = {
  4, 5, 6, 7, 8, 9, 10, 11
};
int ledStates[] = {
  false, false, false, false, false, false, false, false
};

void setup() {
  // put your setup code here, to run once:
  pinMode(led[0], OUTPUT);
  pinMode(led[1], OUTPUT);
  pinMode(led[2], OUTPUT);
  pinMode(led[3], OUTPUT);
  pinMode(led[4], OUTPUT);
  pinMode(led[5], OUTPUT);
  pinMode(led[6], OUTPUT);
  pinMode(led[7], OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(15);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int ledIndex = Serial.readString().toInt() - 1;
    ledStates[ledIndex] = !ledStates[ledIndex];
    digitalWrite(led[ledIndex], ledStates[ledIndex]);
  }
  delay(200);
}