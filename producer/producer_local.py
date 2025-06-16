import json
import time
from kafka import KafkaProducer

KAFKA_BROKER = 'kafka:9092'
KAFKA_TOPIC = 'raw-data'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sample_data = {
    "city": "Valencia",
    "timestamp": 1718123400,
    "temperature": 18.7,
    "humidity": 55,
    "wind_speed": 4.1
}

def main():
    while True:
        producer.send(KAFKA_TOPIC, value=sample_data)
        producer.flush()
        print("Sent message to Kafka")
        time.sleep(5)

if __name__ == '__main__':
    main()
