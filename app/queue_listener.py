import pika
import json
from app.services.translation_service import TranslationService
from app.config import RABBITMQ_HOST, TRANSLATION_QUEUE
from app.send_task_queue import send_to_result_queue

translation_service = TranslationService()

def process_translation_request(ch, method, properties, body):
    try:
        message = json.loads(body)
        text_to_translate = message.get("text", "")

        if text_to_translate:
            translated_text = translation_service.translate_text(text_to_translate)
            print(f"Translated text: {translated_text}")

            send_to_result_queue(translated_text)
            
        else:
            print("Received an empty message or invalid format.")

    except Exception as e:
        print(f"Error processing translation request: {e}")
    
    ch.basic_ack(delivery_tag=method.delivery_tag)

def listen_for_translations():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=TRANSLATION_QUEUE)

    channel.basic_consume(queue=TRANSLATION_QUEUE, on_message_callback=process_translation_request)

    print('Waiting for translation tasks...')
    channel.start_consuming()

if __name__ == "__main__":
    listen_for_translations()
