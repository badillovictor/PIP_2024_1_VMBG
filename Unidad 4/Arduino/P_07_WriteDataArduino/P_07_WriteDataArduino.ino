int v;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){ //Check Arudino's buffer
    //readString will read all the bytes it can until it timeouts
    //timeout length is 1 second by default
    v = Serial.readString().toInt();
    Serial.println(v);
  }
}
