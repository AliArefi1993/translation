import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))

TRANSLATION_MODEL_PATH = "/app/app/models/translate-en_fa-1_5.argosmodel"

ASR_QUEUE = "asr_task_queue"
TRANSLATION_QUEUE = "translation_task_queue"
RESPONSE_QUEUE = "response_queue"