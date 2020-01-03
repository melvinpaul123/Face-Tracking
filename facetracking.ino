#include <Servo.h> 

Servo servo;
Servo servoy;

int pos;             // servo angle 0-180
int i;               // iterator
int t=90;    //variable to move to according angle
int u=90;
int q;
int a;
int v;
int f, z;
// Common servo setup values
int mini_Pul = 600;   // minimum servo position, us (microseconds)
int maxi_Pul = 2400;  // maximum servo position, us



void setup() 
{   
  servo.attach(10, mini_Pul, maxi_Pul); // Attach each Servo object to digital pin 10 (left right)
  servoy.attach(6, mini_Pul, maxi_Pul); // Attach each Servo object to digital pin 6 (up down)
  Serial.begin(9600); // Open the serial connection, 9600 baud
  servoy.write(u);
  servo.write(t);
} 



void loop() 
{ 
  if (Serial.available() > 0) // Wait for serial input (min 3 bytes in buffer)
    {         
      pos = Serial.read();// Read the first byte
     
    // ----------X-axis--------------
          if (pos==49 || pos==1)//1=49
            {
              a=servo.read();
             if(a>60){
             for(v=a; v>=60; v--){
              servo.write(v);
              delay(15);
             }
             }
            }
         else if (pos==50)//2=50
           {
             a=servo.read();
             if(a<120){
             for(v=a; v<=120; v++){
              servo.write(v);
              delay(15);
             }
             }
           }  
           else if (pos==48)//0=48
          {
          z=servo.read();
            servo.write(z);
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
//             if(q<40){
//             for(v=q; v<=40; v++){
//              servoy.write(v);
//              delay(15);
//             }
//           } 
           }
           else if (pos==52)//4=52
           {
             q=servoy.read();
//             if(q>120){
//             for(v=q; v>=120; v--){
//              myservo.write(v);
//              delay(15);
//             }
//             }
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
//        }
    }
}
