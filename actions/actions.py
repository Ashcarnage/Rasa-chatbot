# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import webbrowser
class ValidateSchoolForm(Action):
    def name(self) -> Text:
        return "class_form"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:
#
        required_slots = ["class"]
        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:

                return [SlotSet("requested_slot",slot_name)]



        return [SlotSet("requested_slot",None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template="utter_timetable_val", Name=tracker.get_slot("class"))
        return []

class Actionvideo(Action):
    def name(self) -> Text:
       return "school_vd"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        url="https://www.youtube.com/watch?v=0_e-wmnYPsw"
        dispatcher.utter_message("... Playing the vedio!")
        webbrowser.open(url)
        return []


class timetablepic(Action):
    def name(self) -> Text:
        return "show_timetable"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("class")
        D={"12A":"https://i.imgur.com/ryzkY6I.jpeg","12B":"https://i.imgur.com/rR3zZAm.jpeg"}
        for dict in D.keys(): 
            print(name)
            if name==dict:
                val=D[dict] 
                print(val)   
                dispatcher.utter_message(image=val)
                
        return []

