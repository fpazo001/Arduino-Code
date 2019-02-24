#include <Servo.h>
Servo myservo;

const int pin = 11;
int CurrentPosition = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(pin, OUTPUT);
  myservo.attach(pin);
  Serial.setTimeout(100);
}

void loop()
{
  int newPosition;

  if (Serial.available()) 
  {
    newPosition = Serial.parseInt();

    if (newPosition < 0)
        return;

    if (newPosition > 180)
        return;
  
    for (; CurrentPosition < newPosition; CurrentPosition++)
    {
      myservo.write(CurrentPosition);
      delay(1);
    }
  
    for (; CurrentPosition > newPosition; CurrentPosition--)
    {
      myservo.write(CurrentPosition);
      delay(1);
    }
  }
}
