import argostranslate.package
import argostranslate.translate
from config import TRANSLATION_MODEL_PATH

class TranslationService:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        """
        Load the Argostranslate translation model for English to Persian.
        """
        argostranslate.package.install_from_path(TRANSLATION_MODEL_PATH)
        languages = argostranslate.translate.load_installed_languages()
        
        # Find the English to Persian model
        from_lang = next((lang for lang in languages if lang.code == "en"), None)
        to_lang = next((lang for lang in languages if lang.code == "fa"), None)

        # Set the model to the English to Persian translation model
        if from_lang and to_lang:
            self.model = from_lang.get_translation(to_lang)
            print("Model loaded successfully!")
        else:
            print("Translation model for English to Persian not found.")
    



    def translate_text(self, text: str) -> str:
        """
        Translate the provided text from English to Persian.
        """
        translated_text = self.model.translate(text)
        return translated_text
