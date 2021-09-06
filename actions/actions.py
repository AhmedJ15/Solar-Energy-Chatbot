# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher




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



# class ActionTest1(Action):

#     def name(self) -> Text:
#         return "action_receive_entity"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         Units = str(tracker.get_latest_entity_values("units"))

#         return [SlotSet("units", Units)]