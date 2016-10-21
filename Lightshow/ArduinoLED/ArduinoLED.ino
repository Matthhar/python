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
    if (value == "ON"){
     digitalWrite(13, HIGH);
     delay(1000); 
    }
    if (value == "OFF"){
     digitalWrite(13, LOW);
     delay(1000); 
    }
  }
  else
  {
    digitalWrite(13, LOW);
  }
}
