int IRSensor = 2;
int led =13;
int buzzer=3;
void setup()
{
  pinMode (IRSensor, INPUT);
  pinMode (led, OUTPUT);
  pinMode (buzzer,OUTPUT);
}

void loop()
{
  digitalWrite (led,HIGH);
  digitalWrite (buzzer,HIGH);
  Serial.begin ("led,ON");
}
else
{
  digitalWrite (led,LOW);
  digitalWrite (buzzer,LOW);
  Serial.print IN ("led,OFF");
  delay  (5000);
}
