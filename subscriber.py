# -----------------------------------
# Minimal MQTT Subscriber for Smart Grid
# -----------------------------------
import json
import paho.mqtt.client as mqtt
import psycopg2

# -----------------------------
# PostgreSQL Configuration
# -----------------------------
DB_HOST = "localhost"
DB_PORT = 5433          # your custom port
DB_NAME = "smart_grid"
DB_USER = "postgres"
DB_PASSWORD = "root"    # make sure this is correct

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL")
except Exception as e:
    print(f"❌ PostgreSQL connection failed: {e}")
    exit(1)

# -----------------------------------
# MQTT Configuration
# -----------------------------------
BROKER = "localhost"
PORT = 1883
TOPIC = "energy/meters/#"

# -----------------------------------
# MQTT Callbacks
# -----------------------------------
def on_connect(client, userdata, flags, reasonCode, properties=None):
    if reasonCode == 0:
        print("✅ Connected to MQTT Broker")
        client.subscribe(TOPIC)
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"❌ MQTT connection failed with code {reasonCode}")

def on_message(client, userdata, msg):
    print(f"\n📩 Received message on {msg.topic}")
    payload_raw = msg.payload.decode()
    print(f"Raw payload: {payload_raw}")

    try:
        payload = json.loads(payload_raw)
        print("Parsed payload:", payload)

        # Extract fields
        meter_id = payload.get("meter_id")
        timestamp = payload.get("timestamp")
        power = payload.get("power")
        voltage = payload.get("voltage")
        current = payload.get("current")
        frequency = payload.get("frequency")
        energy = payload.get("energy")

        # Insert into database
        insert_query = """
        INSERT INTO energy_readings (meter_id, "timestamp", power, voltage, current, frequency, energy)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (meter_id, timestamp, power, voltage, current, frequency, energy))
        conn.commit()
        print(f"✅ Inserted data for meter {meter_id} at {timestamp}")

    except Exception as e:
        print(f"❌ Error processing message: {e}")

# -----------------------------------
# MQTT Client Setup
# -----------------------------------
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER, PORT, 60)
except Exception as e:
    print(f"❌ Failed to connect to MQTT Broker: {e}")
    exit(1)

print("📡 Starting MQTT Subscriber...")
client.loop_forever()
