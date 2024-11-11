import pika
import json
from app.config import RABBITMQ_HOST

def send_to_result_queue(translated_text):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue="translation_result")

    message = {"translated_text": translated_text}
    channel.basic_publish(
        exchange="",
        routing_key="translation_result",
        body=json.dumps(message)
    )

    print(f"Sent translated text to result queue: {translated_text}")

    connection.close()
