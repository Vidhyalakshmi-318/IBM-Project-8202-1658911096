#include <Servo.h>
#define trigPin 9
#define echoPin 8
Servo servo;
int sound = 250;

void setup() {
Serial.begin (9600);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
servo.attach(6);
pinMode(13, OUTPUT);
pinMode(12, OUTPUT);
}
void loop() {
  
long duration, distance;
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1; if (distance < 80) {
Serial.print(distance);
Serial.println(" cm");
servo.write(0);
}
else if (distance<180) {
Serial.print(distance);
Serial.println(" cm");
  for(int i=0;i<180;i++)
  {
  servo.write(i);
  digitalWrite(13,HIGH);
  tone(12,30);
  delay(10);
  }
  servo.detach();
}
 
else if (distance>180){
  servo.attach(6);
  servo.write(0);
  digitalWrite(13,LOW);
  noTone(12);
 
}
delay(500);
}