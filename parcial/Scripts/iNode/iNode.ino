#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <Servo.h>


// comando para correr el nodo de arduino en la terminal
// rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600
// comando para dar permisos a arduino
// sudo chmod 777 /dev/ttyACM0

int Entero =0;
float Flotante =0.0;
bool Booleano =false;
String str ="";
char msg[30];
int velocidad=0;

Servo myservo;

ros::NodeHandle arduinoNode; // Inicializar Handler de la librería para nodo de Arduino
std_msgs::String ROString; // Importar variable String de ROS
ros::Publisher pub_String( "String_Ard", &ROString); // Define el topic que Arduino va a publicar (String Ard) a través del objeto arduControl
                        // String_Ard es el topic, la variable a publcar es ROString

// Definir callback suscrito al topic H_int
void callback(const std_msgs::Int16& recibido)
{
 velocidad = map(recibido.data, 0, 100, 0, 180);          //*(255.0/100.0);
  //myservo.write(180);  
 //analogWrite(9, velocidad);
 
}

ros::Subscriber<std_msgs::Int16> sub("Int_H", callback);   //Definir suscriptor al topic H_int mediante la función callback

void setup() {
  myservo.attach(9);
  //pinMode(9, OUTPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  arduinoNode.initNode(); // Inicializar el nodo en Arduino
  arduinoNode.advertise(pub_String);
  arduinoNode.subscribe(sub);
  //randomSeed(analogRead(0));
}

void loop() {

  // Leer valores de los puertos físicos
  Entero = map(analogRead(A4), 0, 1023, 0, 255);
  Flotante = (float)map(analogRead(A3), 0, 1023, 0, 500)*1/100.0;
  Booleano = digitalRead(A5);


  // Enviar los valores a ROS
  //
  myservo.write(180);
  str =  "Bool=" + (String)Booleano + "/Int=" + (String)Entero + "/Float=" + (String)Flotante;
  str.toCharArray(msg,30);
  ROString.data =  msg;
  pub_String.publish(&ROString);
  arduinoNode.spinOnce();
  delay(100);
}
