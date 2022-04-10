from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import wikipedia
import os


def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

def store_topics_in_file(search_topic):
    
    set_topic.add(search_topic)
    print(set_topic)

    # save searched topics in a file
    
    os.remove("list_of_topics.txt")
    
    with open(f"list_of_topics.txt","w") as file:
        print("<<<<<<<<>>>>>>>>>")
        for item in set_topic:
            file.write(item+",")
    print("first **************************************")
    return set_topic


topics_list= []
set_topic= set(())
class ValidateTopicForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_topic_form"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        ######## Validate `topicget1` value. ########
        search_topic = tracker.get_slot("topicget1")

        name = clean_name(search_topic)
        if len(name) == 0:
            dispatcher.utter_message(text="Give a valid topic.")
            dispatcher.utter_message(text="To add topic, type - 'ok go' ")
            return [SlotSet("topicget1", None)]
        else:
            # check in wiki ####
            
            try:
                info = wikipedia.summary(name, auto_suggest=False)

                ## save into a file ###
                with open(f"{search_topic}.txt","w") as file:
                    file.write(info)
                    
                print("going correct path")

                set_topic= store_topics_in_file(search_topic)

                dispatcher.utter_message(text="ok, thanks.")
                dispatcher.utter_message(text=f"your topics= {set_topic} ")


                dispatcher.utter_message(text=f"type-  'search' - search topics && 'change' - change/delete entered topics && 'ok go' - add more topics")
                
                return [SlotSet("topicget1", None)]

            except:
                print("false input value given")
                try:
                    ## wiki without with auto suggesion
                    info= wikipedia.summary(name)

                    with open(f"{search_topic}.txt","w") as file:
                        file.write(info)

                    set_topic= store_topics_in_file(search_topic)
                    dispatcher.utter_message(text="ok, thanks.")
                    dispatcher.utter_message(text=f"your topics= {set_topic} ")

                    dispatcher.utter_message(text=f"type-  'search' - search topics && 'change' - change/delete entered topics && 'ok go' - add more topics")

                    return [SlotSet("topicget1", None)]
                except:
                    dispatcher.utter_message(text="false input value is given")
                    dispatcher.utter_message(text="Add topic type- ok go")
                    return [SlotSet("topicget1", None)]
