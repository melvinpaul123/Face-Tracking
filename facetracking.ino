#include <Servo.h> 

Servo servox;
Servo servoy;

int pos;
int i;               // iterator
int t=90;    //variable to move to according angle
int u=90;
int q,a,v,f,z;

void setup() 
{   
  servox.attach(10); // Attach each Servo object to a digital pin (left right)
  servoy.attach(6); // Attach each Servo object to a digital pin (up down)
  Serial.begin(9600); // Open the serial connection, 9600 baud
  servox.write(t);
  servoy.write(u);
} 

void loop() 
{ 
  if (Serial.available() > 0) // Wait for serial input
  {
    pos = Serial.read();// Read the first byte
     
    // ----------X-axis--------------
          if (pos==49 || pos==1)//1=49
            {
              a=servox.read();
             if(a>60){
             for(v=a; v>=60; v--){
              servox.write(v);
              delay(15);
             }
             }
            }
         else if (pos==50)//2=50
           {
             a=servox.read();
             if(a<120){
             for(v=a; v<=120; v++){
              servox.write(v);
              delay(15);
             }
             }
           }  
           else if (pos==48)//0=48
          {
          z=servox.read();
            servox.write(z);
            delay(15);
          }
      // ----------Y-axis--------------
           else if (pos==51)//3=51
           {
             q=servoy.read();
             if(q>60){
             for(v=q; v>=60; v--){
              servoy.write(v);
              delay(15);
             }
             }
           }
           else if (pos==52)//4=52
           {
             q=servoy.read();
             if(q<120){
             for(v=q; v<=120; v++){
              servoy.write(v);
              delay(15);
             }
           } 
           } 
           else if (pos==53)//5=53
           {
            f=servoy.read();
             servoy.write(f);
             delay(15);
           } 
     Serial.flush();
    }
}
