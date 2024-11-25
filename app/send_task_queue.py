import json
from config import RESPONSE_QUEUE
async def send_to_result_queue(broker, message):
    await broker.publish(
        json.dumps(message),
        queue=RESPONSE_QUEUE
    )
    print(f"Sent translated text to result queue: {message}")
