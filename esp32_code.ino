#include <WiFi.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* host = "server_ip";
const int port = 5000;

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }
    Serial.println("Connected to WiFi");
}

void loop() {
    // Capture audio and send to server
}
