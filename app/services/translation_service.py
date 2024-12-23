import argostranslate.package
import argostranslate.translate
from config import TRANSLATION_MODEL_PATH, MODEL_NAME
import logging
import os


logger = logging.getLogger(__name__)

class TranslationService:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        """
        Load the Argostranslate translation model for English to Persian.
        """
        full_path = os.path.join(TRANSLATION_MODEL_PATH, MODEL_NAME)
        argostranslate.package.install_from_path(full_path)
        languages = argostranslate.translate.load_installed_languages()
        
        from_lang = next((lang for lang in languages if lang.code == "en"), None)
        to_lang = next((lang for lang in languages if lang.code == "fa"), None)

        if from_lang and to_lang:
            self.model = from_lang.get_translation(to_lang)
            logger.info("Model loaded successfully!")
        else:
            logger.warning("Translation model for English to Persian not found.")


    def translate_text(self, text: str) -> str:
        """
        Translate the provided text from English to Persian.
        """
        translated_text = self.model.translate(text)
        return translated_text
