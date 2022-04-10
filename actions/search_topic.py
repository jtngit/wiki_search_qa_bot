from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import wikipedia

def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

class ActionTopicSearch(Action):

    def clean_name(name):
        return "".join([c for c in name if c.isalpha()])

    def name(self) -> Text:
        return "topic_search_result"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        topicget1 = tracker.get_slot("topicget1")
        dispatcher.utter_message(text=f"search topics are : {topicget1}")
        topic_list = topicget1.split(',')
        for item in topic_list:
            topic_search = clean_name(item)

            # search in wiki #####
            
            info = wikipedia.summary(topic_search, auto_suggest=False)
            dispatcher.utter_message(topic_search)
            dispatcher.utter_message(info)
            
            ## save into a file ###
            # with open(f"{topic_search}.txt","w") as file:
            #     file.write(info)


        dispatcher.utter_message(text="seach completed sussessfully!!!!")

        return[]