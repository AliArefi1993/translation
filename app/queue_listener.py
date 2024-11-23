from faststream.rabbit import RabbitBroker, RabbitMessage
from faststream import FastStream
from services.translation_service import TranslationService
from config import RABBITMQ_HOST, TRANSLATION_QUEUE
from send_task_queue import send_to_result_queue

broker = RabbitBroker("amqp://guest:guest@RABBITMQ_HOST/")
app = FastStream(broker)

translation_service = TranslationService()

@app.subscriber(TRANSLATION_QUEUE)
async def process_translation_request(message: RabbitMessage):
    try:
        message_data = message.json()
        text_to_translate = message_data.get("text", "")

        if text_to_translate:
            translated_text = translation_service.translate_text(text_to_translate)
            print(f"Translated text: {translated_text}")

            await send_to_result_queue(translated_text)
            
        else:
            print("Received an empty message or invalid format.")

    except Exception as e:
        print(f"Error processing translation request: {e}")
    