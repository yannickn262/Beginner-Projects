#include <Servo.h>
int x;
int finger;
int angle;
int initialvalue = 0;

int servoPinF1 = 11;
int servoPinF2 = 5;
int servoPinF3 = 10;
int servoPinF4 = 3;
int servoPinF5 = 12;

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;




void setup() {
  // put your setup code here, to run once:

  servo1.attach(servoPinF1);
  servo2.attach(servoPinF2);
  servo3.attach(servoPinF3);
  servo4.attach(servoPinF4);
  servo5.attach(servoPinF5);

  Serial.begin(9600);

  pinMode(servoPinF1, OUTPUT);
  pinMode(servoPinF2, OUTPUT);
  pinMode(servoPinF3, OUTPUT);
  pinMode(servoPinF4, OUTPUT);
  pinMode(servoPinF5, OUTPUT);

  Serial.setTimeout(4000);



}

void loop() {

  servo1.write(initialvalue);
  servo2.write(initialvalue);
  servo3.write(initialvalue);
  servo4.write(initialvalue);
  servo5.write(initialvalue);

  if (Serial.available() == 0)
  {

    Serial.println("Enter a number from 1 to 5 to choose which finger to move");
    Serial.println("Enter 6 if you want to flip someone off, and 7 if you want to be a surfer bro, 8 if you want to rock on/hook em'horns, and 9 if you want to die");
    Serial.println(); Serial.println(); Serial.println(); Serial.println();Serial.println(); Serial.println(); Serial.println();Serial.println(); Serial.println(); 
    finger = Serial.parseInt();
    Serial.println(finger);


    if (finger == 1)
    {
      Serial.println("Enter an angle from 0 to 360");
      angle = Serial.parseInt();
      Serial.print(angle);


      for (x = 0; x < angle; x++)

      {
        servo2.write(x);
        delay(5);

      }
      for (x = angle; x > 0; x--)
      {
        servo2.write(x);
        delay(5);
      }
    }
    else if (finger == 2)
    {
      Serial.println("Enter an angle from 0 to 360");
      angle = Serial.parseInt();
      Serial.print(angle);
      for (x = 0; x < angle; x++)

      {
        servo1.write(x);
        delay(5);

      }
      for (x = angle; x > 0; x--)
      {
        servo1.write(x);
        delay(5);
      }

    }
    else if (finger == 6)
    {
      Serial.println("Yandaddy");
      for (x = 0; x < 360; x++)
      {
        servo1.write(x);
        servo2.write(x);
        servo4.write(x);
        servo5.write(x);
        delay(1);
      }
      delay(2000);
      for (x = 360; x > 0; x--)
      {
        servo1.write(x);
        servo2.write(x);
        servo4.write(x);
        servo5.write(x);
        delay(2);
      }

    }
    else if (finger == 9)
    {
      
      for (x = 0; x < 360; x++)
      {
        servo5.write(x);
      }
      delay(20);
      for (x = 0; x < 360; x++)
      {
        servo4.write(x);
      }
      delay(20);
      for (x = 0; x < 360; x++)
      {
        servo3.write(x);

      }
      delay(20);

      for (x = 0; x < 360; x++)
      {
        servo1.write(x);
      }
      delay(20);

      for (x = 0; x < 360; x++)
      {
        servo2.write(x);
      }
      delay(1000);
      for (x = 360; x > 0; x--)
      {
        servo5.write(x);
        delay(2);
        servo4.write(x);
        delay(2);
        servo3.write(x);
        delay(2);
        servo2.write(x);
        delay(2);
        servo2.write(x);
        delay(2);

      }

    }
    else if (finger == 7)
    {
      for (x = 0; x < 360; x++)
      {
        servo4.write(x);
        servo3.write(x);
        servo1.write(x);
        delay(1);
      }
      delay(1000);
      for (x = 360; x > 0; x--)
      {
        servo4.write(x);
        servo3.write(x);
        servo1.write(x);
        delay(2);
      }
    }
else if (finger == 10)
    {
      for (x = 0; x < 360; x++)
      {
        servo5.write(x);
        servo4.write(x);
        servo3.write(x);
        servo2.write(x);
        delay(1);
      }
      for (x = 0; x < 360; x++)
      {
         servo1.write(x);  
      
      }

      for (x = 360; x > 0; x--)
      {
          servo1.write(x);
      }
      for (x = 0; x < 360; x++)
      {
         servo1.write(x);  
      
      }
      for (x = 360; x > 0; x--)
      {
          servo1.write(x);
      }
      for (x = 0; x < 360; x++)
      {
         servo1.write(x);  
      
      }
      for (x = 360; x > 0; x--)
      {
          servo1.write(x);
      }
       for (x = 360; x > 0; x--)
      {
          servo5.write(x);
          servo4.write(x);
          servo3.write(x);
          servo2.write(x);

      }

    }
    else if (finger == 3)
    {
      Serial.println("Enter an angle from 0 to 360");
      angle = Serial.parseInt();
      Serial.print(angle);
      for (x = 0; x < angle; x++)

      {
        servo3.write(x);
        delay(5);

      }
      for (x = angle; x > 0; x--)
      {
        servo3.write(x);
        delay(5);
      }

    }
    else if (finger == 8)
    {
      for (x = 0; x < 360; x++)

      {
        servo4.write(x);
        delay(2);
        servo3.write(x);

      }
      delay(2000);
      for (x = 360; x > 0; x--)
      {
        servo4.write(x);
        servo3.write(x);
        delay(1);
      }
    }
    else if (finger == 4)
    {
      Serial.println("Enter an angle from 0 to 360");
      angle = Serial.parseInt();
      Serial.print(angle);
      for (x = 0; x < angle; x++)

      {
        servo4.write(x);
        delay(5);

      }
      for (x = angle; x > 0; x--)
      {
        servo4.write(x);
        delay(5);
      }
    }

  }  else if (finger == 5)
  {
    Serial.println("Enter an angle from 0 to 360");
    angle = Serial.parseInt();
    Serial.print(angle);
    for (x = 0; x < angle; x++)

    {
      servo5.write(x);
      delay(5);

    }
    for (x = angle; x > 0; x--)
    {
      servo5.write(x);
      delay(5);
    }



  }



  else {}

}



