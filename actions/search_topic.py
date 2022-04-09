from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset


class ActionTopicSearch(Action):

    def name(self) -> Text:
        return "topic_search_result"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        topicget1 = tracker.get_slot("topicget1")
        dispatcher.utter_message(text=f"search topics are : {topicget1}")
        dispatcher.utter_message(text="we can go through these topics!")

        return[]