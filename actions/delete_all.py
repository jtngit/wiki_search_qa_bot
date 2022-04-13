from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import os

class ActionDeleteTopics(Action):

    def name(self) -> Text:
        return "delete_all_topics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


            id_of_user = tracker.sender_id

            fo = open(f"{id_of_user}.txt", "r+")
            line = fo.read()
            fo.close()

            search_topic= set(())
            for a in line.split(','):
                if a != '' :
                    search_topic.add(a)

            print(search_topic)

            for topi in search_topic:
                os.remove(f"{id_of_user}{topi}.txt")

            os.remove(f"{id_of_user}.txt")
                
            with open(f"{id_of_user}.txt","w") as file:
                file.write('')
            dispatcher.utter_message(text="all topics are removed successfully")
            dispatcher.utter_message(text=f"type: \n 'search' - search topics \n 'delete' - delete a specific topic \n 'ok go' - add more topics \n")
            return[]