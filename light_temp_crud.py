import serial
import mysql.connector
import time

# --- MySQL setup ---
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "arduino_sensors"
BAUD_RATE = 9600
PORT = "COM4"  # Your light + temp Arduino

# --- Connect to DB ---
db = mysql.connector.connect(
    host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, database=DB_NAME
)
cursor = db.cursor()

# --- Connect to Arduino ---
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
print(f"Connected to {PORT} for Light/Temp readings")

last_insert_time = 0

def insert_data(ldr, temp):
    sql = "INSERT INTO light_temp_data (device, ldr, temperature) VALUES (%s, %s, %s)"
    cursor.execute(sql, ("light_temp", ldr, temp))
    db.commit()
    print(f"Inserted → LDR: {ldr} | Temp: {temp} °C")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode(errors="ignore").strip()
            if line.startswith("LDR:"):
                print(line)
                try:
                    parts = line.split("|")
                    ldr = int(parts[0].split(":")[1].strip())
                    temp = float(parts[1].split(":")[1].strip())

                    # --- Only insert every 60 seconds ---
                    current_time = time.time()
                    if current_time - last_insert_time >= 60:
                        insert_data(ldr, temp)
                        last_insert_time = current_time

                except Exception as e:
                    print("Parse error:", e)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nStopping reader...")
finally:
    ser.close()
    cursor.close()
    db.close()
