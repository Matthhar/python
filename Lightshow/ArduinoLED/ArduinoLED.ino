void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0) {
    char value = Serial.read();
    Serial.print("You just sent me: ");
    Serial.write(value);
    Serial.print("\n");
    if (value == 1){
     digitalWrite(13, HIGH);
     delay(2000); 
    }
    if (value == 0){
     digitalWrite(13, LOW);
     delay(2000); 
    }
  }
 else
  {
    digitalWrite(13, LOW);
  }
}
