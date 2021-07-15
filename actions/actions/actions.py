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

        required_slots = ["class","month","year"]
        
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
        D={"12A":"https://i.imgur.com/ryzkY6I.jpeg","12B":"https://i.imgur.com/rR3zZAm.jpeg","12C":"","12D":"","11A":"","11B":"","11C":"","11D":""}
        for dict in D.keys(): 
            print(name)
            if name==dict:
                val=D[dict] 
                print(val)   
                dispatcher.utter_message(image=val)
                
        return []



class timetablepic(Action):
    def name(self) -> Text:
        return "academic_calendar"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        month=tracker.get_slot("month")
        year=tracker.get_slot("year")
        D={"January":"Information of the academic year 2020-21 is not available! please retry","February":"Information of the academic year 2020-21 is not available! please retry",'March':"Information of the academic year 2020-21 is not available! please retry",'April':"https://i.imgur.com/f0Cffww.jpeg",'May':"https://i.imgur.com/ifhIV3S.jpeg",'June':"https://i.imgur.com/1UGk0jd.jpeg",'July':"https://i.imgur.com/oRUJAfj.jpeg",'August':"https://i.imgur.com/TskCuP9.jpeg",'September':"https://i.imgur.com/pb1zmal.jpeg",'October':"https://i.imgur.com/1bgxlEU.jpeg",'November':"https://i.imgur.com/KFOnmNq.jpeg",'December':"https://i.imgur.com/iEU89bG.jpeg"}
        D1={"January":"https://i.imgur.com/6Qkp79F.jpeg","February":"https://i.imgur.com/yoQgyBs.jpeg",'March':"https://i.imgur.com/OVKzB8L.jpeg",'April':"https://i.imgur.com/yoioSU7.jpeg",'May':"https://i.imgur.com/wl3WklD.jpeg",'June':"https://i.imgur.com/rV5bzTJ.jpeg",'July':"https://i.imgur.com/sof0F4p.jpeg",'August':"https://i.imgur.com/xNj9NlK.jpeg",'September':"Sorry, the table has not been updated from August 2022 onwards! please retry",'October':"Sorry, the table has not been updated from August 2022 onwards! please retry",'November':"Sorry, the table has not been updated from August 2022 onwards! please retry",'December':"Sorry, the table has not been updated from August 2022 onwards! please retry"}
        if year=="2021":
            for i in D.keys():
                if i==month:
                    val= D[i]
                    print(val)
                    if val=="Information of the academic year 2020-21 is not available! please retry":
                        dispatcher.utter_message(response="utter_academic_calendar",text=val)
                    else:
                        dispatcher.utter_message(response="utter_academic_calendar",image=val)
        elif year=="2022":
            for i in D1.keys():
                if i==month:
                    val= D1[i]
                    print(val)
                    if val=="Sorry, the table has not been updated from August 2022 onwards! please retry":
                        dispatcher.utter_message(template="utter_academic_calendar",text="Sorry, the table has not been updated from August 2022 onwards! please retry")
                    else:
                        dispatcher.utter_message(template="utter_academic_calendar",image=val)


