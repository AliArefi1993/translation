from faststream.rabbit import RabbitBroker, RabbitMessage
from faststream import FastStream
from services.translation_service import TranslationService
from config import RABBITMQ_HOST, TRANSLATION_QUEUE
from send_task_queue import send_to_result_queue
import json
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

broker = RabbitBroker(f"amqp://guest:guest@{RABBITMQ_HOST}/")
app = FastStream(broker)

translation_service = TranslationService()

@broker.subscriber(TRANSLATION_QUEUE)
async def process_translation_request(message: RabbitMessage):
    try:
        message_data = message.body
        message_json = json.loads(message_data)
        text_to_translate = message_json.get("text", "")
        chain = message_json.get("chain", "")
        request_id = message_json.get("request_id", "")

        if text_to_translate:
            translated_text = translation_service.translate_text(text_to_translate)
            message = {"translated_text":translated_text, "chain":chain, "request_id":request_id}
            logger.info(f"Translated text: {translated_text}")

            await send_to_result_queue(broker, message)
        else:
            logger.info("Received an empty message or invalid format.")
    except Exception as e:
        logger.error(f"Error processing translation request: {e}")

# Main entry point: Run FastStream app asynchronously
async def main():
    await app.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # Run the async main function