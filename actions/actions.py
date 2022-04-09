# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset


class ActionSearchTopicDelete(Action):

    def name(self) -> Text:
        return "topic_search_delete"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        # topicget1 = tracker.get_slot("topicget1")
        dispatcher.utter_message(text="All search topics are deleted!")
        
        # msg = "jency"

        # return [SlotSet("topicget1", None)]
        return[AllSlotsReset()]
