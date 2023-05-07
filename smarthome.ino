String reading;
void setup( ) {
pinMode(6, OUTPUT);
pinMode(5, OUTPUT);
pinMode(4, OUTPUT);
Serial.begin(9600);
}
void loop( ) {
if(Serial.available()>0) {
reading=Serial.readStringUntil('\n'); // readString();

if (reading=="Lamp on")
{digitalWrite(6,HIGH);}
else if (reading=="Lamp off")
{digitalWrite(6,LOW);}

else if (reading=="Fan on")
{digitalWrite(5,HIGH);}
else if (reading=="Fan off")
{digitalWrite(5,LOW); }

else if (reading=="LED on")
{digitalWrite(4,HIGH);}
else if (reading=="LED off")
{digitalWrite(4,LOW);}

}}
