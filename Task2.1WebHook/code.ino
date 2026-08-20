#include "DHT.h"
#include <BH1750.h>
#include <Wire.h>
#include <WiFiNINA.h>
#include "secrets.h"
#include "ThingSpeak.h" /


int keyIndex = 0;           
unsigned long myChannelNumber = SECRET_CH_ID;
const char * myWriteAPIKey = SECRET_WRITE_APIKEY;

WiFiClient client;
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
BH1750 lightMeter;

float temperature;
float humidity;
float light_level;

void setup() {
  Serial.begin(115200);      // Initialize serial 
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo native USB port only
  }
 dht.begin();
 wifi_connection();
  ThingSpeak.begin(client); 
  light_sensor_setting();
 }

void wifi_connection()
{
  // Connect or reconnect to WiFi
  if(WiFi.status() != WL_CONNECTED){
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(SECRET_SSID);

    while(WiFi.status() != WL_CONNECTED){
     WiFi.begin(SECRET_SSID, SECRET_PASS); // Connect to WPA/WPA2 network. Change this line if using open or WEP network
      Serial.print(".");
      delay(5000);     
    } 
    Serial.println("\nConnected.");
  }
}

void temperature_reading()
{
  // Read humidity
  humidity = dht.readHumidity();

  // Read temperature in Celsius
  temperature = dht.readTemperature();

  // Check if the readings failed
  if (isnan(humidity) || isnan(temperature))
  {
    Serial.println("Failed to read from DHT22 sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%  Temperature: ");
  Serial.print(temperature);
  Serial.println("°C");
}

void light_sensor_setting()
{
  // Initialize the I2C bus
  Wire.begin();

  // Initialize BH1750
  lightMeter.begin();

  Serial.println("BH1750 Test begin");
}

void light_readings()
{
  // Read light level in lux
  light_level = lightMeter.readLightLevel();

  Serial.print("Light: ");
  Serial.print(light_level);
  Serial.println(" lx");
}
void send_to_thingspeak()
{
  // Set temperature in Field 1
  ThingSpeak.setField(1, temperature);

  // Set light level in Field 2
  ThingSpeak.setField(3, light_level);

  ThingSpeak.setField(2, humidity);

  // Send the data to ThingSpeak
  int response = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);

  if (response == 200)
  {
    Serial.println("Channel update successful.");
  }
  else
  {
    Serial.print("Problem updating channel. HTTP error code: ");
    Serial.println(response);
  }
}

void loop()
{
  wifi_connection();
  temperature_reading();
  light_readings();
  send_to_thingspeak();

  delay(30000);
}
