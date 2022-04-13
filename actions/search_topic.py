from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import os


class ActionTopicSearch(Action):

    def name(self) -> Text:
        return "topic_search_result"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            id_of_user = tracker.sender_id

            fo = open(f"{id_of_user}.txt", "r+")
            line = fo.read()
            fo.close()
            print (line)
            search_topics_set= set(())

            if line == '':
                dispatcher.utter_message(text="Nothing to search")
                dispatcher.utter_message(text="Add topics type- 'ok go'")
                return[]
            else:
                for a in line.split(','):
                    if a != '' :
                        search_topics_set.add(a)

                for names in search_topics_set:
                    dispatcher.utter_message(names)
                    file = open(f"{id_of_user}{names}.txt", "r+")
                    lines = file.read()
                    file.close()
                    dispatcher.utter_message(lines)
            

            return[]