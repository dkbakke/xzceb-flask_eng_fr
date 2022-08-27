import os
from ibm_watson import LanguageTranslatorV3,ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION='2022-08-25'

authenticator = IAMAuthenticator( apikey )
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    '''Translate english text to french'''
    try:
        translation = language_translator.translate(
            englishText,
            model_id='en-fr').get_result()
    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
    frenchText = translation["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    '''Translate french text to english'''
    try:
        translation = language_translator.translate( frenchText,
            model_id='fr-en').get_result()
    except ApiException as ex:
        print ( "Method failed with status code " + str(ex.code) + ": " + ex.message)
    englishText = translation["translations"][0]["translation"]
    return englishText
    