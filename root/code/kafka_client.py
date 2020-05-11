import json
import sys
import time

from random import randint
from kafka import KafkaConsumer, KafkaProducer

BROKERS = '192.168.2.105:32775,192.168.2.105:32776'

producer = KafkaProducer(bootstrap_servers=BROKERS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
TOPIC_1 = 'test_topic_native_1'
TOPIC_2 = 'test_topic_native_2'


def write_message(topic, key, value):
    producer.send(topic, key=key, value=value)


def run_producer_topic_1():
    print('Starting producer topic 1')
    while True:
        for i in range(2000):
            random_number_1 = randint(0, 4)
            random_number_2 = randint(0, 10)
            # print(f'run_producer_topic_1: {random_number_1} {random_number_2}', flush=True)
            write_message(TOPIC_1, key=bytes([random_number_1]), value={'blah': random_number_2})
        time.sleep(1)


def run_consumer_topic_1():
    print('Starting consumer topic 1', flush=True)
    consumer = KafkaConsumer(TOPIC_1, group_id='1', bootstrap_servers=BROKERS)
    for msg in consumer:
        print(f'Topic: {msg.topic} Partition: {msg.partition} Key: {msg.key} Value: {msg.value}', flush=True)
        value = json.loads(msg.value.decode('utf-8'))
        random_number_2 = value['blah']
        write_message(TOPIC_2, key=bytes([random_number_2]), value='blah')

    print('Exiting consumer topic 1', flush=True)


def run_consumer_topic_2():
    print('Starting consumer topic 2', flush=True)
    consumer = KafkaConsumer(TOPIC_2, group_id='1', bootstrap_servers=BROKERS)
    for msg in consumer:
        print(f'Topic: {msg.topic} Partition: {msg.partition} Key: {msg.key} Value: {msg.value}', flush=True)

    print('Exiting consumer topic 2', flush=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python kafka_client.py <argument>')
        sys.exit(-1)

    argument = sys.argv[1]
    if argument == 'producer_topic_1':
        run_producer_topic_1()
    elif argument == 'consumer_topic_1':
        run_consumer_topic_1()
    elif argument == 'consumer_topic_2':
        run_consumer_topic_2()
