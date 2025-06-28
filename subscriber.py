from google.cloud import pubsub_v1
import json
import pymysql

DB_HOST = 'your-sql-public-ip'
DB_USER = 'root'
DB_PASS = 'your-password'
DB_NAME = 'feedback_system'

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path("your-project-id", "feedback-sub")

def connect_db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)

def callback(message):
    data = eval(message.data.decode('utf-8'))  # better to use json.loads in real apps
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)",
                (data['name'], data['email'], data['feedback']))
    conn.commit()
    conn.close()
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)
print("Listening for messages...")
import time
while True:
    time.sleep(60)
