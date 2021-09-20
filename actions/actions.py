# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

class ActionAskForums(Action):       #Make sure to check documentations and complete this actions function.

    def name(self) -> Text:
        return "action_ask_pk_city"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:

        Type = str(tracker.get_slot("SolutionType"))

        if Type.lower() == "residential":
            dispatcher.utter_message(text="So, where is your home located?")

        elif Type.lower() == "industrial":
            dispatcher.utter_message(text="So, where is your industry located in?")


        return []


class ActionStoreUnits(Action):

    def name(self) -> Text:
        return "action_receive_units"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        Units = str(tracker.get_slot("units"))
        dispatcher.utter_message(text=f"And how many {Units} is available in your area?")

        return [SlotSet("units", Units)]




class ActionVerifyYearlyBill(Action):

    def name(self) -> Text:
        return "action_verify_yearlybill"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        yearly_bill_string = str(tracker.get_slot("yearlybill"))

        if yearly_bill_string.isdigit() != True:
            dispatcher.utter_message(text="Please enter a correct number.")
            return []

        return []


class ActionResetFormsSlots(Action):

    def name(self) -> Text:
        return "action_cancel_invoice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        return [SlotSet("units", None), SlotSet("yearlybill", None), SlotSet("SolutionType", None), SlotSet("pk_city", None)]


# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         # tell the user they are being passed to a customer service agent
#         dispatcher.utter_message(text="I am passing you to a human...")
        
#         # assume there's a function to call customer service
#         # pass the tracker so that the agent has a record of the conversation between the user
#         # and the bot for context
#         call_customer_service(tracker)
     
#         # pause the tracker so that the bot stops responding to user input
#         return [ConversationPaused(), UserUtteranceReverted()]


class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation = tracker.events
        print(conversation)
        return []




# class ActionTest1(Action):

#     def name(self) -> Text:
#         return "action_receive_entity"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         Units = str(tracker.get_latest_entity_values("units"))

#         return [SlotSet("units", Units)]



# class ActionDefaultAskAffirmation(Action):

#     def name(self) -> Text:
#         return "action_default_ask_affirmation"


#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#     # get the most likely intent
#     last_intent_name = tracker.latest_message.intent.name

#     # get the prompt for the intent
#     intent_prompt = self.intent_mappings[last_intent_name]

#     # reply
#     message_number = random.randint(1, 4)
#     if message_number == 1:
#         message = "Peço desculpa, não tenho a certeza se percebi. Quis {}?".format(intent_prompt)
#     if message_number == 2:
#         message = "Lamento, não percebi bem. Quis {}?".format(intent_prompt)
#     if message_number == 3:
#         message = "Não tenho a certeza se percebi. Quis {}?".format(intent_prompt)
#     if message_number == 4:
#         message = "Não sei se percebi. Quis {}?".format(intent_prompt)
#     buttons = [{'title': 'Sim',
#                 'payload': '/{}'.format(last_intent_name)},
#                {'title': 'Não',
#                 'payload': '/out_of_scope'}]
#     dispatcher.utter_message(message, buttons=buttons)


# class ActionDefaultAskAffirmation(Action):
#     """Asks for an affirmation of the intent if NLU threshold is not met."""

#     def name(self) -> Text:
#         return "action_default_ask_affirmation"

#     # def __init__(self) -> None:
#     #     import pandas as pd

#     #     self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
#     #     self.intent_mappings.fillna("", inplace=True)
#     #     self.intent_mappings.entities = self.intent_mappings.entities.map(
#     #         lambda entities: {e.strip() for e in entities.split(",")}
#     #     )

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:

#         intent_ranking = tracker.latest_message.get("intent_ranking", [])
#         if len(intent_ranking) > 1:
#             diff_intent_confidence = intent_ranking[0].get(
#                 "confidence"
#             ) - intent_ranking[1].get("confidence")
#             if diff_intent_confidence < 0.2:
#                 intent_ranking = intent_ranking[:2]
#             else:
#                 intent_ranking = intent_ranking[:1]

#         # for the intent name used to retrieve the button title, we either use
#         # the name of the name of the "main" intent, or if it's an intent that triggers
#         # the response selector, we use the full retrieval intent name so that we
#         # can distinguish between the different sub intents
#         first_intent_names = [
#             intent.get("name", "")
#             if intent.get("name", "") not in ["out_of_scope"]
#             else tracker.latest_message.get("response_selector")
#             .get(intent.get("name", ""))
#             .get("full_retrieval_intent")
#             for intent in intent_ranking
#         ]
#         message_title = (
#             "Do you mean..."
#         )

#         entities = tracker.latest_message.get("entities", [])
#         entities = {e["entity"]: e["value"] for e in entities}

#         entities_json = json.dumps(entities)

#         buttons = []
#         for intent in first_intent_names:
#             button_title = self.get_button_title(intent, entities)
#             if "/" in intent:
#                 # here we use the button title as the payload as well, because you
#                 # can't force a response selector sub intent, so we need NLU to parse
#                 # that correctly
#                 buttons.append({"title": button_title, "payload": button_title})
#             else:
#                 buttons.append(
#                     {"title": button_title, "payload": f"/{intent}{entities_json}"}
#                 )

#         buttons.append({"title": "Something else", "payload": "/out_of_scope"})

#         dispatcher.utter_message(text=message_title) #, buttons=buttons)

#         return []
   


# class ActionDefaultAskAffirmation(Action):

#     def name(self) -> Text:
#         return "action_default_ask_affirmation"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(template="utter_ask_affirmation")
#         return [UserUtteranceReverted()]