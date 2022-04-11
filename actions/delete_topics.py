from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import os

class ActionDeleteTopics(Action):

    def name(self) -> Text:
        return "topic_search_delete"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            delete_topic = tracker.get_slot("deltopic")

            fo = open("list_of_topics.txt", "r+")
            print ("Name of the file: ", fo.name)

            line = fo.read()
            # Close opened file
            fo.close()

            print(type(line))
            print (line)

            search_topic= set(())
            for a in line.split(','):
                if a != '' :
                    search_topic.add(a)

            print(search_topic)

            ## delete from inputs
            try:

                search_topic.remove(delete_topic)
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print(search_topic)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                os.remove("list_of_topics.txt")
                
                
    
                with open(f"list_of_topics.txt","w") as file:
                    for item in search_topic:
                        file.write(item+",")
                
                os.remove(f"{delete_topic}.txt")
                
                dispatcher.utter_message(text="deleted successfully")
                dispatcher.utter_message(text="your topics :")
                for item in search_topic:
                    dispatcher.utter_message(item+ ',')
                dispatcher.utter_message(text=f"type: \n 'search' - search topics \n 'delete' - delete entered topic \n 'ok go' - add more topics")
            except:
                dispatcher.utter_message(text="give a valid topic name")
                dispatcher.utter_message(text=f"type: \n 'search' - search topics \n 'delete' - delete entered topic \n 'ok go' - add more topics")



            return [SlotSet("deltopic", None)]
