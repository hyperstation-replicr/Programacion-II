import serial
import mysql.connector
import time

# --- MySQL setup ---
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "arduino_sensors"
BAUD_RATE = 9600
PORT = "COM5"  # Your alarm Arduino

# --- Connect to MySQL ---
db = mysql.connector.connect(
    host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, database=DB_NAME
)
cursor = db.cursor()

# --- Connect to Arduino ---
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
print(f"Connected to {PORT} for Alarm readings")

def insert_data(alarm_status, pir_state):
    sql = "INSERT INTO alarm_data (device, alarm_status, pir_state) VALUES (%s, %s, %s)"
    cursor.execute(sql, ("alarm", alarm_status, pir_state))
    db.commit()
    print(f"Inserted → Alarm: {alarm_status} | PIR: {pir_state}")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode(errors="ignore").strip()
            if line:
                print(line)

                # Example line: "Alarm_status: ON | PIR: MOTION"
                if "Alarm_status" in line and "PIR" in line:
                    try:
                        parts = line.split("|")
                        alarm_status = parts[0].split(":")[1].strip()
                        pir_state = parts[1].split(":")[1].strip()

                        # Insert immediately when triggered
                        if pir_state == "MOTION":
                            insert_data(alarm_status, pir_state)
                    except Exception as e:
                        print("Parsing error:", e)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nStopping alarm reader...")
finally:
    ser.close()
    cursor.close()
    db.close()
