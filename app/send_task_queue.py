import json
from config import RESPONSE_QUEUE
import logging


logger = logging.getLogger(__name__)
async def send_to_result_queue(broker, message):
    await broker.publish(
        json.dumps(message),
        queue=RESPONSE_QUEUE
    )
    logger.info(f"Sent translated text to result queue: {message}")
