import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version='2022-08-25'

authenticator = IAMAuthenticator( apikey )
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    '''Translate english text to french''' 
    try:
        frenchText = language_translator.translate(
            englishText,
            model_id='en-fr').get_result()
    except ApiException as ex:
        print "Method failed with status code " + str(ex.code) + ": " + ex.message
    return frenchText
    

def frenchToEnglish(frenchText):
    '''Translate french text to english''' 
    try:
        englishText = language_translator.translate(
            frenchText,
            model_id='fr-en').get_result()
    except ApiException as ex:
        print "Method failed with status code " + str(ex.code) + ": " + ex.message
    return englishText
    