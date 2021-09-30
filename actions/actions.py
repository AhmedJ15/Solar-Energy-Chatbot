# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Optional
import json

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

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

class ActionSetAreaSize(Action):

    def name(self) -> Text:
        return "action_set_areasize"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        areasize_string = str(tracker.get_slot("areasize"))

        return [SlotSet("areasize", areasize_string)]


class ActionResetFormsSlots(Action):

    def name(self) -> Text:
        return "action_cancel_invoice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        return [SlotSet("units", None), SlotSet("yearlybill", None), SlotSet("SolutionType", None), SlotSet("pk_city", None)]



class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation = tracker.events
        print(conversation)
        return []







class ValidateRestaurantForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_invoice_form3"

    def validate_customernumber(       #This will act as the def run for the specific slot.
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        #When using FormsValidationAction in your class, you can simply access the slot using slot_value.
        store_phonenumber = slot_value.lower()
        length_of_phonenumber = len(store_phonenumber)
        if (store_phonenumber.startswith("03") and length_of_phonenumber == 11) or (store_phonenumber.startswith("+92") and length_of_phonenumber == 13):
            #If Phone Number starts with 03 and has length 11 OR If Phone Number starts with +92 and has length 13, then set slot.
            return {"customernumber": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"customernumber": None}