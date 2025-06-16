import json
import time
import requests
from kafka import KafkaProducer

KAFKA_BROKER = 'kafka:9092'
KAFKA_TOPIC = 'raw-data'
API_KEY = 'YOUR_API_KEY'
CITY = 'Valencia'
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_weather_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            return {
                'city': CITY,
                'timestamp': data['dt'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
    except:
        pass
    return None

def main():
    while True:
        data = get_weather_data()
        if data:
            producer.send(KAFKA_TOPIC, value=data)
            producer.flush()
        time.sleep(60)

if __name__ == '__main__':
    main()
