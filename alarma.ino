#include <Keypad.h>

#define PIR_PIN     3   // PIR sensor
#define LED_PIN     2   // LED indicator
#define BUZZER_PIN  4   // Buzzer

// --- Keypad setup ---
const byte ROWS = 4;
const byte COLS = 3;

char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};

byte rowPins[ROWS] = {5, 6, 8, 9};
byte colPins[COLS] = {10, 11, 12};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// --- Password setup ---
const String password = "1984";
String input = "";

// --- Alarm state ---
bool alarmArmed = false;
bool motionDetected = false;
bool lastMotionState = false;

// ---------------------- SETUP ----------------------
void setup() {
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  digitalWrite(LED_PIN, LOW);
  noTone(BUZZER_PIN);
  Serial.println("System ready. Press '*' to ARM the alarm.");
}

// ---------------------- MAIN LOOP ----------------------
void loop() {
  handleKeypad();
  handlePIR();
}

// ---------------------- FUNCTIONS ----------------------

void handleKeypad() {
  char key = keypad.getKey();
  if (!key) return;

  Serial.print("Key pressed: ");
  Serial.println(key);

  if (key == '*') {
    alarmArmed = true;
    Serial.println("🔒 Alarm armed! PIR active.");
  }
  else if (key == '#') {
    Serial.println("Enter 4-digit password to disarm:");
    input = "";
  }
  else if (isDigit(key)) {
    input += key;
    Serial.print("Entered: ");
    Serial.println(input);

    if (input.length() == 4) {
      if (input == password) {
        alarmArmed = false;
        noTone(BUZZER_PIN);
        digitalWrite(LED_PIN, LOW);
        Serial.println("✅ Correct password. Alarm disarmed!");
      } else {
        Serial.println("❌ Wrong password!");
      }
      input = "";
    }
  }
}

void handlePIR() {
  int motion = digitalRead(PIR_PIN);

  if (!alarmArmed) {
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);
    motionDetected = false;
    return;
  }

  if (motion == HIGH && !lastMotionState) {
    // Motion just started
    motionDetected = true;
    Serial.println("⚠️ Motion detected!");
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 1000);

    // 🔸 Send update to Python/XAMPP only when triggered
    Serial.print("Alarm_status: ");
    Serial.print(alarmArmed ? "ON" : "OFF");
    Serial.print(" | PIR: ");
    Serial.println("MOTION");

  } else if (motion == LOW && lastMotionState) {
    // Motion just stopped
    motionDetected = false;
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);

    // Optional: send reset message
    Serial.print("Alarm_status: ");
    Serial.print(alarmArmed ? "ON" : "OFF");
    Serial.print(" | PIR: ");
    Serial.println("CLEAR");
  }

  lastMotionState = motion;
}
