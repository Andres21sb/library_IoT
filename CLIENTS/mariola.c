// Proyecto Mariola  
  // Pedro Leiva
  // Creado: 10 octubre 2023

// Librerias conexion Wifi - cliente ESp8266
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFiMulti.h>
#include <Adafruit_LTR390.h>
#include <WiFiClient.h>
#include <String>
#include <DHT.h>
#include <MQ135.h>

WiFiClient  Client;
Adafruit_LTR390 sensor_luminucidad = Adafruit_LTR390();
// defino credenciales red
const char* ssid ="Ap_54088";    
const char* password ="fmcampos";           
bool red1 = true;

// Definicion de Variables para la base de datos
float tb, hb, tc, hc,ta,ha,tv,hv,tr,hr,ca,ne,le,uv = 0;
int i;

//=================== setting=====================================
 
 const char idlog='9';  // corresponde al id de la corrida o tipo de test
 String description="1ra. prueba en sitio Llano Bonito"; 
 float ciclo=300000;    // 5 minutos


#define LEPIN16 16  //LE DEL ESP8266
#define DHTPIN1 13  //d7 sensor_referencia
#define DHTPIN2 14  //d5 sensor_alzamiel
#define DHTPIN3 2   //d4 sensor_camara
#define DHTPIN4 0   //d3 sensor_basurero
#define DHTPIN5 12  //d6 sensor_vacio
#define SW520 15    //d8 // sensor inclinacion
#define ANALOGPIN A0  
#define DHTTYPE DHT22


 
     
DHT sensor_referencia(DHTPIN1, DHTTYPE,22);  
DHT   sensor_alzamiel(DHTPIN2, DHTTYPE,22);
DHT     sensor_camara(DHTPIN3, DHTTYPE,22);
DHT   sensor_basurero(DHTPIN4, DHTTYPE,22);
DHT      sensor_vacio(DHTPIN5, DHTTYPE,22);
MQ135 sensor_calidadaire = MQ135(A0);
float ciclo_back = ciclo;

void setup() {
   
  
  Serial.begin(115200); 
  Serial.println(F("prueba de conexión con el servidor"));
  pinMode(LEPIN16, OUTPUT);     //control flujo sensores
  sensor_referencia.begin();  
  sensor_alzamiel.begin();
  sensor_camara.begin();
  sensor_basurero.begin();
  sensor_vacio.begin();  
   
  sensor_luminucidad.begin();
 
 // pinMODE (SW520, INPUT);  // sensor inclinacion
     


  sensor_luminucidad.setMode(LTR390_MODE_UVS);
  if (sensor_luminucidad.getMode() == LTR390_MODE_ALS) {
    Serial.println("In ALS mode");
  } else {
    Serial.println("In UVS mode");
  }
  sensor_luminucidad.setGain(LTR390_GAIN_3);
  Serial.print("Gain : ");
  Serial.println(3);
  sensor_luminucidad.setThresholds(100, 1000);
  sensor_luminucidad.configInterrupt(true, LTR390_MODE_UVS);
  // ====== ltr390==========
 
 
  WiFi.begin(ssid, password);
  Serial.print("Conectando...");
  while (WiFi.status()!= WL_CONNECTED) {
   // if (red1) { ssid ="basement"; red1=false;
   // }
   // else { ssid ="aglaia"; red1=true;  }
    delay(200);
    Serial.print("."); 
  }
  Serial.println("Conexión OK!"); 
  SenalNormal(); // aviso trabaja normal
  Serial.print("IP Local: ");
  Serial.println(WiFi.localIP());

  EnvioLog(); // funcion  de envio log por post
}
void loop() {
  
  digitalWrite(LEPIN16, HIGH);
  LecturaTH(); // funcion  de envio datos por post
  EnvioDatos();
  
           Serial.println("valor ciclo");
           Serial.println(ciclo);
           
           Serial.println("valor ciclo_back");
           Serial.println(ciclo_back);
  delay(ciclo);  
}


// funcion de lectura de temperatura y humedad
void LecturaTH(){

  SenalNormal(); // aviso trabaja normal
  tr = sensor_referencia.readTemperature() * 0.9995+0.0059;    
  ta = sensor_alzamiel.readTemperature()*0.7794+6.2157;
  tc = sensor_camara.readTemperature()*0.7829+6.0776;  
  tb = sensor_basurero.readTemperature()*0.6388+9.2657;  
  tv = sensor_vacio.readTemperature()*0.7305+7.207;      
   
  hr = sensor_referencia.readHumidity()*0.2561+58;  
  ha = sensor_alzamiel.readHumidity()*0.2473+58.115;  
  hc = sensor_camara.readHumidity()*0.2775+56.258;  
  hb = sensor_basurero.readHumidity()*0.24+57.899;  
  hv = sensor_vacio.readHumidity()*0.2977+52.581;  

  ca = sensor_calidadaire.getPPM();
 
   ne = 1; //digital.read(SW520);
   le = 0;   //ALS luminucidad
   uv = 0;  
   
       
      //sensor_luminucidad.configInterrupt(true, LTR390_MODE_UVS);
      sensor_luminucidad.setMode(LTR390_MODE_UVS);
      uv = sensor_luminucidad.readUVS();
      Serial.println("uv:");
      Serial.println(uv);
      delay(1000); 
      sensor_luminucidad.setMode(LTR390_MODE_ALS);
      le = sensor_luminucidad.readALS();
      Serial.println("le:");
      Serial.println(le);
     
   // verifica si los valores de UV y LE son demaciado altos entonces entonces guarda un cero pero la lectura se almacena en DB
  if (uv>42949)  {
     SenalError();  // aviso señal de error
     le = 0;  
     uv = 0;  
  }
 
  // Check if any reads failed and exit early (to try again).
  if (isnan(hb) || isnan(tb)) {
    Serial.println(F("Failed to read from DHT sensor!")); 
    SenalError();  // aviso señal de error
    delay(1000); 
      
    return;
  }
}



// rutina de envio de datos log
void EnvioLog(){


  SenalNormal(); // aviso trabaja normal
  if (WiFi.status() == WL_CONNECTED){
     HTTPClient http;  // creo el objeto http
     String datos_a_enviar = "&idlog=" + String(idlog) + "&description=" + String(description);

    ciclo = ciclo_back;
    Serial.println("========= igualo ciclo============");
    http.begin(Client,"http://mariola2023.000webhostapp.com/LogPost.php");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded"); // defino texto plano..
    Serial.println(datos_a_enviar);
     int codigo_respuesta = http.POST(datos_a_enviar);

     if (codigo_respuesta>0){
      Serial.println("1-Código HTTP: "+ String(codigo_respuesta));
        if (codigo_respuesta == 200){
          String cuerpo_respuesta = http.getString();
          Serial.println("2-El servidor respondió exitosamente recibiendo Log: ");
          Serial.println(cuerpo_respuesta);
           ciclo = ciclo_back;
             Serial.println("========= recupero ciclo dentro============");
        }
     } else {
        Serial.print("3-Error enviado POST, código: ");
        SenalError();  // aviso señal de error 
        ciclo = 100 ; // cambia el ciclo a medio minuto para que intente de nuevo rapidamente y luego retomar el ciclo al tiempo seteado
        Serial.println(datos_a_enviar);
     }
       http.end();  // libero recursos
       
  } else {
     Serial.println("4-Error en la conexion WIFI");
     SenalError();     // aviso señal de error 
     ciclo = 100 ; // cambia el ciclo a medio minuto para que intente de nuevo rapidamente y luego retomar el ciclo al tiempo seteado
  }
}

 

// rutina de envio de datos por POST DATOS
void EnvioDatos(){
  SenalNormal(); // aviso trabaja normal
  if (WiFi.status() == WL_CONNECTED){
     HTTPClient http;  // creo el objeto http
     String datos_a_enviar = "&idlog=" + String(idlog) +
                              "&tr=" + String(tr) +
                              "&ta=" + String(ta) +
                              "&tc=" + String(tc) +
                              "&tb=" + String(tb) +
                              "&tv=" + String(tv) +  
                              "&hr=" + String(hr) +
                              "&ha=" + String(ha) +  
                              "&hc=" + String(hc) +
                              "&hb=" + String(hb) +  
                              "&hv=" + String(hv) +
                               
                             "&ca=" + String(ca) + "&ne=" + String(1) +  
                             "&le=" + String(le) + "&uv=" + String(uv);

    http.begin(Client,"http://mariola2023.000webhostapp.com/EspPost.php");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded"); // defino texto plano..
    Serial.println(datos_a_enviar);
     int codigo_respuesta = http.POST(datos_a_enviar);

     if (codigo_respuesta>0){
      Serial.println("1-Código HTTP: "+ String(codigo_respuesta));
        if (codigo_respuesta == 200){
          String cuerpo_respuesta = http.getString();
          Serial.println("2-El servidor respondió exitosamente recibiendo datos: ");   
          Serial.println(cuerpo_respuesta);
          ciclo = ciclo_back;
          Serial.println("========= recupero ciclo dentro============");
        }
     } else {
        Serial.print("3-Error enviado POST, código: ");
        Serial.println(datos_a_enviar);
        SenalError();  // aviso señal de error 
        ciclo = 100 ; // cambia el ciclo a medio minuto para que intente de nuevo rapidamente y luego retomar el ciclo al tiempo seteado
     }
       http.end();  // libero recursos
       
  } else {
     Serial.println("4-Error en la conexion WIFI");
     SenalError();  // aviso señal de error 
     ciclo = 100 ; // cambia el ciclo a medio minuto para que intente de nuevo rapidamente y luego retomar el ciclo al tiempo seteado
  }
}
  
// rutina LED CICLO NORMAL
void SenalNormal(){
  for (int i = 0; i < 3; i++) {
    digitalWrite(LEPIN16, HIGH);
    delay(400); 
    digitalWrite(LEPIN16, LOW);
    delay(900);  
  }
  digitalWrite(LEPIN16, LOW);
}
// rutina LED CICLO ERROR
void SenalError(){
  for (int i = 0; i < 15; i++) {
    digitalWrite(LEPIN16, HIGH);
    delay(100); 
    digitalWrite(LEPIN16, LOW);
    delay(400);  
  }
}