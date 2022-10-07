#include <ESP8266WiFi.h>

#include <ESP8266WebServer.h>

ESP8266WebServer server(80);

int Readpin=A0;
int wlevelpin=A1; //check  the pin numberon the board and change this
int Writepin=D0;

void setup() {

pinMode(Readpin,INPUT);
pinMode(wlevelpin,INPUT);
pinMode( Writepin,OUTPUT);
Serial.begin(115200);

WiFi.begin("My_wifi", "adnanadnan");  //Connect to the WiFi networks

while (WiFi.status() != WL_CONNECTED) {  //Wait for connection

delay(500);

Serial.println("Waiting to connect…");

}

Serial.print("IP address: ");

Serial.println(WiFi.localIP());                         //Print the local IP of the webserver

server.on("/Python", handlePath);              //Associate the handler function to the path

server.begin();                                                   //Start the server

Serial.println("Server listening");

}

void loop() {

server.handleClient(); //Handling of incoming requests

}


int callerValue(){
  int sVal=0;
  int temp = analogRead(A0);
  Serial.print("Actual Sensor Value: ");
  Serial.println(temp);
  sVal=map(temp, 0, 1023, 0, 100);
  Serial.print("Mapped Sensor Value: ");
  Serial.println(sVal);
  return sVal;
}
int callerValue1(){
  int wlevel=0;
  int wlevel = analogRead(A1);
  Serial.print("Water level sensor value: ");
  Serial.println(wlevel);
  return wlevel;

}
void handlePath() { 

int a;
//Handler for the path
int ca=callerValue();
int ca1=callerValue1();
String thisString=String(ca);
String thisString1=String(ca1);

server.send(200, "int", thisString);
server.send(300, "int",
  if (server.args() > 0 ) { // Arguments were received
    for ( uint8_t i = 0; i < server.args(); i++ ) {
      Serial.print("Input received was: ");
      Serial.println(server.arg(i)); // Display the argument
      a = server.arg(i).toInt();
      a*=0.0592*1000;
      boolean flag=true;
      while(flag){
        digitalWrite(Writepin,HIGH);
        delay(a+200);
        flag=false;
        
      }
      digitalWrite(Writepin,LOW);
      
      
      Serial.println(a);

      
//      String Str1[1] = {server.arg(i)};
     
//      Argument_Name = server.argName(i);
//      if (server.argName(i) == "user_input") {
//        Serial.print(" Input received was: ");
//        Serial.println(server.arg(i));
//        Clients_Response = server.arg(i);
// Serial.println(Clients_Response);}



      }


       

      
      
      }}
