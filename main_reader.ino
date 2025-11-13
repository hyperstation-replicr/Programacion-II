#include <TM1637Display.h>

#define LDR_PIN A0      // LDR sensor on analog pin A0
#define TEMP_PIN A1     // LM35 temperature sensor on analog pin A1
#define LED_PIN 3       // LED on PWM pin 3
#define FAN_PIN 9       // Fan control via NPN transistor (base resistor ~1k)

// TM1637 pins
#define CLK 7           // Clock pin
#define DIO 6           // Data pin

TM1637Display display(CLK, DIO);

float smoothBrightness = 0;  
unsigned long previousMillis = 0;
unsigned long secondsElapsed = 0;

// --- Manual clock start time (24h format) ---
int startHour = 20;   // <-- CHANGE THIS to your current hour (e.g., 6:00 PM = 18)
int startMinute = 50; // <-- CHANGE THIS to your current minute

void setup() {
  Serial.begin(9600);
  pinMode(LDR_PIN, INPUT);
  pinMode(TEMP_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);

  display.setBrightness(7);
  display.showNumberDecEx(0, 0b01000000, true);

  // Convert start time to total seconds
  secondsElapsed = startHour * 3600UL + startMinute * 60UL;
}

void loop() {
  // --- LDR section ---
  int ldrValue = analogRead(LDR_PIN);
  float normalized = (800.0 - ldrValue) / 500.0;
  normalized = constrain(normalized, 0, 1);
  int targetBrightness = int(255.0 * normalized * normalized);
  smoothBrightness = 0.9 * smoothBrightness + 0.1 * targetBrightness;
  analogWrite(LED_PIN, int(smoothBrightness));

  // --- LM35 Temperature section ---
  int tempValue = analogRead(TEMP_PIN);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperatureC = voltage * 100.0;

  // --- Fan always ON ---
  int fanSpeed = 255;
  analogWrite(FAN_PIN, fanSpeed);

  // --- Clock update ---
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= 1000) {
    previousMillis = currentMillis;
    secondsElapsed++;

    int hours = (secondsElapsed / 3600) % 24;
    int minutes = (secondsElapsed / 60) % 60;

    int displayTime = hours * 100 + minutes;
    display.showNumberDecEx(displayTime, 0b01000000, true); // HH:MM
  }

  // --- Serial Output ---
  Serial.print("LDR: ");
  Serial.print(ldrValue);
  Serial.print(" | Temp (C): ");
  Serial.print(temperatureC, 1);
  Serial.print(" | Fan PWM: ");
  Serial.println(fanSpeed);

  delay(100);
}
