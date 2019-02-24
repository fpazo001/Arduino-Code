int distancecal;
int movement;
int x;             //Replace with Servo Code
int y;             //Replace with Servo Code
String serialData;



void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(10);

}


void loop()
{
  Distance();
  PIR();
  
}

void Distance() {

  distancecal = 3000;
  Serial.print(distancecal);
  Serial.print(" , ");
  return distancecal;

}


void PIR() {


  movement = 2000;
  Serial.print(movement);
  Serial.print(" , ");
  return movement;

}



