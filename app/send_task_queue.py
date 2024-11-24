import json
from faststream.rabbit import RabbitBroker, RabbitMessage
from config import RABBITMQ_HOST

broker = RabbitBroker(RABBITMQ_HOST)

async def send_to_result_queue(translated_text):
    message = {"translated_text": translated_text}
    await broker.publish(
        json.dumps(message),
        queue="translation_result"
    )
    print(f"Sent translated text to result queue: {translated_text}")
