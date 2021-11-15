from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
import os

API_BASE_URL = 'https://api.hgbrasil.com/weather'
API_KEY = ''

def processar_msg_clima(clima):
  mensagem = f"O clima em {clima['city']} está com condição ({clima['description'].lower()}) com temperatura de {clima['temp']}°C e previsão de {clima['forecast'][0]['description'].lower()} para hoje."
  return mensagem
class ActionGetClima(Action):

  def name(self) -> Text:
    return "action_get_clima"

  def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
    query = tracker.get_slot('cidade')[0]
    params = f'?key={API_KEY}&city_name={query}'
    full_api_url = API_BASE_URL + params

    response = requests.get(full_api_url).json()

    mensagem = processar_msg_clima(response['results'])

    dispatcher.utter_message(text=mensagem)

    return []