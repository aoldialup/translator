import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
apikey = os.getenv('watson_key')

authenticator = IAMAuthenticator(apikey=apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)
language_translator.set_service_url(
    "https://api.us-east.language-translator.watson.cloud.ibm.com")

def english_to_french(text: str):
    res = language_translator.translate(text, source='en', target='fr')
    return res._to_dict()['result']['translations'][0]['translation']

def french_to_english(text: str):
    res = language_translator.translate(text, source='fr', target='en')
    return res._to_dict()['result']['translations'][0]['translation']